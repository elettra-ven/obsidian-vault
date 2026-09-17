**Professor**: maria.victoriafeser@unibo.it

---
# Introduction

## Module Roadmap

This module introduces the main linear algebra tools that will be used throughout the course and, in particular, in the PCA module. It is based on the book *Mathematics for Machine Learning*.

The main themes are:

1. **Matrices and matrix operations**: notation, dimensions, multiplication, rank, determinants, inverses, traces, block matrices, and Kronecker products;
2. **Norms and distances**: quantitative measures of vector size and separation;
3. **Matrix decompositions**: Cholesky decomposition, eigendecomposition, spectral decomposition, and singular value decomposition;
4. **Vector calculus**: gradients, quadratic forms, Jacobians, the chain rule, and Hessian matrices;
5. **R illustrations**: practical computation of matrix operations, norms, decompositions, and linear systems.

The goal is not only to review definitions, but also to build the intuition and the algebraic tools needed for the statistical methods developed later in the course.

## Notation

Throughout this module, we use the following conventions:

- **bold lowercase letters** such as $\mathbf{x}$ denote vectors;
- **bold uppercase letters** such as $\mathbf{A}$ denote matrices;
- $\mathbf{0}_p$ denotes the zero vector in $\mathbb{R}^p$;
- $\mathbf{I}_p$ denotes the identity matrix of size $p\times p$;
- $\mathbf{x}^\top\mathbf{y}$ denotes the Euclidean inner product of two vectors;
- $\|\mathbf{x}\|_2$ denotes the Euclidean norm;
- matrix dimensions are written explicitly when useful, for example $\mathbf{A}\in\mathbb{R}^{n\times p}$.

---
# Matrices

## Definition

An $n \times m$ matrix $\mathbf{A}$ is a rectangular array with $n$ rows and $m$ columns:

$$
\mathbf{A} = [a_{ij}] =
\begin{bmatrix}
a_{11} & \cdots & a_{1m} \\
\vdots & \ddots & \vdots \\
a_{n1} & \cdots & a_{nm}
\end{bmatrix}.
$$

The entry in row $i$ and column $j$ is denoted $a_{ij}$.

## Addition and Subtraction

Two matrices can be added only if they have the same dimensions. If $\mathbf{A}=[a_{ij}]$ and $\mathbf{B}=[b_{ij}]$ are conformable for addition, i.e. $\mathbf{A}, \mathbf{B} \in \mathbb{R}^{m \times n}$, then

$$
\mathbf{A} + \mathbf{B} = [a_{ij}+b_{ij}].
$$

Properties:

- $\mathbf{A}+\mathbf{B}=\mathbf{B}+\mathbf{A}$,
- $(\mathbf{A}+\mathbf{B})+\mathbf{C}=\mathbf{A}+(\mathbf{B}+\mathbf{C})$,
- $\alpha(\mathbf{A}+\mathbf{B})=\alpha\mathbf{A}+\alpha\mathbf{B}$.

## Transposition

The transpose of an $n \times m$ matrix $\mathbf{A}$ is the $m \times n$ matrix obtained by swapping rows and columns:

$$
\mathbf{A}^\top = [a_{ji}].
$$



Useful identities:

$$
(\mathbf{A}^\top)^\top = \mathbf{A},
$$
and with $\mathbf{B}\in \mathbb{R}^{n \times m}$
$$
(\mathbf{A}+\mathbf{B})^\top = \mathbf{A}^\top + \mathbf{B}^\top,
$$

and with $\mathbf{C}\in \mathbb{R}^{m \times n}$
$$
(\mathbf{AC})^\top = \mathbf{C}^\top \mathbf{A}^\top.
$$

**Suggested Exercises 1 and 2.**

## Multiplication

Let $\mathbf{A}$ be an $n \times m$ matrix and $\mathbf{B}$ an $m \times k$ matrix. Then the product $\mathbf{C}=\mathbf{AB}$ is an $n \times k$ matrix with entries

$$
c_{ij} = \sum_{\ell=1}^m a_{i\ell}b_{\ell j}.
$$

That is, each entry is the inner product of the $i$-th row of $\mathbf{A}$ with the  $j$-th column of $\mathbf{B}$.


Properties for matrices of suitable dimensions:

- $(\mathbf{AB})\mathbf{C}=\mathbf{A}(\mathbf{BC})$, 
- $\mathbf{A}(\mathbf{B}+\mathbf{C})=\mathbf{AB}+\mathbf{AC}$, 
- $(\mathbf{A}+\mathbf{C})\mathbf{B}=\mathbf{AB}+\mathbf{CB}$, 
- in general, $\mathbf{AB} \neq \mathbf{BA}$.

**Suggested Exercise 3.**

## Scalar Multiplication

If $\alpha \in \mathbb{R}$ and $\mathbf{A}=[a_{ij}]$, then

$$
\alpha \mathbf{A} = [\alpha a_{ij}].
$$

This scales every matrix entry by the same factor.

## Identity Matrix

The identity matrix of size $n$ is

$$
\mathbf{I}_n =
\begin{bmatrix}
1 & 0 & \cdots & 0 \\
0 & 1 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & 1
\end{bmatrix}.
$$

For a square matrix $\mathbf{A}\in\mathbb{R}^{n\times n}$, it satisfies

$$
\mathbf{AI}_n = \mathbf{I}_n\mathbf{A} = \mathbf{A}
$$

More generally, if $\mathbf{A}\in\mathbb{R}^{n\times m}$, then

$$
\mathbf{A}\mathbf{I}_m=\mathbf{I}_n\mathbf{A}=\mathbf{A}.
$$
The order of the multiplication matters.

## Some Special Types of Matrices

- **Zero matrix** $\mathbf{0}$: all entries are zero.
- **Vector**: an $n \times 1$ matrix.
- **Vector of ones** $\mathbf{1}_n$: all entries equal 1.
- **Square matrix**: same number of rows and columns, i.e. $\mathbf{A}\in\mathbb{R}^{n\times n}$.
- **Symmetric square matrix**: $\mathbf{A}=\mathbf{A}^\top$.
- **Orthogonal square matrix**: $\mathbf{A}^\top\mathbf{A}=\mathbf{A}\mathbf{A}^\top=\mathbf{I}$. The columns and rows of $\mathbf{A}$ are orthonormal vectors.
- A nonsquare matrix $\mathbf{A}\in\mathbb{R}^{n\times m}$ with $m<n$ has $m$ orthonormal columns if $\mathbf{A}^\top\mathbf{A}=\mathbf{I}_m$. In that case, $\mathbf{A}\mathbf{A}^\top\neq\mathbf{I}_n$.
- **Diagonal matrix**: only diagonal entries may be nonzero.
- **Triangular matrix**: all entries above or below the diagonal are zero.
- **Idempotent square matrix**: $\mathbf{A}^2=\mathbf{A}\mathbf{A}=\mathbf{A}$.
- **Orthogonal square projector**: $\mathbf{A}^2=\mathbf{A}\mathbf{A}=\mathbf{A}$ and $\mathbf{A}=\mathbf{A}^\top$.
- A symmetric matrix $\mathbf{A}$ is **positive definite** if 
$$
\mathbf{x}^\top \mathbf{A} \mathbf{x} > 0 \quad \text{for all } \mathbf{x} \neq \mathbf{0}.
$$


## Rank of a Matrix

>[!NOTE] The rank of a matrix, denoted $\operatorname{rank}(\mathbf{A})$, is the number of linearly independent columns of $\mathbf{A}$. Equivalently, it is also the number of linearly independent rows.

Important facts:

$$
\operatorname{rank}(\mathbf{A}) = \operatorname{rank}(\mathbf{A}^\top) \leq \min(n,m).
$$

A matrix has **full rank** if its rank is the largest possible given its dimensions, i.e. $\min(n,m)$.

Additional properties:

- $\operatorname{rank}(\mathbf{AB}) \leq \min\{\operatorname{rank}(\mathbf{A}),\operatorname{rank}(\mathbf{B})\}$,
- $\operatorname{rank}(\mathbf{A}+\mathbf{B}) \leq \operatorname{rank}(\mathbf{A}) + \operatorname{rank}(\mathbf{B})$.

For a square matrix, full rank is closely tied to invertibility.

## Determinant ($|\mathbf{A}|$)

The determinant associates a scalar to a square matrix. It is denoted either $|\mathbf{A}|$ or $\det(\mathbf{A})$.

For small matrices:

- if $\mathbf{A}=[a_{11}]$, then $|\mathbf{A}|=a_{11}$,
- if $\mathbf{A}=\begin{bmatrix}a_{11} & a_{12} \\ a_{21} & a_{22}\end{bmatrix}$, then

$$
|\mathbf{A}| = a_{11}a_{22} - a_{12}a_{21},
$$

- for a $3 \times 3$ matrix, the formula is longer but follows the same principle.

Key properties:

- $|\mathbf{AB}| = |\mathbf{A}|\,|\mathbf{B}|$,
- $|\mathbf{A}^\top| = |\mathbf{A}|$,
- $|\alpha\mathbf{A}| = \alpha^n |\mathbf{A}|$ for an $n \times n$ matrix,
- $|\mathbf{I}_n|=1$.

>[!NOTE] A square matrix is **singular** if and only if its determinant is zero.

==**Suggested Exercise 4.**==

---
# Matrix Operations

One of the main applications of matrix algebra is the study of **linear systems**. A linear system is a collection of linear equations involving the same unknowns. In general, a system of $n$ equations in $p$ unknowns can be written as

$$
\begin{cases}
a_{11}x_1 + \cdots + a_{1p}x_p = b_1,\\
\qquad \vdots\\
a_{n1}x_1 + \cdots + a_{np}x_p = b_n.
\end{cases}
$$

Using matrix notation, these equations can be expressed compactly as

$$
\mathbf{A}\mathbf{x}=\mathbf{b},
$$

where $\mathbf{A}\in\mathbb{R}^{n\times p}$ is the **coefficient matrix**, $\mathbf{x}\in\mathbb{R}^p$ is the vector of unknowns, and $\mathbf{b}\in\mathbb{R}^n$ is the right-hand-side vector. Each row of $\mathbf{A}$ represents one equation, and each column contains the coefficients associated with one unknown.

Solving the system means finding all vectors $\mathbf{x}$ that satisfy every equation simultaneously. Depending on $\mathbf{A}$ and $\mathbf{b}$, a linear system may have no solution, exactly one solution, or infinitely many solutions. Matrix operations such as inversion, rank computation, and matrix decomposition help us determine which case occurs and, when solutions exist, compute them efficiently.

**Suggested Exercise 5.**

## Inverse Matrix

For a full-rank square matrix $\mathbf{A}\in\mathbb{R}^{n\times n}$, the inverse $\mathbf{A}^{-1}$ is defined by

$$
\mathbf{A}^{-1}\mathbf{A}=\mathbf{A}\mathbf{A}^{-1}=\mathbf{I}_n.
$$

If the inverse exists, the linear system

$$
\mathbf{A}\mathbf{x}=\mathbf{b}
$$

has solution

$$
\mathbf{x}=\mathbf{A}^{-1}\mathbf{b}.
$$

For a $2 \times 2$ matrix,

$$
\mathbf{A}=
\begin{bmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{bmatrix},
$$

its inverse is

$$
\mathbf{A}^{-1} = \frac{1}{a_{11}a_{22}-a_{12}a_{21}}
\begin{bmatrix}
a_{22} & -a_{12} \\
-a_{21} & a_{11}
\end{bmatrix},
$$

provided $a_{11}a_{22}-a_{12}a_{21} \neq 0$.

Useful identities:

$$
(\mathbf{A}^{-1})^{-1}=\mathbf{A}, \qquad
(\mathbf{AB})^{-1}=\mathbf{B}^{-1}\mathbf{A}^{-1},\; \mathbf{B}\in\mathbb{R}^{n\times n} \mbox{ of full rank}.
$$

>[!WARNING] A **singular** matrix has no solution, since its determinant is 0 and can't be a denominator. 

**Suggested Exercise 6.**

## Diagonal and Trace of a Matrix

The **diagonal** of a square matrix is the collection of entries $a_{11}, a_{22}, \dots, a_{nn}$.

>[!NOTE] The **trace** of a square matrix is the sum of its diagonal entries:

$$
\operatorname{tr}(\mathbf{A}) = \sum_{i=1}^n a_{ii}.
$$

Basic properties with $\mathbf{A},\,\mathbf{B}\in\mathbb{R}^{n\times n}$:

- $\operatorname{tr}(\mathbf{A}+\mathbf{B}) = \operatorname{tr}(\mathbf{A}) + \operatorname{tr}(\mathbf{B})$,
- $\operatorname{tr}(\alpha\mathbf{A}) = \alpha\operatorname{tr}(\mathbf{A})$,
- $\operatorname{tr}(\mathbf{AB}) = \operatorname{tr}(\mathbf{BA})$ when both products are defined.

**Suggested Exercise 7.**

## Partitioned Matrices

Many matrix calculations are easier when we partition a matrix into blocks. For instance,

$$
\mathbf{A} =
\begin{bmatrix}
\mathbf{A}_{11} & \mathbf{A}_{12} \\
\mathbf{A}_{21} & \mathbf{A}_{22}
\end{bmatrix}
$$

can be handled block-wise if the dimensions are compatible.

Example:

$$
\begin{bmatrix}
\mathbf{A}_{11} & \mathbf{A}_{12} \\
\mathbf{A}_{21} & \mathbf{A}_{22}
\end{bmatrix}
\begin{bmatrix}
\mathbf{x}_1 \\
\mathbf{x}_2
\end{bmatrix}
=
\begin{bmatrix}
\mathbf{A}_{11}\mathbf{x}_1 + \mathbf{A}_{12}\mathbf{x}_2 \\
\mathbf{A}_{21}\mathbf{x}_1 + \mathbf{A}_{22}\mathbf{x}_2
\end{bmatrix}.
$$

> $\mathbf{x}_{1}$ has to have the same dimension as $\mathbf{A}_{11}$!

A special case of a partitioned matrix is the **block-diagonal matrix**,
which has the following form:

$$
\mathbf{A}=\left[
\begin{matrix}
\mathbf{A}_{11} & 0 & 0 & 0\\
0 & \mathbf{A}_{22} & 0 & 0\\
0 & 0 & ... & ...\\
0 & 0 & ... & \mathbf{A}_{nn}
\end{matrix}
\right]  ,
$$
with $\mathbf{A}_{ii}$ square sub-matrices not necessarily of the same dimensions.

>[!WARNING] A **block-diagonal matrix** is not necessarily diagonal. It can be called a diagonal matrix if and only if the partitions are diagonal themselves.

Determinants, inverses, and transposes can also be defined for partitioned
matrices, and addition and multiplication can be applied to conformably partitioned
matrices. Let $\mathbf{A}$ and $\mathbf{B}$ be two conformably partitioned
matrices with:

$$
\mathbf{A}=\left[
\begin{matrix}
\mathbf{A}_{11} & \mathbf{A}_{12}\\
\mathbf{A}_{21} & \mathbf{A}_{22}
\end{matrix}
\right]  ,\mathbf{B}=\left[
\begin{matrix}
\mathbf{B}_{11} & \mathbf{B}_{12}\\
\mathbf{B}_{21} & \mathbf{B}_{22}
\end{matrix}
\right]  .
$$

Then,

* Addition: 
	The addends must have the same dimensions.
$$
\mathbf{A}+\mathbf{B}=\left[
\begin{matrix}
\mathbf{A}_{11}+\mathbf{B}_{11} & \mathbf{A}_{12}+\mathbf{B}_{12}\\
\mathbf{A}_{21}+\mathbf{B}_{21} & \mathbf{A}_{22}+\mathbf{B}_{22}
\end{matrix}
\right]  
$$

* Multiplication: 
$$
\mathbf{AB}=\left[
\begin{matrix}
\mathbf{A}_{11}\mathbf{B}_{11}+\mathbf{A}_{12}\mathbf{B}_{21} & \mathbf{A}_{11}\mathbf{B}_{12}+\mathbf{A}_{12}\mathbf{B}_{22}\\
\mathbf{A}_{21}\mathbf{B}_{11}+\mathbf{A}_{22}\mathbf{B}_{21} & \mathbf{A}_{21}\mathbf{B}_{12}+\mathbf{A}_{22}\mathbf{B}_{22}%
\end{matrix}
\right]  
$$

* Determinant, provided the required inverse exists:
$$
\left\vert \mathbf{A}\right\vert =\left\vert
\begin{matrix}
\mathbf{A}_{11} & \mathbf{A}_{12}\\
\mathbf{A}_{21} & \mathbf{A}_{22}
\end{matrix}
\right\vert =\left\vert \mathbf{A}_{11}\right\vert \left\vert \mathbf{A}_{22}-\mathbf{A}_{21}\mathbf{A}_{11}^{-1}\mathbf{A}_{12}\right\vert =\left\vert \mathbf{A}_{22}\right\vert \left\vert \mathbf{A}_{11}-\mathbf{A}_{12}\mathbf{A}_{22}^{-1}\mathbf{A}_{21}\right\vert.
$$

If $\mathbf{A}$ is a block-diagonal matrix:
$$
\left\vert \mathbf{A}\right\vert
=\left\vert
\begin{matrix}
\mathbf{A}_{11} & \mathbf{0}\\
\mathbf{0} & \mathbf{A}_{22}
\end{matrix}
\right\vert =\left\vert \mathbf{A}_{11}\right\vert \left\vert \mathbf{A}_{22}\right\vert 
$$

* Inverse: if $\mathbf{A}$ is a block-diagonal matrix:
$$
\mathbf{A}^{-1}=\left[
\begin{matrix}
\mathbf{A}_{11} & \mathbf{0}\\
\mathbf{0} & \mathbf{A}_{22}
\end{matrix}
\right]^{-1}=\left[
\begin{matrix}
\mathbf{A}_{11}^{-1} & \mathbf{0}\\
\mathbf{0} & \mathbf{A}_{22}^{-1}%
\end{matrix}
\right]
$$

This notation is very common in multivariate statistics.

## Kronecker Product

For matrices $\mathbf{A}\in\mathbb{R}^{n\times m}$ and $\mathbf{B}\in\mathbb{R}^{k\times l}$, the Kronecker product is

$$
\mathbf{C}=\mathbf{A} \otimes \mathbf{B} =
\begin{bmatrix}
a_{11}\mathbf{B} & \cdots & a_{1m}\mathbf{B} \\
\vdots & \ddots & \vdots \\
a_{n1}\mathbf{B} & \cdots & a_{nm}\mathbf{B}
\end{bmatrix},\;\; \mathbf{C}\in\mathbb{R}^{nk\times ml}.
$$

The dimensions of the matrixes don't have to match, for every index of the resulting matrix we pre-multiply the correct single element of $\mathbf{A}$ for the whole matrix $\mathbf{B}$.
It is useful for structured covariance matrices and vectorization identities.

---
# Norms and Distances

## Definition of Norms: 

Let $V$ be a vector space. A function

$$
\|\cdot\| : V \to \mathbb{R}
$$

is called a **norm** if, for all vectors $\mathbf{x},\mathbf{y} \in V$ and all scalars $\lambda \in \mathbb{R}$, it satisfies:

1. **Positive definiteness**
   $$
   \|\mathbf{x}\| \ge 0 \quad \text{and} \quad \|\mathbf{x}\| = 0 \iff \mathbf{x} = \mathbf{0}.
   $$

2. **Absolute homogeneity**
   $$
   \|\lambda \mathbf{x}\| = |\lambda|\,\|\mathbf{x}\|.
   $$

3. **Triangle inequality**
   $$
   \|\mathbf{x}+\mathbf{y}\| \le \|\mathbf{x}\| + \|\mathbf{y}\|.
   $$

These three properties guarantee that a norm behaves like a sensible measure of length.

### Common norms on $\mathbb{R}^n$

$\ell_1$ norm: For $\mathbf{x} = [x_1,\dots,x_n]^\top \in \mathbb{R}^n$,

$$
\|\mathbf{x}\|_1 = \sum_{i=1}^n |x_i|.
$$

This is often called the ==**Manhattan norm**==.

$\ell_2$ norm:

$$
\|\mathbf{x}\|_2 = \sqrt{\sum_{i=1}^n x_i^2}.
$$

This is the **Euclidean norm**.

$\ell_p$ norm: For $p \ge 1$,

$$
\|\mathbf{x}\|_p = \left(\sum_{i=1}^n |x_i|^p\right)^{1/p}.
$$

The $\ell_1$ and $\ell_2$ norms are special cases of the $\ell_p$ norm.

**Maximum norm** (or *infinite norm*):

$$
\|\mathbf{x}\|_\infty = \max_{1 \le i \le n} |x_i|.
$$

This norm measures the largest absolute component of the vector.

**Suggested Exercises 8 and 9.**

## Distances

Given a norm, the distance between two vectors $\mathbf{x}$ and $\mathbf{y}$ is defined by

$$
d(\mathbf{x},\mathbf{y}) = \|\mathbf{x}-\mathbf{y}\|.
$$

The definition works for any norm. Different norms lead to different distance measures. Because norms satisfy the three norm axioms, the induced distance has the expected properties:

1. **Non-negativity**
   $$
   d(\mathbf{x},\mathbf{y}) \ge 0.
   $$

2. **Identity of indiscernibles**
   $$
   d(\mathbf{x},\mathbf{y}) = 0 \iff \mathbf{x}=\mathbf{y}.
   $$

3. **Symmetry**
   $$
   d(\mathbf{x},\mathbf{y}) = d(\mathbf{y},\mathbf{x})
   $$
   because $\|\mathbf{x}-\mathbf{y}\| = \|-(\mathbf{y}-\mathbf{x})\| = \|\mathbf{y}-\mathbf{x}\|$.

4. **Triangle inequality**
   $$
   d(\mathbf{x},\mathbf{z}) \le d(\mathbf{x},\mathbf{y}) + d(\mathbf{y},\mathbf{z}).
   $$


A special case is given by the distance from the origin, i.e. the zero vector $\mathbf{0}$. Hence,

$$
d(\mathbf{x},\mathbf{0}) = \|\mathbf{x}-\mathbf{0}\| = \|\mathbf{x}\|.
$$

So the length of a vector is a special case of distance.

**Suggested Exercise 10.**

---
# Matrix Decompositions

## Cholesky Decomposition

For the Cholesky decomposition of a matrix $\mathbf{A} \in \mathbb{R}^{n \times n}$ to exist, the matrix must be:

- square,
- symmetric,
- positive definite (this can be checked with $det(\mathbf{A}) > 0$ and $det(\mathbf{A}) \neq 0$).

==Recall== that a symmetric matrix $\mathbf{A}$ is positive definite if

$$
\mathbf{x}^\top \mathbf{A} \mathbf{x} > 0 \quad \text{for all } \mathbf{x} \neq \mathbf{0}.
$$

>[!NOTE] If $\mathbf{A}$ is symmetric and positive definite, it admits a unique factorization:
>$$
\mathbf{A} = \mathbf{L}\mathbf{L}^\top,
$$

where $\mathbf{L}$ is a **lower-triangular matrix** with positive diagonal entries. The matrix $\mathbf{L}$ is called the **Cholesky factor**.

==This factorization can be viewed as a matrix analogue of taking a square root.==

**Suggested Exercise 11.**

For diagonal matrices

$$
\mathbf{A} = \begin{bmatrix}
a_{11} & 0 & 0 \\
0 & a_{22} & 0 \\
0 & 0 & a_{33}
\end{bmatrix},
$$

a valid Cholesky factor is simply

$$
\mathbf{L} = \begin{bmatrix}
\sqrt{a_{11}} & 0 & 0 \\
0 & \sqrt{a_{22}} & 0 \\
0 & 0 & \sqrt{a_{33}}
\end{bmatrix}.
$$

**Suggested Exercise 12.**

### Solving systems using Cholesky factors

The Cholesky decomposition is computationally important because it allows us to:

- solve **linear systems** efficiently when $\mathbf{A}$ is symmetric positive definite;
- compute **determinants** efficiently, since for $\mathbf{A} = \mathbf{L}\mathbf{L}^\top$,
  $$
  \det(\mathbf{A}) = \det(\mathbf{L})^2
  = \left(\prod_{i=1}^n l_{ii}\right)^2;
  $$
- avoid computing a full matrix inverse in many practical algorithms. Indeed, if

$$
\mathbf{A} = \mathbf{L}\mathbf{L}^\top,
$$

then solving

$$
\mathbf{A}\mathbf{x} = \mathbf{b}
$$

can be done in two triangular steps:

1. solve
   $$
   \mathbf{L}\mathbf{z} = \mathbf{b};
   $$
2. solve
   $$
   \mathbf{L}^\top \mathbf{x} = \mathbf{z}.
   $$

This is numerically attractive because triangular systems are easy to solve.

**Suggested Exercise 13.**

## Spectral Decomposition

The spectral decomposition of a matrix $\mathbf{A} \in \mathbb{R}^{n \times n}$ is a special case of eigendecomposition for a symmetric matrix. This decomposition is also called **matrix diagonalization**.

Let $\mathbf{p} \in \mathbb{R}^n$ be a nonzero vector. By definition, it is an **eigenvector** of $\mathbf{A}$ with corresponding **eigenvalue** $\lambda \in \mathbb{R}$ if

$$
\mathbf{A}\mathbf{p} = \lambda \mathbf{p}.
$$

This equation says that applying the linear map represented by $\mathbf{A}$ to the vector $\mathbf{p}$ changes only its scale, not its direction.

>[!NOTE] A matrix $\mathbf{A}$ is called **diagonalizable** if there exists an invertible matrix $\mathbf{P}$ such that
>$$
\mathbf{\Lambda} = \mathbf{P}^{-1}\mathbf{A}\mathbf{P},
$$
 
where $\mathbf{\Lambda}$ is diagonal. 

>[!info] If the columns of $\mathbf{P}$ are eigenvectors of $\mathbf{A}$ and the diagonal entries of $\mathbf{\Lambda}$ are the corresponding eigenvalues, then this factorization is the **eigendecomposition** of $\mathbf{A}$. 

For a real symmetric matrix, the eigenvectors can be chosen to be orthonormal, so $\mathbf{P}$ is **orthogonal**, i.e.

$$
\mathbf{P}^\top\mathbf{P}=\mathbf{I}_n.
$$


Then we have

$$
\mathbf{\Lambda} = \mathbf{P}^\top\mathbf{A}\mathbf{P},
$$

or, equivalently,

$$
\mathbf{A}=\mathbf{P}\mathbf{\Lambda}\mathbf{P}^\top.
$$

**Suggested Exercise 14.**

### How to Compute Eigenvalues and Eigenvectors

For hand calculations, the standard procedure is based on the **eigenvalue equation**

$$
\mathbf{A}\mathbf{x} = \lambda \mathbf{x}, \qquad \mathbf{x} \neq \mathbf{0}.
$$

This equation is equivalent to

$$
(\mathbf{A} - \lambda \mathbf{I})\mathbf{x} = \mathbf{0}.
$$

This reformulation shows that, for a given scalar $\lambda$, an eigenvector is simply a nonzero solution of a **homogeneous linear system** with coefficient matrix $\mathbf{A}-\lambda \mathbf{I}$. 

To obtain an eigenvector, the homogeneous system

$$
(\mathbf{A}-\lambda \mathbf{I})\mathbf{x} = \mathbf{0}
$$

must have a nontrivial solution. A homogeneous linear system has a nontrivial solution precisely when its coefficient matrix is **not invertible**. Therefore we require

$$
\det(\mathbf{A}-\lambda \mathbf{I}) = 0.
$$

Hence, the roots of 

$$
\det(\mathbf{A}-\lambda \mathbf{I})
$$

are the eigenvalues of $\mathbf{A}$.

So the general hand-computation procedure is:

1. form $\mathbf{A}-\lambda \mathbf{I}$;
2. compute $\det(\mathbf{A}-\lambda \mathbf{I})$;
3. solve the polynomial equation $\det(\mathbf{A}-\lambda \mathbf{I}) = 0$.

Once an eigenvalue $\lambda$ is known, substitute it back into

$$
(\mathbf{A}-\lambda \mathbf{I})\mathbf{x} = \mathbf{0}
$$

and solve the resulting homogeneous system. Any nonzero solution is an eigenvector associated with $\lambda$.

**Suggested Exercise 15.**


### Additional Properties

In the case of a diagonal matrix, say

$$
\mathbf{A} = \begin{bmatrix}
a_{11} & 0 \\
0 & a_{22}
\end{bmatrix},
$$
its eigendecomposition is immediate. We have $\mathbf{\Lambda} = \mathbf{A}$ and may take $\mathbf{P} = \mathbf{I}$. The eigenvalues are $a_{11}$ and $a_{22}$, with the standard basis vectors as eigenvectors:

$$
\mathbf{e}_1 = \begin{bmatrix}1 \\ 0\end{bmatrix}, \qquad \mathbf{e}_2 = \begin{bmatrix}0 \\ 1\end{bmatrix}.
$$


One practical reason to diagonalize a matrix is that powers of square matrices are easy to compute. Indeed, if

$$
\mathbf{A} = \mathbf{P}\mathbf{\Lambda}\mathbf{P}^{-1},
$$

then

$$
\mathbf{A}^k = \mathbf{A}\mathbf{A}\ldots= \mathbf{P}\mathbf{\Lambda}^k\mathbf{P}^{-1},
$$

with

$$
\mathbf{\Lambda}^k = \operatorname{diag}(\lambda_1^k,\dots,\lambda_n^k).
$$
Every real symmetric matrix can be diagonalized with an orthogonal matrix $\mathbf{P}$ such that $\mathbf{P}^\top\mathbf{P}=\mathbf{I}$. From $\mathbf{A} = \mathbf{P}\mathbf{\Lambda}\mathbf{P}^{-1}$ and $\mathbf{P}^{-1}=\mathbf{P}^\top$, we obtain

$$
\mathbf{\Lambda} = \mathbf{P}^\top \mathbf{A}\mathbf{P}.
$$

**Suggested Exercise 16.**


## Singular Value Decomposition

The singular value decomposition (SVD) extends eigendecomposition to **any real matrix**:

- square or rectangular,
- full rank or rank deficient,
- symmetric or nonsymmetric.

Let $\mathbf{A} \in \mathbb{R}^{m \times n}$. The SVD of $\mathbf{A}$ is

$$
\mathbf{A} = \mathbf{U}\mathbf{\Sigma}\mathbf{V}^\top,
$$

where:

- $\mathbf{U} \in \mathbb{R}^{m \times m}$ is an orthogonal matrix,
- $\mathbf{V} \in \mathbb{R}^{n \times n}$ is an orthogonal matrix,
- $\mathbf{\Sigma} \in \mathbb{R}^{m \times n}$ is diagonal in the rectangular sense, with nonnegative entries on the diagonal.

The diagonal entries of $\mathbf{\Sigma}$ are the **singular values** of $\mathbf{A}$:

$$
\sigma_1 \ge \sigma_2 \ge \cdots \ge \sigma_r > 0,
$$

where $r = \operatorname{rank}(\mathbf{A})$.


If $\mathbf{A}$ has rank $r$, then the **reduced SVD** is often more convenient:

$$
\mathbf{A} = \mathbf{U}_r \mathbf{\Sigma}_r \mathbf{V}_r^\top,
$$

where:

- $\mathbf{U}_r \in \mathbb{R}^{m \times r}$,
- $\mathbf{\Sigma}_r \in \mathbb{R}^{r \times r}$,
- $\mathbf{V}_r \in \mathbb{R}^{n \times r}$.

This form keeps only the singular vectors associated with nonzero singular values.


For each singular value $\sigma_i$, we have

$$
\mathbf{A}\mathbf{v}_i = \sigma_i \mathbf{u}_i,
\qquad
\mathbf{A}^\top \mathbf{u}_i = \sigma_i \mathbf{v}_i.
$$

A very useful way to write the SVD is

$$
\mathbf{A}
=
\sum_{i=1}^r \sigma_i \mathbf{u}_i \mathbf{v}_i^\top.
$$

Each matrix
$$
\sigma_i \mathbf{u}_i \mathbf{v}_i^\top
$$
has rank 1.

So the SVD decomposes the matrix into a sum of rank-1 pieces, ordered from most important to least important.


### Relation with Eigenvalues

Given that **$\mathbf{A} = \mathbf{U}\mathbf{\Sigma}\mathbf{V}^\top$**, we can write

$$
\mathbf{A}^\top \mathbf{A} = \mathbf{V}\mathbf{\Sigma}^\top \mathbf{\Sigma}\mathbf{V}^\top,
$$

so the right singular vectors **$\mathbf{V}$** are eigenvectors of $\mathbf{A}^\top \mathbf{A}$, and the eigenvalues of $\mathbf{A}^\top \mathbf{A}$ are

$$
\sigma_1^2, \sigma_2^2, \dots, \sigma_r^2.
$$

Similarly,

$$
\mathbf{A}\mathbf{A}^\top = \mathbf{U}\mathbf{\Sigma}\mathbf{\Sigma}^\top \mathbf{U}^\top,
$$

so the left singular vectors **$\mathbf{U}$** are eigenvectors of **$\mathbf{A}\mathbf{A}^\top$**.




# Vector Calculus

Vector calculus is one of the main mathematical tools needed in statistics and machine learning. The key reason is that many estimation/learning problems are phrased as optimization problems: we choose parameters to minimize a loss or maximize a likelihood. Gradients tell us how the objective changes when we change the parameters, and therefore point to directions used by optimization algorithms.

## Gradient 

When a function depends on several variables,

$$
f : \mathbb{R}^p \to \mathbb{R}, \qquad \mathbf{x} = (x_1,\dots,x_p)^\top,
$$

a **partial derivative** measures the rate of change with respect to one variable while keeping the others fixed.

For example, if $f(x_1,x_2)=x_1^2x_2+3x_2^2$, then

$$
\frac{\partial f}{\partial x_1} = 2x_1x_2,
\qquad
\frac{\partial f}{\partial x_2} = x_1^2 + 6x_2.
$$

For a scalar-valued function $f : \mathbb{R}^p \to \mathbb{R}$, the **gradient** is the column vector of partial derivatives:

$$
\nabla f(\mathbf{x}) =
\begin{bmatrix}
\frac{\partial f}{\partial x_1}\\[4pt]
\vdots\\[4pt]
\frac{\partial f}{\partial x_p}
\end{bmatrix}.
$$

The gradient points in the direction of steepest increase of $f$.

**Suggested Exercise 17.**

### Useful Results

Let $\mathbf{x}$ and $\mathbf{a}$ be vectors, and let $\mathbf{A}$ be a matrix. Then the following identities are extremely common:

$$
\nabla_{\mathbf{x}}(\mathbf{a}^\top \mathbf{x}) = \mathbf{a},
$$

$$
\nabla_{\mathbf{x}}(\mathbf{x}^\top \mathbf{a}) = \mathbf{a},
$$

$$
\nabla_{\mathbf{x}}(\mathbf{x}^\top \mathbf{x}) = 2\mathbf{x},
$$


$$
\nabla_{\mathbf{x}}(\mathbf{A}\mathbf{x}) = \mathbf{A}.
$$

### Quadratic Forms 

A quadratic form in $\mathbf{x}\in\mathbb{R}^{n}$ with a square matrix $\mathbf{A}\in\mathbb{R}^{n\times n}$ is an expression of the form

$$
f(\mathbf{x}) = \mathbf{x}^\top \mathbf{A}\mathbf{x}.
$$

If $\mathbf{A}$ is symmetric, then:

- $\mathbf{A}$ is **positive definite** if $\mathbf{x}^\top \mathbf{A}\mathbf{x} > 0$ for all nonzero $\mathbf{x}$,
- **positive semidefinite** if $\mathbf{x}^\top \mathbf{A}\mathbf{x} \ge 0$,
- **negative definite** if $\mathbf{x}^\top \mathbf{A}\mathbf{x} < 0$,
- **indefinite** if the sign depends on $\mathbf{x}$.

These concepts appear everywhere in statistics, especially for covariance matrices and Hessians.

We have that

$$
\nabla_{\mathbf{x}}\big(\mathbf{x}^\top \mathbf{A}\mathbf{x}\big)
= (\mathbf{A}+\mathbf{A}^\top)\mathbf{x},
$$

and if $\mathbf{A}$ is symmetric, this becomes

$$
\nabla_{\mathbf{x}}\big(\mathbf{x}^\top \mathbf{A}\mathbf{x}\big) = 2\mathbf{A}\mathbf{x}.
$$


## Jacobian and Hessian Matrices


### Jacobian Matrix

If a function maps a vector to another vector,

$$
\mathbf{f} : \mathbb{R}^p \to \mathbb{R}^n,
$$

with components $f_1,\dots,f_n$, then the collection of first derivatives is the **Jacobian**:

$$
\mathbf{J}(\mathbf{x}) =
\frac{\partial \mathbf{f}}{\partial \mathbf{x}} =
\begin{bmatrix}
\frac{\partial f_1}{\partial x_1} & \cdots & \frac{\partial f_1}{\partial x_p} \\
\vdots & \ddots & \vdots \\
\frac{\partial f_n}{\partial x_1} & \cdots & \frac{\partial f_n}{\partial x_p}
\end{bmatrix}.
$$

The Jacobian gives the best local linear approximation of a vector-valued function.




### Chain rule

The chain rule is central in many derivations. Let


$$
g : \mathbb{R}^p \to \mathbb{R}^k, \qquad
f : \mathbb{R}^k \to \mathbb{R}^n,
$$

then for the composition $\mathbf{h}(\mathbf{x}) = f(g(\mathbf{x}))$, the derivative combines the Jacobians of the pieces.

In the scalar-output case, this is often remembered as

$$
\nabla_{\mathbf{x}} f(g(\mathbf{x}))
= \mathbf{J}_g(\mathbf{x})^\top \nabla f(g(\mathbf{x})).
$$
with

$$
\mathbf{J}_g(\mathbf{x})=\begin{bmatrix}
\frac{\partial g_1}{\partial x_1} & \cdots & \frac{\partial g_1}{\partial x_p} \\
\vdots & \ddots & \vdots \\
\frac{\partial g_k}{\partial x_1} & \cdots & \frac{\partial g_k}{\partial x_p}
\end{bmatrix}.
$$

**Suggested Exercises 18 and 19.**

### Hessian Matrix

For a scalar-valued function $f : \mathbb{R}^p \to \mathbb{R}$, the matrix of second partial derivatives is the **Hessian**:

$$
\mathbf{H}_f(\mathbf{x}) =
\begin{bmatrix}
\frac{\partial^2 f}{\partial x_1^2} & \cdots & \frac{\partial^2 f}{\partial x_1 \partial x_p} \\
\vdots & \ddots & \vdots \\
\frac{\partial^2 f}{\partial x_p \partial x_1} & \cdots & \frac{\partial^2 f}{\partial x_p^2}
\end{bmatrix}.
$$

**Suggested Exercise 20.**



# `R` illustrations

In practical statistics and machine learning, we usually do **not** compute matrix inverses explicitly unless necessary. In `R`, one usually solves systems using `solve(A, b)` rather than `solve(A) %*% b`, because this is numerically better and more efficient.

## Basic matrix operations

```{r}
A <- matrix(c(1, 2, 3,
              4, 5, 6), nrow = 2, byrow = TRUE)
B <- matrix(c(1, 0, 1,
              0, 1, 1), nrow = 2, byrow = TRUE)

A
B
A + B
t(A)
```

## Matrix multiplication

```{r}
A <- matrix(c(1, 1, 1,
              2, 2, 2), nrow = 2, byrow = TRUE)
B <- matrix(c(3, 4,
              3, 4,
              3, 4), nrow = 3, byrow = TRUE)

A %*% B
```

## Solving a linear system

```{r}
A <- matrix(c(2, 3, 5,
              4, -2, -7,
              9, 5, -3), nrow = 3, byrow = TRUE)
b <- c(1, 8, 2)

solve(A, b)
```


## Rank, determinant, and inverse

```{r}
A <- matrix(c(1, 2,
              3, 5), nrow = 2, byrow = TRUE)

det(A)
solve(A)
qr(A)$rank
```

## Kronecker product 

```{r}
A <- matrix(c(1, 2,
              3, 4), nrow = 2, byrow = TRUE)
B <- matrix(c(0, 1,
              1, 0), nrow = 2, byrow = TRUE)

kronecker(A, B)

```

## Computing Norms and Distances

```{r norms-in-r}
x <- c(3, -4)

norm_l1 <- sum(abs(x))
norm_l2 <- sqrt(sum(x^2))
norm_linf <- max(abs(x))

c(l1 = norm_l1, l2 = norm_l2, linf = norm_linf)
```

For a general $p$-norm:

```{r pnorm-in-r}
x <- c(1, -2, 2)
p <- 3
(sum(abs(x)^p))^(1/p)
```

Computing distance:

```{r distances-in-r}
x <- c(1, 2)
y <- c(4, 6)

z <- x - y

c(
  d1 = sum(abs(z)),
  d2 = sqrt(sum(z^2)),
  dinf = max(abs(z))
)
```

A small helper function can be useful:

```{r distance-function}
distance_p <- function(x, y, p = 2) {
  z <- x - y
  if (is.infinite(p)) {
    return(max(abs(z)))
  }
  (sum(abs(z)^p))^(1/p)
}

distance_p(c(1, 0, -1), c(2, -2, 3), p = 2)
distance_p(c(1, 0, -1), c(2, -2, 3), p = 1)
distance_p(c(1, 0, -1), c(2, -2, 3), p = Inf)
```


## Matrix Decomposition


### Cholesky decomposition

```{r chol-example-2}
A <- matrix(c(4, 2, 2,
              2, 2, 1,
              2, 1, 3), nrow = 3, byrow = TRUE)

R <- chol(A)
L <- t(R)

L
L %*% t(L)
```


### Eigendecomposition

```{r}
S <- matrix(c(2, 1,
              1, 2), nrow = 2, byrow = TRUE)
eigen(S)
```


### SVD

```{r}
A <- matrix(c(3, 0,
              0, 1), nrow = 2, byrow = TRUE)

s <- svd(A)

s$u
s$d
s$v

A_reconstructed <- s$u %*% diag(s$d, nrow = length(s$d)) %*% t(s$v)
A
A_reconstructed
```


```{r}
A <- matrix(c(3, 2, 2,
              2, 3, -2), nrow = 2, byrow = TRUE)

s <- svd(A)

A
s$d
s$u
s$v

A
A_reconstructed <- s$u %*% diag(s$d, nrow = length(s$d)) %*% t(s$v)
round(A_reconstructed, 10)
```

