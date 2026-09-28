To apply the resolution principle to non-*ground* clauses, it is necessary to introduce the concept of **unification**.

>[!info] Unification
>A formal manipulation procedure used to establish when two expressions can be made to coincide by applying suitable substitutions.
>**It's a set of substitutions**.

>[!info] Substitution
>$\sigma$ is a set of bindings of terms $T_i$ to variable symbols $X_i$, $(i = 1,...,n)$

$$\sigma = \{ \frac{X_1}{T_1}, \frac{X_2}{T_2}, ..., \frac{X_n}{T_n}\}$$
Applying the substitution $\sigma$ to an expression $E$ produces a new expression $[E]\sigma$.

- if a **substitution** is applied, $[E]\sigma$ is called an **instance** of $E$.
- if a **renaming** (substitution that simply change the name of some variables) is applied, $[E]\sigma$ is called a **variant** of $E$.

>[!tip] Example of substitutions:
>Given the expression:
>$$p(X,f(Y),b,Z)$$
>We apply the substitution:
>$$\sigma = \{\frac{X}{c}, \frac{Y}{a}, \frac{Z}{W}\}$$
>
>The following instance is produced:
>$$p(c,f(a),b,W)$$

## Combining substitutions
We can compose two or more substitutions.
For example:
$$\sigma_1 = \{X_1/T_1, ..., X_n/T_n\}$$
$$\sigma_2 = \{Y_1/Q_1, ..., Y_m/Q_m\}$$
Then:
$$\sigma_1 \sigma_2 = \{X_1/[T_1]\sigma_2, ..., X_n/[T_n]\sigma_2, \ Y_1/Q_1,...,Y_m/Q_m\}$$
>[!info] Example:
>$$\sigma_1 = \{X/f(Z), W/R, S/c\}$$
>$$\sigma_2 = \{Y/X, R/W, Z/b\}$$
>Then:
>$$\sigma_1\sigma_2 = \{X/f(b), [\text{deleted}], S/c, Y/X, R/W, Z/b\}$$

>[!note] **More general substitution**
>A substitution $\theta$ is more general than a substitution $\sigma$ if there exists a substitution $\lambda$ such that $\sigma=\theta\lambda$.
## Unifying substitutions

Unification makes two or more atoms **identical** through a suitable substitution.
The substitution $\sigma$ is called **unifying substitution** if there exists a substitution $\sigma$ such that, for a set of atoms $[A_1,A_2,...,A_n]$:
$$[A_1]\sigma = [A_2]\sigma = ...= [A_n]\sigma$$
If this is the case, the set $[A_1,A_2,...,A_n]$ is also called **unifiable**.

>[!definition] **Most general unifier** (MGU)
>Several unifying substitutions may exist; we want to find the most general one.
# Unification algorithm

The *Unify* function takes as input parameters two atoms or terms to unify, A and B, and the substitution already applied so far.

The function always terminates and can return either the **MGS** of A and B or **failure**.

![[img/Pasted image 20260928125207.png|375]]
![[img/Pasted image 20260928125244.png|381]]

>[!info] Occur check
This is the check that a variable term being unified with a second term does not occur within that second term. 
It is necessary to ensure the algorithm terminates and that the unification procedure is correct.
>
>**For example:**
>
>Let's consider the terms
>- $p(X,f(X))$
>- $p(Y,Y)$
>  
>Without the occur check they unify, and the substitution produced (containing an infinite term) is $Y=f(f(f(...)))$
>
>So if $p$ represented the predicate "greater than" and f the successor function, it would follow that there exists a number greater than itself.
>
>However, this is an **unsound** proof.

# THE RESOLUTION PRINCIPLE FOR GENERAL CLAUSES (in which variables may occur)

Let $C_1,C_2$ be two clauses of the form:
$$C_1 = A_1 \vee ...\vee A_n$$
$$C_2 = B_1 \vee ...\vee B_n$$
Where $A_i$ and $B_j$ are a positive or negative literal in which variables may occur.

If there exist $A_i$ and $B_j$ such that $[A_i]\theta = \sim [B_j]\theta$, where $\theta$ is the MGU, then, a new clause $C_3$ can be derived as the resolvent:

$$[A_1 \vee ... \vee A_{i-1}\vee A_{i+1}\vee ... \vee A_{n}\vee B_1 \vee ... \vee B_{j-1}\vee B_{j+1}\vee ... \vee B_{m}]\theta$$

$C_3$ is a logical consequence of $C_1 \cup C_2$.

## Inference rule
In First-Order Logic, **Resolution** is an inference rule used to derive a new clause (a **resolvent**) from two parent clauses.
To do this, you must:

1. Find a **complementary pair** of literals (one positive, one negative predicate with matching names).
    
2. Find an **MGU (Most General Unifier)**, a substitution that makes those two conflicting literals completely identical so they can cancel each other out.
    
3. Combine all the **remaining** parts of both clauses, applying the MGU substitution to everything.

For example:
- **$C_1$:** $p(a,b) \lor q(X,a) \lor c(X)$
- **$C_2$:** $\sim p(a,Y) \lor \sim c(f(Y))$

To create the **resolvent** $C_3$, we target the $p$ predicate:
- **Literal from $C_1$:** $p(a, b)$
- **Literal from $C_2$:** $\sim p(a, Y)$

1. **Find the MGU**
	We need to make $p(a, b)$ and $p(a, Y)$ identical. To do this, we substitute variable $Y$ with the constant $b$.
	
	**MGU ($\theta$):** $\{Y/b\}$
	
	Once unified, $p(a, b)$ and $\sim p(a, b)$ cancel each other out (they "resolve").
2. **Apply substitution**
	- From $C_1$, we keep: $q(X, a) \lor c(X)$ (no $Y$ here, so nothing changes).
	- From $C_2$, we keep: $\sim c(f(Y))$ $\rightarrow$ replacing $Y$ with $b$ turns this into **$\sim c(f(b))$**.
	  
	  **Result ($C_3$):**

$$q(X,a) \lor c(X) \lor \sim c(f(b))$$

To create $C_4$, we target the $c$ predicate instead:
- **Literal from $C_1$:** $c(X)$
- **Literal from $C_2$:** $\sim c(f(Y))$

1. **Find the MGU**
	We need to make $c(X)$ and $c(f(Y))$ identical. To do this, we substitute variable $X$ with the function term $f(Y)$.
	
	**MGU ($\theta$):** $\{X/f(Y)\}$
	
	Once unified, they both become $c(f(Y))$ and cancel each other out.
2. **Apply substitution**
	- From $C_1$, we keep: $p(a,b)$ and $q(X,a)$ (that turns into $q(f(Y),a)$).
	- From $C_2$, we keep: $\sim p(a(Y))$.
	  
	  **Result ($C_4$):**

$$p(a,b) \lor q(f(Y),a) \lor \sim p(a,Y)$$
