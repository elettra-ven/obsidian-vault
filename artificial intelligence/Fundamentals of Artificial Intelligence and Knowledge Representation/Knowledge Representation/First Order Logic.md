We need to communicate in an non-ambiguous language.
For this purpose, we must agree on a rigorous language, free of ambiguity: **First Order Logic**.

## Symbols
Can be associated to concepts and used to create **sentences**.
The **act of reasoning** is a process from knowledge to a state that is "extracted" from it.

"Every human is mortal" + "Socrates is human" $\implies$ =="Socrates is mortal"==

We must rely on **logical consequence** for the interpretation of symbols:
Let $\Gamma = F_1,...,F_n$ be a set of sentences (hypotheses or premises, and 𝐹 be a sentence (conclusion). 

>[!note] Logical consequence
$F$ is a **logical consequence** of $\Gamma$, written $\Gamma \models F$, if for any possible different interpretation, it is always true that if all the formulas in $\Gamma$ are true (in the world under examination) then also $F$ is true.

### Propositional Logic
It illustrates ideas using propositions ($P_i$).
Each proposition is an **atomic formula** that can be either True or False, and can be connected to other atoms through **connectives** ($\vee, \wedge, \rightarrow, \neg, \text{ etc...}$).
If the single atoms/$P_i$ are well-formed, then their connections will also be well-formed formulas.
Logical connectives can be interpreted through "**truth tables**".

>[!note] Given an interpretation $\Im$, a formula $G$ is said to be true in $\Im$ if $G$ is evaluated to true in the interpretation.

>[!note] Given a formula $G$ and an interpretation $\Im$, if $G$ is true in $\Im$ we say that $\Im$ is a **model** for $G$, and usually write:
>$$\Im \models G$$

>[!info] Decidability
>There is always a terminating method to decide whether a formula is valid.
>
>To decide if a formula is valide we can **enumerate** all of the possible interpretation or look at the **formula** for each interpretation.

The goal of the propositional logic it to decide if **G** is a valid formula.
For this purpose, we temporally change the goal to *decide if, **given some formulas that are true**, G is also true*.
### Logical equivalence

![[Pasted image 20260921113635.png|502]]

This syntactic procedure is able to deduce the formulas from a formal problem (resolution). 
### Reasoning
It's a method that deals with symbols in order to decide if a specific formula-goal $G$ is valid.

>[!warning] Some definitions:
>- $x\models y$ : $y$ is a **logic consequence** of $x$.
>- $x\vdash^{E} y$ : $y$ can be **deduced** by $x$ using the reasoning $E$.

$$KB \text{ (Knowledge Based)} \vdash G \rightarrow \text{ soundness/correctness }\rightarrow KB \text{ (Knowledge Based)} \models G$$

$$KB \text{ (Knowledge Based)} \models G \rightarrow \text{ completeness }\rightarrow KB \text{ (Knowledge Based)} \vdash G$$

There are different methods of reasoning:

>[!important] Theorem of Reasoning by Deduction
>Given a set of formulas  $\{F_1, ... , F_n\}$ and a formula $G$,
>$F_1 \wedge ... \wedge F_n \models G$ if and only if $\models (F_1 \wedge ... \wedge F_n) \rightarrow G$

We can prove the logical consequence of G by proving the validity of $(F_1 \wedge ... \wedge F_n) \rightarrow G$.


>[!important] Theorem of Reasoning by Refutations
>Given a set of formulas  $\{F_1, ... , F_n\}$ and a formula $G$, 
>$F_1 \wedge ... \wedge F_n \models G$ if and only if $F_1 \wedge ... \wedge F_n \wedge \neg G$ is **inconsistent**.

We can prove the logical consequence of G by proving the inconsistency of $F_1 \wedge ... \wedge F_n \wedge \neg G$.

### Resolution rule
Together with the **refutation** mechanism can be used for *reasoning*.

It applies to logic formulas expressed in the form of clauses. 
A clause is a disjunction of literals. 
We consider a set of clauses in **Conjunctive Normal Form** (CNF): way of writing a logical formula as an **AND** of **ORs**.

Example of **resolution**:
![[Pasted image 20260921115343.png|517]]

---
## Example of Refutation and Resolution together

>[!tip] Goal
>We want to know if $F_1 \wedge ... \wedge F_n \models G$

We know that we can prove the above if we prove the **inconsistency** of $F_1 \wedge ... \wedge F_n \neg G$.
We must prove that there is no prossible interpretation $\Im$ that makes the formula ($F_1 \wedge ... \wedge F_n \neg G$) true.

We use **resolution**:
1. Transform our knowledge base KB in CNF form: 
	each conjunct will be a clause 
2. Negate the formula G and add it to the KB 
3. Apply the resolution principle (to all the clauses) until we reach the inconsistency

![[Pasted image 20260921115904.png|419]]

---
## Exercise

Given the following 
$$𝐾𝐵 = \{(a \rightarrow c \vee d) \wedge (a \vee d \vee e) \wedge (a \rightarrow \neg c )\}$$ Prove that $G = \{(d \vee e)\}$ is logical consequence of KB.

-  Transform in CNF the KB:
	1. $(\neg a \vee c \vee d)$
	2. $(a \vee d \vee e)$
	3. $(\neg a \vee \neg c)$
-  Negate the formula G:
	4. $\neg d$
	5. $\neg e$
-  Derive the possible resolvents (iterative):
	6. (1+2)
	7. (2 + 3)
	8. (1 + 4)
	9. (2 + 4)
	10. (2 + 5)
	11. (1 + 3)
	
	12. (10+11) $:\rightarrow d$
	
	13. (4+12): **empty clause** (contradiction)

The original formula G is logical consequence of the KB.

---

>[!note] Horn Clauses
>They have at most one positive literal.

A **literal** is an atom or its negation.

Horn Clauses are equivalent to $A \leftarrow B_1, ..., B_n$.

# FOL (First Order Logic)

## Terms
- A constant; 
- A variable; 
- If $f$ is a $n$-ary function symbol, and $t_1, ...,t_n$ are terms, then $f(t_1, ...,t_n)$ is also a term.

The **terms** are used as symbols to indicate objects of the problem.

>[!info] An **atom**/atomic formula is defined as the application of a $n$-ary predicate symbol $p$ to $n$ terms.
>$$p(t_1,...,t_n)$$

## WFF (Well Formed Formulas)
They are **recursively** defined as:
1. Every atom is a WFF
2. If $\phi$ and $\psi$ are WFF, their **logical connections** are also WFF.
3. If $\phi$ is a WFF, given a variable X, $\exists X \, \phi$ and $\forall X \, \phi$ are also WFF

