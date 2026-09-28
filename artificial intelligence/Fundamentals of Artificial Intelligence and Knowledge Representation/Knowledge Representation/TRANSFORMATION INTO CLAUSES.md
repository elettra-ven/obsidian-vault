Any well formed formula of predicate logic can be transformed into a set of general clauses.

## 1. Transformation into a **closed WFF**

Given the following initial formula:
$$\forall X (p(Y) \rightarrow \sim (\forall Y (q(X,Y) \rightarrow p(Y))))$$
it becomes:
$$\forall X \ \forall Y (p(Y) \rightarrow \sim (\forall Y (q(X,Y) \rightarrow p(Y))))$$

>[!info] **Closed** well-formed formula
>Every variable in the expression is **bound** by a quantifier.
>Closed WFFs express determinate propositions and evaluate to either **true** or **false** under a given interpretation.

## 2. Application of **equivalences** for logical connectives

For example, $A \rightarrow B$ (**if A happens then B happens as well**) is replaced by $\sim A \vee B$ (**either A doesn't happen, or B happens**).
The goal here is to reduce the formula to its **and-or** form.
$$\forall X \ \forall Y (\sim p(Y) \vee \sim(\forall Y(\sim q(X,Y) \vee p(Y))))$$

## 3. Applying **negation to atoms** rather than to compound formulas

>[!warning] Keep in mind that:
>1. $\forall X \ \sim A$ is equivalent to $\sim \exists X A$
>	
>	For all variables X, A is negated = It doesn't exist a variable X that verifies A
>	
>
>2. $\exists X \sim A$ is equivalent to $\sim \forall X A$
>	
>	A variable that negates A exists = it can't be said that A is verified for all variables X
>	
>	
>3. $\sim(A_1 \vee A_2 \vee ... \vee A_n)$ is equivalent to $\sim A_1 \wedge \sim A_2 \wedge ... \wedge \sim A_n$
> 	  
>4.  $\sim(A_1 \wedge A_2 \wedge ... \wedge A_n)$ is equivalent to $\sim A_1 \vee \sim A_2 \vee ... \vee \sim A_n$

$$\forall X \ \forall Y (\sim p(Y) \vee (\exists Y ( q(X,Y) \wedge \sim p(Y))))$$
## 4. Renaming of variables

$$\forall X \ \forall Y (\sim p(Y) \vee (\exists Z ( q(X,Z) \wedge \sim p(Z))))$$

The second variable $Y$ is named $Z$ to avoid conflicts

## 5. Moving the quantifiers to the front of the formula

$$\forall X \ \forall Y \exists Z ((\sim p(Y) \vee (q(X,Z) \wedge \sim p(Z)))$$

This is called **prenex formula**.

## 6. Conjunctive normal form

The formula is expressed as a **conjunction of disjunctions**, with the quantifiers up front.
$$\forall X \ \forall Y \exists Z ((\sim p(Y) \vee q(X,Z)) \wedge (\sim p(Y) \vee \sim p(Z)))$$

## 7. **Skolemization**

Every existentially quantified variable is **replaced by a function of the universally quantified variables that precede it.** 
For example $\forall X \ \exists Y \ p(X,Y)$ can be expressed as $\forall X \ p(X, g(X))$.
The variable that is replaces lies within the scope of the precedent quantifiers.
>This function is called a Skolem function.

$$\forall X \ \forall Y ((\sim p(Y) \vee q(X,f(X,Y))) \wedge (\sim p(Y) \vee \sim p(f(X,Y))))$$
This step loses expressiveness, but it still holds the properties necessary for proof procedures.
## 8. Elimination of universal quantifiers

$$((\sim p(Y) \vee q(X,f(X,Y))) \wedge (\sim p(Y) \vee \sim p(f(X,Y))))$$

A formula of this kind represents a set of clauses (each given by a conjunct in the formula). 
**The resulting clause normal form is**:

$$\{\sim p(Y) \vee q(X,f(X,Y)), \sim p(Y) \vee \sim p(f(X,Y))\}$$