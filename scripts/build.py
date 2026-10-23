#!/usr/bin/env python3
"""Compile the manuscript with Tectonic and repository-local resources."""
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import tarfile

root = Path(__file__).resolve().parents[1]
source_file = root / "rough_polynomial_fluctuation_theory.tex"
pdf_name = source_file.with_suffix(".pdf").name
sys.dont_write_bytecode = True
# Validate existing output paths before creating build state.
def validate_tree(paths):
    seen = set()
    pending = list(paths)
    while pending:
        path = Path(pending.pop()).resolve()
        if root not in path.parents:
            raise SystemExit(f"Build path escapes the repository: {path}")
        if path.is_dir() and path not in seen:
            seen.add(path)
            pending.extend(path.iterdir())
validate_tree([root / ".build", root / "build", source_file])
runtime = root / ".build"
def local(path):
    path = Path(path).resolve()
    if root not in path.parents:
        raise SystemExit(f"Output must remain inside the package: {path}")
    return path

paths = {name: local(runtime / name) for name in
         ["tools/downloads", "tools/tectonic", "cache", "cache/config",
          "cache/tectonic", "cache/texmf-var", "cache/texmf-config", "tmp", "output"]}
paths["output"] = local(root / "build")
for path in paths.values():
    path.mkdir(parents=True, exist_ok=True)
env = os.environ.copy()
env.update(TMPDIR=str(paths["tmp"]), XDG_CACHE_HOME=str(paths["cache"]),
           XDG_CONFIG_HOME=str(paths["cache/config"]),
           TECTONIC_CACHE_DIR=str(paths["cache/tectonic"]),
           TEXMFVAR=str(paths["cache/texmf-var"]),
           TEXMFCONFIG=str(paths["cache/texmf-config"]),
           PYTHONDONTWRITEBYTECODE="1", SOURCE_DATE_EPOCH="1792713600")
lock = json.loads((root / "scripts/tectonic.json").read_text())
platform_name = {("Darwin", "arm64"): "aarch64-apple-darwin",
                 ("Darwin", "x86_64"): "x86_64-apple-darwin",
                 ("Linux", "x86_64"): "x86_64-unknown-linux-musl",
                 ("Linux", "aarch64"): "aarch64-unknown-linux-musl"}.get(
                     (platform.system(), platform.machine()))
if not platform_name:
    raise SystemExit("Supported platforms: macOS/Linux, ARM64/x86_64")
asset = lock["assets"][platform_name]
archive = local(paths["tools/downloads"] / asset["name"])
offline = env.get("PAPER_OFFLINE") == "1"
if not archive.is_file():
    if offline:
        raise SystemExit("Offline rebuild needs the previously verified compiler archive")
    part = local(archive.with_suffix(archive.suffix + ".part"))
    subprocess.run(["curl", "--http1.1", "--fail", "--location", "--retry", "3",
                    "--connect-timeout", "20", asset["url"], "-o", str(part)],
                   env=env, check=True)
    if hashlib.sha256(part.read_bytes()).hexdigest() != asset["sha256"]:
        part.unlink()
        raise SystemExit("Tectonic official archive digest mismatch")
    part.replace(archive)
if hashlib.sha256(archive.read_bytes()).hexdigest() != asset["sha256"]:
    raise SystemExit("Tectonic archive digest mismatch")
# Extract only the regular executable; no archive paths or links are trusted.
with tarfile.open(archive, "r:gz") as source:
    matches = [m for m in source.getmembers() if m.isfile() and Path(m.name).name == "tectonic"]
    if len(matches) != 1:
        raise SystemExit("Expected exactly one regular Tectonic executable")
    executable_bytes = source.extractfile(matches[0]).read()
binary = local(paths["tools/tectonic"] / "tectonic")
if not binary.is_file() or binary.read_bytes() != executable_bytes:
    binary.write_bytes(executable_bytes)
    binary.chmod(0o755)
version = subprocess.check_output([str(binary), "--version"], env=env, text=True).strip()
if version.lower() != "tectonic 0.17.0":
    raise SystemExit(f"Unexpected compiler version: {version}")
bundle_hash_dir = local(paths["cache/tectonic"] / "bundles/hashes")
bundle_hash_file = local(bundle_hash_dir / lock["bundle"]["cache_hash_key"])
def check_bundle_identifier():
    if bundle_hash_file.is_file() and bundle_hash_file.read_text().strip() != lock["bundle"]["identifier"]:
        raise SystemExit("Tectonic bundle identifier changed; rebuild is not the recorded environment")
check_bundle_identifier()
command = [str(binary), "--bundle", lock["bundle"]["url"], "-Z", "deterministic-mode",
           "--keep-logs", "--keep-intermediates", "--outdir", str(paths["output"])]
if offline:
    command.append("--only-cached")
command.append(str(source_file))
subprocess.run(command, cwd=root, env=env, check=True)
check_bundle_identifier()
if not bundle_hash_file.is_file():
    raise SystemExit("Compiler did not record a verifiable bundle identifier")
record = {"compiler": version, "compiler_archive_sha256": asset["sha256"],
          "bundle_url": lock["bundle"]["url"],
          "bundle_identifier": bundle_hash_file.read_text().strip(),
          "source_sha256": hashlib.sha256((source_file).read_bytes()).hexdigest(),
          "rebuilt_pdf_sha256": hashlib.sha256((paths["output"] / pdf_name).read_bytes()).hexdigest()}
(paths["output"] / "rebuild.json").write_text(json.dumps(record, indent=2) + "\n")
print("Paper rebuilt:", paths["output"] / pdf_name)
