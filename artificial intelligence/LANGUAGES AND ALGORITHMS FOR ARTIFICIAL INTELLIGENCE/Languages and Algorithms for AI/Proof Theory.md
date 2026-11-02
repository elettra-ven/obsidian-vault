It's a way to prove logical consequences by using syntax:
- Logical proof
- Inexistence of a **counterexample** (for tautologies)

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
>$\wedge E$ is a **==dangerous rule==** if followed *top-down* (which is actually form $F$ to $F\wedge G$).
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
>*Example*:
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

---

>[!example] We want to prove $A\wedge B \vdash B\wedge A$
>$$
>\dfrac{
>{\dfrac{A\wedge B}{A}\wedge E_1\qquad \dfrac{A\wedge B}{B}\wedge E_2}
>}{B\wedge A}\wedge I
>$$

>[!example] We want to prove $\vdash A\wedge (B\wedge C) \implies B\wedge (C\wedge A)$
>>[!quote] $\vdash \dots$ is a **tautology**.
>$$
>
>\dfrac{
>\dfrac{\dfrac{\dfrac{[A\wedge(B\wedge C)]}{B\wedge C}\wedge E}{B}\wedge E \qquad
>\dfrac{\dfrac{\dfrac{[A\wedge(B\wedge C)]}{B\wedge C}\wedge E}{C}\wedge E \qquad \dfrac{[A\wedge(B\wedge C)]}{A}\wedge E}{C\wedge A}\wedge I}{B\wedge(C\wedge A)}\wedge I}{A\wedge (B\wedge C) \implies B\wedge (C\wedge A)}\implies I
>$$

>[!example] We want to prove $\vdash A\implies((A\implies\perp)\implies \perp)$
>$$\dfrac{\dfrac{\dfrac{[A\implies\perp]\qquad [A]}{\perp}\implies E}
>{(A\implies\perp)\implies \perp}\implies I }
>{A\implies ((A\implies \perp)\implies \perp}\implies I$$

>[!example] We want to prove $A\implies C, C\implies\perp \vdash A\implies (D\implies B)\wedge(C\implies D)$
>$$
>\dfrac
>{\dfrac
>{\dfrac{\dfrac{A\implies B \quad [A]}{B}\implies E}
>{D\implies B}\implies I \qquad\qquad\qquad 
>\dfrac{\dfrac{\dfrac{C\implies \perp}{\perp}\implies E}{D}\perp E}{C\implies D}\implies I}
>{(D\implies B)\qquad \wedge \quad(C\implies D)}\wedge I}
>{A\implies (D\implies B)\wedge(C\implies D)}\wedge I$$

---

The previous set of rules is **incomplete** in respect to classical logic.

>[!fail] For example
>It's impossible to prove $\vdash \neg \neg A \implies A$.

To make the set *classical-logic-complete* we need to add the following rule:
#### ==🔴Reduction Ad Absurdum==
$$(RAA)\qquad \frac{ \begin{matrix} [\neg\varphi] \\ \vdots \\ \perp \end{matrix} }{ \varphi }RAA$$
>[!tip] Reduction Ad Absurdum is **invertible**.
>We can always apply this rule, without making mistakes.
>However, it should be used as a last resort rule.

>[!done] Example with the **RAA** rule
>We want to prove that $\vdash \neg \neg A \implies A$.
>$$\dfrac{\dfrac{\dfrac{[(A\implies\perp)\implies\perp]\quad[A\implies\perp]}{\perp}\implies E}{A}\textbf{ RAA}}
>{\neg \neg A \implies A}\implies I$$

---

>[!example] We want to prove $((A\wedge B)\implies \perp)\implies\perp \ \vdash A$
>$$\dfrac{ \dfrac{ ((A\wedge B)\implies \perp)\implies\perp \quad \dfrac{ \dfrac{ [A\implies \perp] \quad \dfrac{[A\wedge B]}{A}\wedge E }{ \bot }\implies E }{ (A\wedge B)\implies \perp }\implies I }{ \bot }\implies E }{ A }\textbf{ RAA}$$

