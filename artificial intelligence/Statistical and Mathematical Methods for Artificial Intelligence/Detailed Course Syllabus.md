### Linear Algebra, Principal Component Analysis, Statistical Inference, and Regression

#### Maria-Pia Victoria-Feser
**email**: maria.victoriafeser@unibo.it

#### Autumn Semester 2026

- [1 Course Overview](#course-overview)
    - [1.1 Course Structure](#course-structure)
    - [1.2 Overall Learning Objectives](#overall-learning-objectives)
    - [1.3 Learning Progression Across the Course](#learning-progression-across-the-course)
- [2 Module 1: Basics of Linear Algebra](#module-1-basics-of-linear-algebra)
    - [2.1 Module Purpose](#module-purpose)
    - [2.2 Learning Objectives](#learning-objectives)
    - [2.3 Detailed Content](#detailed-content)
        - [2.3.1 1. Matrix notation and basic operations](#matrix-notation-and-basic-operations)
        - [2.3.2 2. Rank, determinants, and linear systems](#rank-determinants-and-linear-systems)
        - [2.3.3 3. Trace, block structure, and Kronecker products](#trace-block-structure-and-kronecker-products)
        - [2.3.4 4. Norms and distances](#norms-and-distances)
        - [2.3.5 5. Matrix decompositions](#matrix-decompositions)
        - [2.3.6 6. Vector calculus](#vector-calculus)
        - [2.3.7 7. Computational work in `R`](#computational-work-in-r)
    - [2.4 Connection to Later Modules](#connection-to-later-modules)
    - [2.5 Suggested Practice Status](#suggested-practice-status)
- [3 Module 2: Principal Component Analysis](#module-2-principal-component-analysis)
    - [3.1 Module Purpose](#module-purpose-1)
    - [3.2 Learning Objectives](#learning-objectives-1)
    - [3.3 Detailed Content](#detailed-content-1)
        - [3.3.1 1. Covariance matrices and their structure](#covariance-matrices-and-their-structure)
        - [3.3.2 2. PCA as variance maximization](#pca-as-variance-maximization)
        - [3.3.3 3. Spectral decomposition, scores, and reconstruction](#spectral-decomposition-scores-and-reconstruction)
        - [3.3.4 4. Choosing the number of components](#choosing-the-number-of-components)
        - [3.3.5 5. Data illustrations in `R`](#data-illustrations-in-r)
        - [3.3.6 6. PCA in high-dimensional settings](#pca-in-high-dimensional-settings)
    - [3.4 Connection to Other Modules](#connection-to-other-modules)
    - [3.5 Suggested Practice Status](#suggested-practice-status-1)
- [4 Module 3: Introduction to Statistics](#module-3-introduction-to-statistics)
    - [4.1 Module Purpose](#module-purpose-2)
    - [4.2 Learning Objectives](#learning-objectives-2)
    - [4.3 Detailed Content](#detailed-content-2)
        - [4.3.1 1. Probability foundations](#probability-foundations)
        - [4.3.2 2. Random variables and distributions](#random-variables-and-distributions)
        - [4.3.3 3. Moments, dependence, and quantiles](#moments-dependence-and-quantiles)
        - [4.3.4 4. Standard probability models](#standard-probability-models)
        - [4.3.5 5. Point estimation](#point-estimation)
        - [4.3.6 6. Properties and sampling distributions of estimators](#properties-and-sampling-distributions-of-estimators)
        - [4.3.7 7. Interval estimation](#interval-estimation)
        - [4.3.8 8. Bootstrap inference and coverage](#bootstrap-inference-and-coverage)
    - [4.4 Computational Competencies](#computational-competencies)
    - [4.5 Suggested Practice Status](#suggested-practice-status-2)
- [5 Module 4: Regression Models](#module-4-regression-models)
    - [5.1 Module Purpose](#module-purpose-3)
    - [5.2 Learning Objectives](#learning-objectives-3)
    - [5.3 Detailed Content](#detailed-content-3)
        - [5.3.1 1. Regression as conditional modeling](#regression-as-conditional-modeling)
        - [5.3.2 2. Gaussian linear regression](#gaussian-linear-regression)
        - [5.3.3 3. Classical estimation](#classical-estimation)
        - [5.3.4 4. Fitted values, projections, and residuals](#fitted-values-projections-and-residuals)
        - [5.3.5 5. Regression diagnostics](#regression-diagnostics)
        - [5.3.6 6. Polynomial regression and overfitting](#polynomial-regression-and-overfitting)
        - [5.3.7 7. Model assessment and selection](#model-assessment-and-selection)
        - [5.3.8 8. Shrinkage and regularization](#shrinkage-and-regularization)
    - [5.4 Computational Competencies](#computational-competencies-1)
    - [5.5 Suggested Practice Status](#suggested-practice-status-3)
- [6 Teaching and Learning Approach](#teaching-and-learning-approach)
- [7 Learning-Outcome Map](#learning-outcome-map)
- [8 Expected Integrative Competencies](#expected-integrative-competencies)

# 1 Course Overview

This four-module course develops the mathematical, statistical, and computational foundations needed to understand modern methods for data analysis and statistical learning. The course begins with linear algebra and vector calculus, uses these tools to derive principal component analysis (PCA), introduces probability and statistical inference, and concludes with regression, model assessment, and regularization.

The course emphasizes the connection between mathematical structure and statistical practice. Matrix decompositions are used to understand dimensionality reduction; probability models are treated as data-generating mechanisms; estimators are studied through their sampling distributions; and regression methods are evaluated according to both explanatory value and out-of-sample predictive performance.

Throughout the course, theoretical ideas are paired with reproducible illustrations in `R`. Simulations are used to connect population quantities with empirical behavior and to investigate results that are difficult to study analytically.

## 1.1 Course Structure

| Module | Title                                   | Central question                                                                                                                       |
| :----- | :-------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------- |
| 1      | [[Module 1 -- Basics of Linear Algebra]] | Which algebraic and differential tools are needed to formulate and solve statistical-learning problems?                                |
| 2      | Principal Component Analysis            | How can high-dimensional data be projected onto a lower-dimensional subspace while retaining as much information as possible?          |
| 3      | Introduction to Statistics              | How do probability models, estimators, sampling distributions, and confidence intervals connect data to unknown population quantities? |
| 4      | Regression Models                       | How can a response be explained and predicted from covariates while controlling model complexity and checking model assumptions?       |

## 1.2 Overall Learning Objectives

By the end of the course, students should be able to:

1. use vectors and matrices to represent multivariate data and statistical models;
2. perform and interpret fundamental matrix operations, norms, projections, and matrix decompositions;
3. connect eigendecomposition and singular value decomposition to PCA and low-rank approximation;
4. compute and interpret PCA scores, explained variance, projections, and reconstructions;
5. formulate probability models using events, random variables, distributions, moments, and conditional probabilities;
6. distinguish population quantities, empirical summaries, estimators, and realized estimates;
7. construct estimators using plug-in and maximum-likelihood principles;
8. evaluate estimators using bias, variance, mean squared error, consistency, and asymptotic normality;
9. construct and interpret exact, asymptotic, and bootstrap confidence intervals;
10. fit linear and polynomial regression models using least squares and maximum likelihood;
11. diagnose regression problems using residuals and graphical methods;
12. assess predictive performance using test error and cross-validation;
13. explain the bias–variance trade-off and apply ridge and lasso regression; and
14. implement, visualize, and critically interpret the principal methods in `R`.

## 1.3 Learning Progression Across the Course

The modules are designed to build on one another:

- **Module 1** supplies the common language of vectors, matrices, decompositions, projections, and optimization.
- **Module 2** applies that language to covariance matrices, principal directions, latent representations, and low-rank reconstruction.
- **Module 3** introduces the probability and inferential ideas needed to reason about random data, estimation uncertainty, and simulation-based procedures.
- **Module 4** combines the preceding algebraic and statistical tools in supervised learning, prediction, diagnostics, model selection, and regularization.

# 2 Module 1: Basics of Linear Algebra

## 2.1 Module Purpose

This module develops the linear algebra and vector-calculus tools used throughout the course. Its purpose is not only to review definitions, but also to build the geometric and computational intuition required for PCA, covariance matrices, least squares, and regularized regression.

## 2.2 Learning Objectives

By the end of Module 1, students should be able to:

1. identify matrix dimensions and determine whether proposed matrix operations are conformable;
2. perform matrix addition, transposition, multiplication, and scalar multiplication;
3. use transpose identities and distinguish matrix multiplication from elementwise multiplication;
4. recognize identity, diagonal, triangular, symmetric, positive-definite, and positive-semidefinite matrices;
5. compute and interpret matrix rank, determinants, inverses, and traces;
6. express and solve linear systems in matrix form and identify the role of rank and invertibility;
7. work with partitioned matrices and Kronecker products;
8. compute common vector norms and the distances induced by them;
9. verify the defining properties of a norm, including absolute homogeneity and the triangle inequality;
10. state the conditions for a Cholesky decomposition and use it to solve symmetric positive-definite systems;
11. compute eigenvalues and eigenvectors and interpret the spectral decomposition of a symmetric matrix;
12. explain the singular value decomposition of a rectangular or rank-deficient matrix;
13. connect singular values to the eigenvalues of A⊤A and AA⊤;
14. compute gradients, Jacobians, and Hessians for basic scalar- and vector-valued functions;
15. differentiate linear and quadratic forms; and
16. reproduce the main calculations with appropriate functions in `R`.

## 2.3 Detailed Content

### 2.3.1 1. Matrix notation and basic operations

- Matrix dimensions, entries, rows, and columns.
- Addition and subtraction of conformable matrices.
- Transposition and the identities
    
    (A+B)⊤=A⊤+B⊤,(AC)⊤=C⊤A⊤.
    
- Matrix multiplication as row-by-column inner products.
- Scalar multiplication and the identity matrix.
- Special matrix classes: square, diagonal, triangular, symmetric, positive definite, and positive semidefinite.

### 2.3.2 2. Rank, determinants, and linear systems

- Rank as the number of linearly independent rows or columns.
- Full rank and its relationship with invertibility.
- Determinants of small matrices and determinant identities.
- Singular matrices and the condition det(A)=0.
- Linear systems in the form
    
    Ax=b.
    
- Existence and uniqueness of solutions.
- Matrix inverses, including the inverse of a 2×2 matrix.
- Efficient solution of systems without explicitly forming a matrix inverse.

### 2.3.3 3. Trace, block structure, and Kronecker products

- Diagonal elements and the trace of a square matrix.
- Linearity and cyclic properties of the trace, including
    
    tr(AB)=tr(BA).
    
- Partitioned and block-diagonal matrices.
- Block matrix multiplication.
- Kronecker products and their role in structured matrices and covariance models.

### 2.3.4 4. Norms and distances

- Definition and axioms of a norm.
- The ℓ1, ℓ2, ℓp, and ℓ∞ norms.
- Absolute homogeneity:
    
    ∥λx∥2=|λ|∥x∥2.
    
- Distances induced by norms.
- Geometric interpretation of vector length and separation.

### 2.3.5 5. Matrix decompositions

- Cholesky factorization
    
    A=LL⊤
    
    for symmetric positive-definite matrices.
- Solution of linear systems by forward and backward substitution.
- Eigenvalues and eigenvectors through
    
    Ap=λp.
    
- Characteristic equation and hand computation of eigenpairs.
- Eigendecomposition and the spectral theorem for real symmetric matrices:
    
    A=PΛP⊤.
    
- Orthogonal eigenvectors and diagonalization.
- Singular value decomposition:
    
    A=UΣV⊤.
    
- Full and reduced SVD, rank-one expansions, and relationships with eigendecomposition.

### 2.3.6 6. Vector calculus

- Partial derivatives and gradients of scalar-valued functions.
- Gradients of linear and quadratic forms.
- Positive-definite and positive-semidefinite quadratic forms.
- Jacobian matrices for vector-valued functions.
- The multivariate chain rule.
- Hessian matrices and their role in curvature and optimization.

### 2.3.7 7. Computational work in `R`

- Creating and manipulating matrices.
- Matrix multiplication, transposition, rank, determinant, and inverse.
- Solving linear systems.
- Computing Kronecker products, norms, and distances.
- Computing Cholesky, spectral, and singular value decompositions.
- Checking algebraic identities numerically.

## 2.4 Connection to Later Modules

The spectral theorem and SVD lead directly to PCA in Module 2. Norms and projections provide the geometry of reconstruction and least squares. Gradients and quadratic forms are used to derive least-squares and penalized estimators in Module 4.

## 2.5 Suggested Practice Status

The current module identifies Suggested Exercises 1–20 throughout the notes, covering matrix identities, inverses, determinants, traces, norms, decompositions, and vector calculus.

# 3 Module 2: Principal Component Analysis

## 3.1 Module Purpose

This module develops PCA from three equivalent perspectives: variance maximization, orthogonal projection and reconstruction, and optimal low-rank approximation. It connects the spectral decomposition of a covariance matrix with practical dimensionality reduction and visualization.

## 3.2 Learning Objectives

By the end of Module 2, students should be able to:

1. construct an empirical covariance matrix from centered multivariate data;
2. prove that a covariance matrix is symmetric and positive semidefinite;
3. explain the rank bound for a centered covariance matrix, including high-dimensional settings;
4. formulate PCA as a constrained maximum-variance problem;
5. derive principal directions from the eigenvectors of the covariance matrix;
6. order principal components by their associated eigenvalues;
7. compute explained-variance proportions and cumulative explained variance;
8. select a reduced dimension q using explained variance, a scree plot, and reconstruction considerations;
9. compute latent scores using
    
    Z=XPq;
    
10. reconstruct centered data using
    
    Xˆ=XPqP⊤q;
    
11. interpret PqP⊤q as an orthogonal projector;
12. show that Xˆ=X when all p principal components are retained;
13. quantify projection and reconstruction error;
14. connect PCA with truncated SVD and the Eckart–Young–Mirsky theorem;
15. carry out PCA in `R` and interpret loadings, scores, explained variance, and reconstructions; and
16. apply PCA to both conventional multivariate data and high-dimensional image data.

## 3.3 Detailed Content

### 3.3.1 1. Covariance matrices and their structure

- Centering observations and constructing the centered data matrix.
- Empirical covariance under the 1/n convention and comparison with the 1/(n−1) convention.
- Variances on the diagonal and covariances off the diagonal.
- Symmetry, positive semidefiniteness, and nonnegative eigenvalues.
- Rank bounds and the special case n≪p.

### 3.3.2 2. PCA as variance maximization

- Projection of an observation onto a unit direction.
- Variance of the projected scores:
    
    var(z)=p⊤Sp.
    
- Unit-length constraint and the Rayleigh quotient.
- Lagrange-multiplier derivation of the eigenvalue equation.
- First principal direction as the eigenvector associated with the largest eigenvalue.
- Subsequent orthogonal directions and decreasing explained variance.

### 3.3.3 3. Spectral decomposition, scores, and reconstruction

- Spectral decomposition of the covariance matrix.
- Principal directions and loading vectors.
- Latent scores in the principal-coordinate system.
- Orthogonal projection onto a q-dimensional principal subspace.
- Reconstruction from latent scores.
- Exact reconstruction when q=p and approximate reconstruction when q<p.
- Projection error and the information represented by discarded directions.

### 3.3.4 4. Choosing the number of components

- Individual explained-variance ratios.
- Cumulative explained variance.
- Scree plots and threshold-based choices of q.
- Balancing dimension reduction, interpretability, and reconstruction accuracy.
- Comparing reconstructions across different numbers of retained components.

### 3.3.5 5. Data illustrations in `R`

- A two-dimensional toy dataset for visualizing covariance, directions, projections, and reconstruction.
- Manual calculations and graphical interpretation.
- PCA of the iris data.
- Comparison of manual computations with standard `R` PCA output.
- Interpretation of loadings and colored score plots.

### 3.3.6 6. PCA in high-dimensional settings

- Computational difficulties when the number of variables is large.
- Covariance-based and SVD-based decompositions.
- Relationship between covariance eigenvalues and singular values.
- Truncated SVD and rank-q approximations.
- The Eckart–Young–Mirsky theorem and optimal approximation in Frobenius norm.
- Image data represented as vectors.
- Eigenimages, latent image scores, and reconstructions with different values of q.

## 3.4 Connection to Other Modules

Module 2 is the main direct application of the decompositions in Module 1. Its empirical covariance matrix anticipates the distinction between population and empirical quantities developed in Module 3. Its low-rank approximation and dimension-selection questions also foreshadow the model-complexity and prediction questions in Module 4.

## 3.5 Suggested Practice Status

The current module identifies Suggested Exercises 21–31. These exercises reinforce covariance-matrix properties, the linear-algebra interpretation of PCA, variance maximization, projection, reconstruction, dimension selection, and SVD-based formulations.

# 4 Module 3: Introduction to Statistics

## 4.1 Module Purpose

This module introduces probability models as data-generating processes and develops the connection between population quantities, observed data, estimators, sampling distributions, and confidence intervals. Analytical results and Monte Carlo simulations are used together to study statistical uncertainty.

## 4.2 Learning Objectives

By the end of Module 3, students should be able to:

1. define outcome spaces and events and apply basic set operations to events;
2. use probability axioms and set identities to compute event probabilities;
3. calculate and interpret conditional probability;
4. apply Bayes’ rule and the law of total probability;
5. characterize independence through joint and conditional probabilities;
6. distinguish discrete and continuous random variables and their probability functions;
7. use probability mass functions, densities, cumulative distribution functions, and joint distributions;
8. construct and interpret an empirical distribution function;
9. compute and interpret expectations, variances, covariances, correlations, and empirical moments;
10. use quantiles to summarize population and empirical distributions;
11. identify and simulate Bernoulli, binomial, uniform, Gaussian, multivariate Gaussian, and exponential models;
12. explain inverse-transform simulation from a uniform random variable;
13. distinguish a population parameter, an estimator, and an observed estimate;
14. construct plug-in and maximum-likelihood estimators;
15. evaluate an estimator using bias, variance, efficiency, mean squared error, and consistency;
16. explain the law of large numbers and central limit theorem in relation to estimator behavior;
17. design and interpret a Monte Carlo study of a statistical procedure;
18. construct asymptotic normal, exact Student, and bootstrap percentile confidence intervals;
19. interpret confidence level and coverage correctly; and
20. estimate the finite-sample coverage of an interval procedure through simulation.

## 4.3 Detailed Content

### 4.3.1 1. Probability foundations

- Outcome spaces, realizations, and events.
- Intersections, unions, complements, and mutually exclusive events.
- Venn-diagram representations and set identities.
- Probability functions and basic probability rules.
- Conditional probability and its interpretation.
- Medical-screening illustration of conditional reasoning.
- Bayes’ rule and the law of total probability.
- Independence of events and equivalent formulations when conditional probabilities are defined.

### 4.3.2 2. Random variables and distributions

- Random variables as functions on an outcome space.
- Supports and realizations.
- Discrete probability mass functions and continuous probability densities.
- Cumulative distribution functions and interval probabilities.
- Joint distributions and dependence between random variables.
- Empirical distribution functions as sample-based approximations of population distributions.

### 4.3.3 3. Moments, dependence, and quantiles

- Expectation and its linearity properties.
- Variance and the computational identity
    
    var(X)=E[X2]−(E[X])2.
    
- Variance under affine transformations and variance of sums.
- Covariance and correlation.
- Empirical means, variances, covariances, and correlations.
- Population and empirical quantiles, including the median and quartiles.

### 4.3.4 4. Standard probability models

- Bernoulli and binomial distributions for binary outcomes and counts.
- Uniform distributions and inverse-transform simulation.
- Gaussian distributions, standardization, and affine transformations.
- Multivariate Gaussian distributions, covariance matrices, and their connection with PCA.
- Exponential distributions for positive waiting times.
- Simulation and graphical comparison of empirical samples with theoretical distributions in `R`.

### 4.3.5 5. Point estimation

- Statistical models and unknown parameters.
- Estimators as random variables and estimates as realized values.
- Plug-in estimation through replacement of a population distribution by the empirical distribution.
- Sample means and empirical covariance matrices as plug-in estimators.
- Likelihood and log-likelihood functions.
- Maximum-likelihood estimation for Bernoulli and Gaussian models.

### 4.3.6 6. Properties and sampling distributions of estimators

- Bias and unbiasedness.
- Sampling variance and efficiency.
- The 1/n decrease in the variance of the sample mean.
- Mean squared error and the bias–variance decomposition.
- Consistency and convergence in probability.
- Law of large numbers.
- Central limit theorem and asymptotic normality.
- Monte Carlo studies of sampling distributions, bias, variance, and consistency.

### 4.3.7 7. Interval estimation

- Confidence intervals as random intervals produced by a repeated-sampling procedure.
- Exact versus asymptotic distributions.
- Central Gaussian intervals based on asymptotic normality.
- Exact Student interval for a Gaussian mean with unknown variance.
- Standard errors and the role of sample size.

### 4.3.8 8. Bootstrap inference and coverage

- Nonparametric resampling from the observed empirical distribution.
- Bootstrap replicates and approximation of an estimator’s sampling distribution.
- Percentile bootstrap intervals.
- Manual bootstrap calculations and comparison with `boot::boot()` and `boot::boot.ci()`.
- Histograms of bootstrap distributions.
- Coverage as a property of an interval-construction procedure.
- Monte Carlo comparison of asymptotic, bootstrap-normal, and bootstrap-percentile intervals.

## 4.4 Computational Competencies

Students use `R` to generate random variables, draw histograms and density overlays, compute empirical moments and quantiles, simulate sampling distributions for multiple sample sizes, implement Monte Carlo experiments, construct bootstrap intervals, and estimate confidence-interval coverage.

## 4.5 Suggested Practice Status

Formal suggested exercises for Module 3 remain to be added. Natural exercise groups already supported by the module are probability identities, distribution calculations, moment properties, maximum-likelihood derivations, simulation studies of estimator behavior, bootstrap confidence intervals, and coverage experiments.

# 5 Module 4: Regression Models

## 5.1 Module Purpose

This module develops regression as a framework for conditional modeling, explanation, and prediction. It combines matrix algebra, probability, optimization, diagnostics, and resampling to move from the Gaussian linear model to polynomial regression, model selection, ridge regression, and lasso regression.

## 5.2 Learning Objectives

By the end of Module 4, students should be able to:

1. formulate a regression model as a conditional distribution for a response given covariates;
2. distinguish explanatory and predictive objectives;
3. write Gaussian linear regression in scalar and matrix form;
4. interpret intercept and slope coefficients in a multiple-regression model;
5. derive the least-squares estimator using matrix calculus and the normal equations;
6. state the rank conditions required for a unique least-squares solution;
7. show why Gaussian maximum likelihood and least squares give the same coefficient estimator;
8. estimate the regression error variance and distinguish the maximum-likelihood and unbiased estimators;
9. compute fitted values, residuals, residual sum of squares, and the hat matrix;
10. interpret least squares as an orthogonal projection onto the column space of the design matrix;
11. use standardized residuals and diagnostic plots to detect nonlinearity, heteroscedasticity, outliers, and departures from normality;
12. fit polynomial regression models using transformed covariates;
13. explain underfitting, overfitting, training error, test error, and the bias–variance trade-off;
14. compare models using out-of-sample RMSE and K-fold cross-validation;
15. formulate ridge and lasso estimation as penalized optimization problems;
16. compare the effects of L2 and L1 penalties on regression coefficients;
17. select a penalty parameter using cross-validation; and
18. interpret coefficient paths and selected models cautiously, especially after data-dependent lasso selection.

## 5.3 Detailed Content

### 5.3.1 1. Regression as conditional modeling

- Conditional distributions of a response given fixed covariates.
- Conditional mean functions and additional distributional parameters.
- Explanation, interpretation, and prediction.
- Regression as supervised learning and its contrast with unsupervised PCA.

### 5.3.2 2. Gaussian linear regression

- Scalar representation:
    
    Yi=x⊤iβ+εi.
    
- Matrix representation:
    
    Y=Xβ+ε.
    
- Interpretation of the intercept and slopes.
- Conditional mean and constant conditional variance assumptions.
- Fixed-design perspective.
- Illustration of simple linear regression in `R`.

### 5.3.3 3. Classical estimation

- Least-squares criterion and residual sum of squares.
- Gradient calculation, normal equations, and the estimator
    
    βˆLS=(X⊤X)−1X⊤y.
    
- Full-column-rank and dimensional conditions.
- Squared-error loss and empirical risk minimization.
- Gaussian likelihood and equivalence of least-squares and maximum-likelihood coefficient estimates.
- Maximum-likelihood and unbiased estimation of σ2.
- Degrees of freedom and residual sum of squares.

### 5.3.4 4. Fitted values, projections, and residuals

- Fitted values and in-sample predictions.
- Residual vectors and residual orthogonality.
- Hat matrix:
    
    H=X(X⊤X)−1X⊤.
    
- Least squares as orthogonal projection onto the column space of X.
- Residual-maker matrix In−H.
- Leverage values and standardized residuals.

### 5.3.5 5. Regression diagnostics

- Residuals versus fitted values and versus individual covariates.
- Correctly specified Gaussian examples.
- Curvature as evidence of nonlinearity.
- Funnel patterns as evidence of heteroscedasticity.
- Isolated residuals and outlying observations.
- Normal Q–Q plots and heavy-tailed errors.
- Distinguishing diagnostic evidence from formal proof of an assumption.

### 5.3.6 6. Polynomial regression and overfitting

- Polynomial feature vectors and models that are nonlinear in the covariate but linear in the coefficients.
- Comparison of polynomial degrees.
- Underfitting and excessive model flexibility.
- Training and test errors.
- High-degree polynomial illustrations.
- Why a small in-sample error does not guarantee accurate prediction.

### 5.3.7 7. Model assessment and selection

- Root mean squared prediction error.
- Independent test samples.
- U-shaped test-error behavior as model flexibility increases.
- Bias–variance considerations.
- K-fold cross-validation when a dedicated test sample is unavailable.
- Selection of polynomial degree using cross-validated RMSE.

### 5.3.8 8. Shrinkage and regularization

- Penalized least-squares criteria.
- Ridge regression with an L2 penalty.
- Closed-form ridge estimator and invertibility under regularization.
- Lasso regression with an L1 penalty.
- Sparsity and variable selection.
- Standardization and the treatment of the intercept.
- Coefficient paths as functions of the penalty parameter.
- Selection of λ by cross-validation.
- Interpretation of `lambda.min` and `lambda.1se`.
- Prediction-oriented interpretation and limitations of conventional post-selection inference.

## 5.4 Computational Competencies

Students use `R` to simulate regression data, fit linear and polynomial models with `lm()`, calculate predictions and residuals, construct diagnostic plots, compare training and test errors, implement cross-validation, and fit ridge and lasso models with `glmnet`.

## 5.5 Suggested Practice Status

Formal suggested exercises for Module 4 remain to be added. Natural exercise groups already supported by the module are matrix derivations of least squares, hat-matrix properties, residual diagnostics, polynomial model comparison, cross-validation, ridge calculations, and interpretation of lasso paths and selected variables.

# 6 Teaching and Learning Approach

The course combines four complementary modes of learning:

1. **Mathematical derivation:** students work from definitions and establish important identities and estimators.
2. **Geometric interpretation:** projections, norms, eigenspaces, and column spaces are used to explain PCA and least squares.
3. **Statistical interpretation:** formulas are connected to data-generating mechanisms, sampling variation, uncertainty, and prediction.
4. **Computational investigation:** reproducible `R` examples and simulations are used to verify calculations and explore finite-sample behavior.

Students should be encouraged to move repeatedly between formulas, verbal interpretations, graphical displays, and code. The objective is not merely to run standard functions, but to understand what those functions compute and which assumptions justify the resulting interpretation.

# 7 Learning-Outcome Map

|Competency|Module 1|Module 2|Module 3|Module 4|
|:--|:-:|:-:|:-:|:-:|
|Matrix and vector notation|Primary|Applied|Applied|Applied|
|Orthogonal projection|Introduced|Primary|–|Primary|
|Spectral decomposition and SVD|Primary|Primary|Connected through covariance|Used indirectly|
|Probability models|–|Empirical covariance context|Primary|Conditional models|
|Estimation and uncertainty|Optimization foundations|Empirical estimation context|Primary|Applied|
|Simulation in `R`|Basic computation|PCA illustrations|Primary|Model investigation|
|Prediction and model selection|–|Dimension selection|Inferential foundations|Primary|
|Low-dimensional or regularized modeling|Algebraic foundations|Low-rank PCA|Bias–variance foundations|Ridge and lasso|

# 8 Expected Integrative Competencies

After completing all four modules, students should be able to:

- translate a statistical problem into matrix notation;
- identify the algebraic structure that makes a computation possible;
- connect an empirical procedure to an underlying probability model;
- distinguish exact results, asymptotic approximations, and simulation-based evidence;
- interpret dimension reduction and regression as projection or optimization problems;
- assess the effect of model complexity on estimation and prediction;
- use `R` to reproduce a method and diagnose its behavior; and
- communicate results using mathematical notation, numerical summaries, and appropriate graphical displays.