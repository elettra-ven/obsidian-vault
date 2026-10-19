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

## Example
Let's compute a simple program that computes the **factorial** of a number:

```
fact(N,M):
```

Where `M = N!`
Let's add the clauses:

```
fact(0,1)
fact(N,M) :- N > 0, N1 is N-1, fact(N1,M1), M is N*M1
```

The factorial of `N` is the factorial of `N-1` (which is `M1`) multiplied for `N`.

```
:- fact(2,F)
:- 2 > 0, N1 is 2-1, fact(N1,M1), F is N*M1
:- fact(1,M1) F is 2*M1
```

We match this expression with the first clause fact(N,M) `fact(N,M) :- N>0, N1 is N-1, fact(N1,M1), M is N*M1`:

```
:- 1 > 0, N1 is 1-1, fact(N1',M1'), M1 is N*M1', F is 2*M1
:- fact(0,M1'), M1 is 1*M1', F = 2*M1
```

We reached the desired conclusion: `F = 2*M1`.

If we want, for instance, to compute the factorial of 3, we would call first the factorial of 2, which would call the factorial of 1, which would end by calling the clause factorial of 0.

However, **recursion is very expensive** in terms of resources and computational time.
We try to implement the factorial problem in a **non-tail recursion**:

```
fact1(N,Y) :- fact(N,1,1,Y)
fact1(N, M, ACC, ACC) :- M > N
fact1(N, M, ACCin, ACCout) :- ACCtemp is ACCin*M, M1 is M+1, fact1(N, M1, ACCtemp, ACCout)
```

Where `ACCin` and `ACCout` are Input and Output accumulators.

Another solution to the tail-recursive version of the factorial:

```
fact2(N,Y) 
	"Y is the factorial of N” 
fact2(N,Y) :- fatt2(N,1,Y)
fact2(0,ACC,ACC)
fact2(M,ACC,Y) :- ACC1 is M*ACC, M1 is M-1, fact2(M1,ACC1,Y).
```

---
# Lists
In Prolog, lists are terms build upon the special atom "empty list, `[ ]`" and the constructor operator "`.`”.

>[!abstract] Recursive definition:
>- The atom `[]` represents the empty list
>- The term `[T|List]` is a list if `T` is any term, and `List` is a list.
>  `T` is called "head of the list", while `List` is the "tail".

`[a | [b | [c|[]]]]` can be written as `[a, b, c]`.

>[!question] For example
>Define a predicate `isList` that is true only if the argument is a list.
>Starting from the recursive definition, T is a list if: 
>- T is an empty list, or 
>- T is a non empty list, and its tail is a list
>  
>  ```
>isList([]).
>isList([T|List]) :-
>	isList(List)
>  ```

>[!question] Predicate `lenght(L,N)`
>```
>lenght([],0)
>lenght([X|Tail],N) :-
>	lenght(Tail, Res)
>	N is Res
>```

>[!question] Predicate `append(L1,L2,L3)`
>Where `L3 = concat(L1,L2)`.
>
>```
>append([],L2,L2)
>append([L1|T1],L2,[L3|T3]) :-
>	append(T1,L2,T3)
>```

