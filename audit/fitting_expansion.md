# Fitting chapter expansion and verification

Presentation-only edits. No thesis, analysis-code, or notebook files were modified.

- `sections/07_fitting.tex`: 161 main-talk frames.
- `figures/thesis/fitting/coverage.json`: source-to-frame mapping with exact source-PDF crop rectangles in PDF points (origin at top left).
- All 80 unique figure/table PDF or EPS sources referenced by the fitting chapter are included. The union of displayed crop rectangles covers 100% of each original page. EPS assets were converted using epstopdf; other original PDFs were copied byte-for-byte. Cropped pages retain vector graphics.
- All four simultaneous-fit parameter tables and all four integration tables are editable TeX, retaining every source value and uncertainty. All 16 Gaussian candidates, ten named staple-width candidates, ten power-law/FT candidate rows, five constant-width separable candidates, five variable-width candidates, and four simultaneous separable alternatives are present.
- All four momenta include three amplitudes in both coordinate systems, both fixed-staple slice views, both Fourier output rows in 2D and 3D, complete fitted parameters, and complete numerical integration intervals.
- Standalone compilation using the presentation preamble succeeded with 162 pages and no overfull/underfull boxes. QA PDF: `/tmp/fitting_preview/driver.pdf`. Selected rendered pages were inspected for table readability, math layout, and crop boundaries. Full-source crop union coverage was checked programmatically.

## Verified corrections and qualifications in the presentation

1. PySR loss: thesis prose says absolute-value penalty and model-dependent N−k; embedded Julia implementation uses a squared-prediction penalty and N−3. Slides use the implemented objective, all five probe coordinates, weight .1, and invalid-evaluation handling. Finite probes do not prove integrability.
2. PySR Pareto expressions were cross-checked against `sivers_TMD_PhD_project/PySR/outputs_A2B_real/20260821_101855_eCTY5z/hall_of_fame.csv`, which also agrees with the plotting functions in `plots_for_Thesis/make_thesis_pysr_plots.py`. Exact stored C14 has expanded prefactor 39.36887156938522, not 39.71. Exact C16 has prefactor 18.768698420626166, not 245.5. The thesis C21 expression incorrectly moves the −0.003188983/eta term outside the multiplicative (10.300505/eta)^2.4254909 factor. Slides use exact stored shifted-exponential and grouped expressions, avoiding rounding ambiguity.
3. The actual Pareto CSV includes C5, C22, C23, C25, C27 omitted in the thesis table. All are now shown. The higher-complexity shifted profiles do not obey the required even parity automatically; the thesis assertion about b²-only dependence is restricted to its highlighted subset.
4. The Gaussian g2 width family is 1+u/eta−v/sqrt(eta), confirmed visually from the original vector table. It differs in signs from named power-law c6. The slide lists the full 4×4 family with original row IDs.
5. Fourier integrability: even power-law tails require j>1/2, but the odd numerator nu requires j''>1 for absolute integrability; both also require positive denominator coefficients. The highest-momentum fitted j'' is close to the latter boundary. Pure b²-dependent PySR expressions do not provide longitudinal decay at fixed b².
6. The parameterization (bL,bT) versus (nu,b²) is a coordinate transformation, not intrinsically a gain in independent data. The presentation states that the same retained data are encoded and acknowledges continuation beyond nu²<=PL² b².
7. The fit implementation has 15 independent Gaussian priors, every sigma=.05, in `save_h5_A12B_A2B/SimultaniousFit/SimultaneousFit_A12bA2B.py:197–247`. All prior means are included. Slides distinguish augmented chi² and reported lsqfit dof=Ndata from unregularized candidate statistics.
8. Ignoring covariance need not generically bias central values or always underestimate uncertainty. Slides describe changed weighting and potentially misestimated uncertainty without an unconditional bias claim.
9. For exp(−c|nu|), the even factor has a cusp in its first derivative; nu exp(−c|nu|) is continuously differentiable but has a second-derivative jump. Odd parity alone does not exclude the latter. Near-zero fitted widths indicate weakly constrained decay; only zero or negative widths establish the stated nondecaying/growing continuation. Negative amplitude coefficients are convention-dependent.
10. Antiquark convention: qbar(x)=−f1(−x) is stated for positive physical x. Small negative-x contributions are a model-selection expectation, not a universal theorem about sea quarks.
11. Finite-source normalization was checked numerically: P−1 whole-line E integral .889(24) agrees with a/(1+d*9)^j=.8889258 using the standardized 1/(2pi) convention. A stale notebook with unitary normalization must not be used to relabel the actual thesis artifacts. The later SimultaniousFit/SilumFitAmp_bsq_PL.ipynb includes the extra 1/sqrt(2pi) factor.
12. Source P−4 Fourier captions incorrectly say P−2; presentation titles use P−4. Source image headers with reversed inequalities (6>=eta>=10) are preserved as original vector evidence; slide captions state the correct 6<=eta<=10.

## Remaining provenance limits

The existing numerical artifacts were preserved, not refit. Neither the thesis nor source analysis notebooks were changed. The proposed Fourier-axis reinterpretation is withdrawn. Original x labels and the thesis interpretation are retained. Existing fit stability, prior sensitivity, covariance regularization, and per-resample Fourier-integrability claims require further analysis before stronger conclusions are justified.
