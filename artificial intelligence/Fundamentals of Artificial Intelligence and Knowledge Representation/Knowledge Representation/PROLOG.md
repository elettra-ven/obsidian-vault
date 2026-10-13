A Prolog program is a set of defined clauses of the form:
- **Fact**
	$A.$
- **Rule**
	$A :-\  B_1,B_2,...,B_n.$
	":-" is read as "implies".
- **Goal**
	$:- \ B_1,B_2,...,B_n$

where $A$ and $B_i$ are atomic formulas ($A$ is the *head* and $B$ is the *body* of the clauses).

>[!warning] atomic formulas
>They have the form:
>$$p(t_1,...t_n)$$
>
>- $p$ is the predicate symbol
>- $t_i$ are the terms

## Declarative interpretation
The formulas are defined by stating the knowledge about the problem.
The resolution will handle the rest.

`grandfather(X,Y) :- father(X,Z), father(Z,Y)`
	"For each X,Y, X is the **grandfather** of Y ***if it exists*** Z s.t. X is father of Z and Z is father of Y."
	same for:
`grandfather(X,Y) :- father(X,Z), mother(Z,Y)`

>[!tip] Theorem:
>A computation is the attempt to prove, through resolution, that a formula logically follows from the program.

If a problem can be expressed through Horn Clauses, it can be written as a Prolog program. The Prolog engine is then in charge of handling the resolution (**SLD**) of the goal.

>[!note] Example:
>`father(John,Mary)`
>`mother(Mary,Jane)`
>
>"Is it true that John is the grandfather of Jane?"
>	`:- grandfather(John,Jane)`
>"Is there any `X` such that John is the grandfather of `X`?"
>	`:- grandfather(John, X)`

Prolog SLD resolution has **two non-determinisms**:
- The rule of **computation** (it selects the "left-most" literal)
- The **search strategy** (DFS with chronological backtracking)

>[!abstract] DFS is **incomplete**.