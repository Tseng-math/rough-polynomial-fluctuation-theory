# Rough Polynomial Fluctuation Theory

## Coefficient-Uniform Jump, Variation, and Endpoint Bounds

**Tseng**

Preprint in harmonic analysis.
**Current public release:** [v1 (2026-08-28)](https://github.com/Tseng-math/rough-polynomial-fluctuation-theory/releases/tag/v1)
[**Read the paper (PDF)**](./rough_polynomial_fluctuation_theory.pdf) ·
[**LaTeX source**](./rough_polynomial_fluctuation_theory.tex) ·
[**Citation metadata**](./CITATION.cff)

---

## Overview

This manuscript studies the full sharp-truncation trajectory of rough singular integrals with an arbitrary real two-variable polynomial phase of bounded degree. The angular kernel is assumed only to belong to the endpoint class L log L and to have mean zero.

For the radial factor b = 1, the main theorem establishes coefficient-uniform critical 2-jump estimates on L^p for every p in the range 1 < p < infinity, together with the spatial weak-type (1,1) endpoint. The constants are independent of every coefficient of the polynomial phase; no nondegeneracy, smallness, or genericity assumption is imposed on the phase.

In the unphased case P = 0, the weak endpoint gives an independent resolution of the critical-jump problem posed by Jones, Seeger, and Wright. For general P, the result extends this endpoint to arbitrary bounded-degree two-variable polynomial phases.

The jump theorem further yields r-variation estimates for every r > 2, maximal-truncation bounds, almost-everywhere principal-value convergence, and a canonical truncation trajectory anchored at infinity. The theory also extends to bounded radial multipliers of finite total variation, with linear dependence on the BV size of the radial factor.

## Main results

- Critical 2-jump bounds on L^p for every 1 < p < infinity.
- Spatial weak-type (1,1) critical 2-jump endpoint.
- Constants uniform in all coefficients of the polynomial phase.
- No phase nondegeneracy, smallness, or genericity assumptions.
- Strong and weak r-variation consequences for every r > 2.
- Maximal-truncation estimates and almost-everywhere principal-value convergence.
- Extension to bounded radial BV multipliers.
- Independent treatment of the unphased weak endpoint P = 0.

Precise theorem statements, assumptions, constants, and comparison with the existing literature are given in the manuscript.

## Proof architecture

The proof combines a finite global algebraic flag on polynomial phases modulo pure input and output phases, coefficient-uniform annular decay, a phase-adapted Calderon-Zygmund decomposition with anchored phase-packet induction, concentration-stable equal- and unequal-shell correlation estimates, and a selector-free fixed-rank Rademacher-Menshov reduction.

The unphased weak endpoint is proved independently within the same framework.

## Versioning

The `main` branch contains the latest public version of the manuscript.

Fixed public versions are archived through GitHub Releases and tagged sequentially as `v1`, `v2`, `v3`, and so on. Earlier releases are retained as historical versions rather than being replaced by later revisions.

When citing the manuscript, please cite the specific released version when the distinction matters.

## Citation

Machine-readable citation metadata is provided in [`CITATION.cff`](./CITATION.cff).

GitHub's **Cite this repository** menu can be used to export citation information. If a persistent identifier such as a DOI is assigned later, the metadata will be updated accordingly.

## AI-use disclosure

The manuscript contains an explicit AI-use disclosure immediately following the abstract. Please consult the PDF or LaTeX source for the complete disclosure.
