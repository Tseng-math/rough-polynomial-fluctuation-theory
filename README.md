# Rough Polynomial Fluctuation Theory

## Coefficient-Uniform Critical Jumps, Finite Radial Variation, and Endpoint Bounds

**Tseng**

Preprint in harmonic analysis.

**Current public release:** [v2 (2026-08-31)](https://github.com/Tseng-math/rough-polynomial-fluctuation-theory/releases/tag/v2)

[**Read the paper (PDF)**](./rough_polynomial_fluctuation_theory.pdf) ·
[**LaTeX source**](./rough_polynomial_fluctuation_theory.tex) ·
[**Citation metadata**](./CITATION.cff)

---

## Overview

This manuscript develops a coefficient-uniform fluctuation theory for the full sharp-truncation trajectory of rough singular integrals with arbitrary bounded-degree real two-variable polynomial phases. The angular kernel is assumed only to lie in the endpoint class L log L and to have mean zero.

A central feature is that the critical 2-jump functional is genuinely pointwise: the supremum over jump amplitudes is taken before the spatial norm. For the unweighted radial factor b = 1, the paper proves coefficient-uniform pointwise critical 2-jump bounds on L^p for every 1 < p < infinity, together with the spatial weak-type (1,1) endpoint. The constants are independent of every coefficient of the polynomial phase, with no nondegeneracy, smallness, or genericity assumption.

At P = 0, the weak endpoint strictly strengthens, and hence independently resolves, the critical-jump problem posed by Jones, Seeger, and Wright. For general P, the principal-value weak-type (1,1) consequence answers the rough-kernel problem posed by Ding and Lai in the mean-zero L log L class.

The theory further extends to bounded radial factors of finite rho-variation for every fixed 1 <= rho < infinity. The constants remain independent of the polynomial coefficients and of where the radial variation is concentrated. For 1 <= rho < 2, there is also a direct pointwise Young-Stieltjes transfer; at and above rho = 2, the proof instead uses operator-specific Fourier, correlation, and packet-orthogonality arguments.

## Main results

- Pointwise critical 2-jump bounds on L^p for every 1 < p < infinity.
- Spatial weak-type (1,1) bounds for the pointwise critical 2-jump functional.
- Constants uniform in every coefficient of an arbitrary bounded-degree two-variable polynomial phase.
- No phase nondegeneracy, smallness, or genericity assumptions.
- Extension to every fixed finite radial variation exponent 1 <= rho < infinity.
- Strong and weak r-variation consequences for every r > 2.
- Maximal-truncation bounds and almost-everywhere principal-value convergence.
- A canonical trajectory determined by its finite-annulus increments and zero-at-infinity anchor.
- Sharpness and obstruction results for the pointwise-versus-mixed jump endpoint, the radial endpoint, and true quadratic output variation.

Precise theorem statements, hypotheses, constant dependencies, endpoint distinctions, and comparisons with the existing literature are given in the manuscript.

## Endpoint and sharpness picture

The paper also identifies several boundaries of the theory. The pointwise critical-jump endpoint is strictly stronger than the conventional mixed weak formulation. A scalar-path obstruction shows that the direct Young-Stieltjes transfer cannot be extended as a black-box argument to rho = 2, even though the operator-specific theory recovers every finite rho. A one-dimensional radial Hilbert example rules out rho = infinity, and an exact Mellin representation together with the Jones-Wang counterexample shows that true output V^2 already fails for sharp Hilbert truncations.

## Proof architecture

The polynomial phase is organized by a finite global algebraic flag modulo pure input and output phases. This provides a coefficient-uniform normalization that remains stable under simultaneous translation and accommodates convolution, genuinely nonconvolution, and diagonally degenerate phase geometries.

For the weak endpoint, a phase-adapted Calderon-Zygmund decomposition is combined with concentration-stable equal- and unequal-shell correlation estimates and a selector-free fixed-rank Rademacher-Menshov reduction. The packet arguments are arranged so that the relevant coefficients are fixed before the output point is evaluated.

The finite-radial theory is obtained by proving stability of the oscillatory, packet, weak-endpoint, and completion arguments under finite radial variation. The unphased weak endpoint is proved independently within the same framework.

## Scope of uniformity

The estimates are uniform in all coefficients of each fixed polynomial phase P of bounded degree. They do not take a pointwise supremum over polynomial phases inside the spatial norm.

Unless explicitly stated otherwise in a localized argument, the global constants depend only on the structural parameters displayed in the corresponding theorem and not on polynomial coefficients, truncation scales, auxiliary finite cutoffs, or approximation choices.

## Versioning

The `main` branch contains the latest public version of the manuscript.

Fixed public versions are archived through GitHub Releases and tagged sequentially as `v1`, `v2`, `v3`, and so on. Earlier releases are retained as historical versions rather than being replaced by later revisions.

When citing the manuscript, please cite the specific released version when the distinction matters.

## Citation

Machine-readable citation metadata is provided in [`CITATION.cff`](./CITATION.cff).

GitHub's **Cite this repository** menu can be used to export citation information. If a persistent identifier such as a DOI is assigned later, the metadata will be updated accordingly.

## AI-use disclosure

The manuscript contains an explicit AI-use disclosure immediately following the abstract. Please consult the PDF or LaTeX source for the complete disclosure.
