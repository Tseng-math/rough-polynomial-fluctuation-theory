# Critical Jumps for Rough Polynomial Carleson Operators with Angular Hardy Data and Finite Radial Variation

**Tseng** · Version 3 · Manuscript dated October 23, 2026

[Read the paper](rough_polynomial_fluctuation_theory.pdf) ·
[LaTeX source](rough_polynomial_fluctuation_theory.tex) ·
[Citation](CITATION.cff) · [Version notes](CHANGELOG.md)

This paper studies the complete sharp-truncation trajectories of rough singular
integrals with real polynomial phases on $\mathbb R^n\times\mathbb R^n$.
Its principal results are:

- **Strong critical jumps with polynomial modulation.** For mean-zero angular
  data in $H^1(\mathbb S^{n-1})$, every $1<p<\infty$, and a fixed radial
  amplitude of finite $\rho$-variation, $1\le\rho<\infty$, both the
  bounded-degree polynomial phase supremum and the jump-amplitude supremum
  are taken pointwise before the spatial $L^p$ norm. The bound is linear
  in the angular Hardy norm and the radial variation norm.
- **The fixed-phase weak endpoint.** Mean-zero angular $L\log L$ data give
  a weak type $(1,1)$ bound for the pointwise critical-jump functional,
  uniformly in the polynomial coefficients. This result also allows every
  fixed finite radial variation exponent.

The radial amplitude is fixed in these estimates; there is no supremum over
amplitudes. The Hardy space is angular. In dimensions at least two its mean-zero
subspace strictly contains the mean-zero angular $L\log L$ class. Both theorems concern entire
trajectories, including their annular identities and zero limit at infinity,
and imply maximal-truncation bounds, $r$-variation for every $r>2$, and
principal-value convergence. Counterexamples rule out unrestricted bounded
radial amplitudes and true quadratic output variation.

The paper includes precise comparisons with earlier work, including the radial
phase theorem of Ding–Liu (2011) and the fixed-phase weak estimates of Chen–Ji.

## Files and compilation

`rough_polynomial_fluctuation_theory.tex` is the complete source, including the
bibliography; `rough_polynomial_fluctuation_theory.pdf` is its compiled version.
`CITATION.cff` supplies GitHub's preferred manuscript citation.

Run:

```sh
bash scripts/build.sh
```

The script requires Python 3 and `curl`. It downloads the official
Tectonic 0.17.0 compiler, verifies its pinned SHA256 digest, and uses the pinned
TeX resource bundle. It supports macOS and Linux on ARM64 and x86_64. Compiler,
cache and temporary state stay in `.build/`; the rebuilt PDF and LaTeX log
are written to `build/`. Once the resources are cached,
`PAPER_OFFLINE=1 bash scripts/build.sh` builds without network access.

Alternatively, use a standard LaTeX installation with the packages listed in
the preamble and compile until the contents and references stabilize.

## Citation and versions

Use [CITATION.cff](CITATION.cff) or GitHub's **Cite this repository** menu to
cite the manuscript. Earlier versions remain available under their original
[tags and releases](https://github.com/Tseng-math/rough-polynomial-fluctuation-theory/releases).

## AI-use disclosure

The author selected the research objectives through interaction with AI systems;
the mathematical arguments and derivations were produced by those systems.
