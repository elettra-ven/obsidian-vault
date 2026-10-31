It's a way to prove logical consequences by using syntax.
It allows to use computation to perform **deduction** (or inference).

# Natural deduction

Natural deduction for propositional logic is a system that consists in a set of **rules** that allow to deduce or derive **conclusions from premises**.

>[!note] Connectives for Natural Deduction
>$$\wedge,\ \ \rightarrow,\ \ \perp.$$

## Rules

All rules either **introduce** or **eliminate** connectives.
### 1. Introduction Rules
1) if we know that two hypothesis $F$ and $G$ are both true we can day that $F \wedge G$ is true.
$$(\wedge I) \qquad \frac{\varphi \ \ \psi}{\varphi \wedge \psi}\wedge I$$

2) If assuming $G$ lets us derive $F$, if we know that $F$ is true, we can derive that $G \rightarrow F$.
$$(\rightarrow I)\qquad \frac{ \begin{matrix} [\varphi] \\ \vdots \\ \psi \end{matrix} }{ \varphi \rightarrow \psi } \; \rightarrow I$$
	$[\ ]$ indicates the **discard of the hypothesis**.

3) $\perp$ has no introduction rule. 
### 2. Elimination Rules

1) If we know that $F\wedge G$ is true, we can derive that $F$ is true.
$$(\wedge E) \qquad \frac{\varphi \wedge \psi}{\varphi} \wedge E \quad \frac{\varphi \wedge \psi}{\psi} \wedge E$$
>[!warning] Attention
>$\wedge E$ is a **dangerous rule** if followed *top-down* (which is actually form $F$ to $F\wedge G$).
>
>>[!quote] Invertible and non-invertible rules
>>Unsafe rules are also called **non-invertible**, whereas safe rules are called **invertible**.


2) If we know that $F \rightarrow G$ and that $F$ is true, we can derive that $G$ is true.
$$(\rightarrow E)\qquad \frac{\varphi\quad \varphi\rightarrow\psi}{\psi} \rightarrow E$$

>[!warning] Attention
>Again, $\rightarrow E$ is a **non-invertible** if followed *top-down* (which is actually form $G$ to $F,\ F\rightarrow G$).

3) $\perp$ has an elimination rule, ***everything* is a logical consequence of $\perp$**.
$$(\perp)\qquad \frac{\perp}{\varphi}\perp$$

>[!tip] Derivation trees
>Example:
>$$
>\dfrac{
>  \dfrac{
>    \dfrac{[\varphi \wedge \psi]^1}{\psi} \;\wedge E
>    \qquad
>    \dfrac{[\varphi \wedge \psi]^1}{\varphi} \;\wedge E
>  }{
>    \psi \wedge \varphi
>  } \;\wedge I
>}{
>  \varphi \wedge \psi \rightarrow \psi \wedge \varphi
>} \;\rightarrow I_1
>$$


