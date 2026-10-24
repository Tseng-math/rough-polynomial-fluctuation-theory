# Critical Jumps for Rough Polynomial Carleson Operators with Angular Hardy Data and Finite Radial Variation

**Tseng** · Version 4.1 · October 24, 2026

[Read the paper](rough_polynomial_fluctuation_theory.pdf) · [LaTeX source](rough_polynomial_fluctuation_theory.tex) · [Citation](CITATION.cff) · [Version history](CHANGELOG.md)

## Overview

This paper establishes critical-jump estimates for complete sharp-truncation trajectories of rough singular integrals with arbitrary bounded-degree real polynomial phases $P(x,y)$.

The main results are:

- **Maximally modulated strong estimates.** For mean-zero angular data in $H^1(\mathbb S^{n-1})$ and every $1<p<\infty$, both the polynomial-phase supremum and the critical-jump supremum are taken pointwise before the spatial $L^p$ norm.

- **Fixed-phase weak endpoint estimates.** For mean-zero angular data in $L\log L(\mathbb S^{n-1})$, the pointwise critical-jump functional satisfies a weak-type $(1,1)$ estimate for each fixed polynomial phase, uniformly in its coefficients.

Both results accommodate fixed radial amplitudes of finite $\rho$-variation for every $1\leq\rho<\infty$. Consequences include maximal-truncation bounds, $r$-variation estimates for $r>2$, and almost-everywhere principal-value convergence. The paper also establishes sharpness results for the radial and variation endpoints.

## Files and compilation

The manuscript is available as a [PDF](rough_polynomial_fluctuation_theory.pdf) and a complete, self-contained [LaTeX source](rough_polynomial_fluctuation_theory.tex).

To rebuild the PDF:

```sh
bash scripts/build.sh
```

The script requires Python 3 and `curl`. It downloads pinned TeX resources on the first run and keeps build files within the project. Subsequent offline builds are supported with `PAPER_OFFLINE=1 bash scripts/build.sh`.

## Citation

Citation metadata is provided in [CITATION.cff](CITATION.cff). Earlier versions remain available under the repository's [tags and releases](https://github.com/Tseng-math/rough-polynomial-fluctuation-theory/releases).

## AI-use disclosure

The author selected the research objectives through interaction with AI systems; the mathematical arguments and derivations were produced by those systems.
