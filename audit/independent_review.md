# Independent mathematical review

Reviewed 2026-10-20 by a fresh independent agent.

## Correction to the review

The proposed Fourier-axis sign and unit reinterpretations are withdrawn. They were not established against the complete generating conventions. At the author’s instruction, the presentation retains the original x convention, plots, numerical tables, and physical interpretation without relabeling or rescaling.

The only authorized thesis-source correction removes the spurious eta from the imaginary uppercase B1 denominator and its substitution into A2B. The thesis was pulled before editing; commit `6f5c572` was pushed to origin/main. Analysis code and notebooks were not changed.

## Reported fit statistics


`TMD_fit/jupyter/SimultaneousFit_A12bA2B.ipynb` supplies 15 Gaussian priors,
calls `lsqfit.nonlinear_fit(..., prior=current_prior, ...)`, and saves
`fit.chi2/fit.dof`. Many parameter-prior widths are 0.05. A later definition
uses logarithmic coordinates for three positive differences; the prior
penalty is in those fitted coordinates.

The reported objective therefore includes the prior penalty in addition
to the full-covariance data residual. It must not be described simply as
data chi-square divided by `N_data-15`, nor should all these priors be
called weak. With one prior per fitted parameter, lsqfit reports
`N_data` degrees of freedom. Its extrapolation with three data points and
two supplied parameter priors reports three, not the nominal frequentist
one. A local independent three-data/two-parameter fit confirmed dof=3.

This review did not rerun all fits, test prior sensitivity, or establish
which historical notebook execution produced every saved fit file.

## Normalization provenance correction

An initial concern based on the alternate
`TMD_fit/jupyter/SilumFitAmp_bsq_PL.ipynb` does **not** establish a
normalization error in the thesis figures.

That older copy lacks the `1/sqrt(2*pi)` conversion in its amplitude
prefactors and produces a unitary-normalized table with full integral
`2.228(59)` at PL=-1. In contrast, later functions in
`save_h5_A12B_A2B/SimultaniousFit/SilumFitAmp_bsq_PL.ipynb` divide the
prefactors by `sqrt(2*pi)`. The actual thesis table prints `0.889(24)`.
Its rounded spatial parameters give
`3.863/(1+9*0.163)^1.627 = 0.8889257809`,
consistent with the stated `1/(2*pi)` Fourier convention. All four
published full even integrals pass this normalization comparison:

| PL | Central spatial value at nu=0 | Thesis full integral |
| --- | ---: | ---: |
| -1 | 0.8889257809 | 0.889(24) |
| -2 | 1.0406197061 | 1.041(41) |
| -3 | 0.7567383846 | 0.759(69) |
| -4 | 0.8676322287 | 0.87(10) |

The stale alternate code differs by `sqrt(2*pi)=2.50662827463`;
common normalization cancels in shift ratios. No blanket normalization
warning or numerical rescaling of the thesis artifacts is warranted.

## Checks that passed

- The four gamma-channel projections are consistent with the displayed
  vector decomposition and metric. Their real/imaginary reflection signs,
  plus/minus-b1 matrices, even/odd combinations, and displayed inversions
  are algebraically consistent.
- The uppercase B1 mapping cancels eta in both real and imaginary parts.
  The inversion denominators require the stated nonsingular geometry.
- The three-point spectral sum and forward plateau normalization are
  mutually consistent.
- Independently evaluated oscillatory quadrature agrees with both
  displayed Bessel transforms to about 1e-11 for the nonsingular test
  parameters C=0.4, D=1.7, j=1.8, x=0.6, a=1.2.
- Absolute integrability requires j>1/2 for the even power law and j>1
  for the odd numerator. Near j=1 the odd transform's small-x limit
  deserves the qualification now present in the slides.
- The least-squares functional derivatives, alternating updates and
  weighted singular-value residual formula are correct. The numerical
  residuals concern fitted functions and their stated domains.

## Scope and limits

This was an independent review of revised source equations and selected
primary numerical artifacts, with direct code inspection and targeted
numerical checks. It is not certification of every equation embedded
inside every original plot panel, nor of the whole research pipeline.
Original figures and their x convention are retained. No fits or plot data were regenerated.

## Final presentation checks after withdrawing the axis reinterpretation

- Rebuilt `main.pdf`: 381 pages; no overfull or underfull box warnings.
- Figure inventory: all 184 thesis figure references covered in active main-talk frames.
- All pages rendered; zero text spans outside page bounds. Revised opening, Fourier definitions, result, integral-table, and conclusion pages visually inspected.
- Exact correlator check rerun: all four contractions and eight amplitude inversions passed; the imaginary uppercase B1 conversion cancels eta.
- Source and extracted PDF text checked for the removed axis-reinterpretation labels.
