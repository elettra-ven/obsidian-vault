Many problems in AI can be solved by searching in a **solution space**.
The process of finding the correct sequence/path to achieve a certain goal is called "**search**".

Searching is based on the exploration of a **search tree** that represents the expansion of all states starting from the initial state (the root of the tree).

>[!info] Expansion
>Starting from an initial state, and applying the operators (or successor function) the search will generate new states.

The **leaves** of the search tree (nodes that can't be expanded) represent **success** states or **failures** (dead ends).

![[Pasted image 20260924154344.png]]

Let's implement this:
![[Pasted image 20260924155213.png]]The *fringe* is the set of node that are not yet expanded.

# Non-informed search strategies
>Do not use any domain knowledge and apply rules arbitrarily.
>They are **not exhaustive** search strategies and they become impractical for complex problems.

Strategies are evaluated according to four criteria:
- **Completeness**: 
	does the strategy guarantees to find a solution if one exists?
- **Time complexity**: 
	how long does it take to find a solution?
- **Space complexity**: 
	how much memory is needed to carry out the search?
- **Optimality**: 
	does the strategy find the best solution when there are more solutions?


## 1. Breadth-first search
Breadth-first search always **EXPANDS LESS DEEP** tree nodes.
Let $d$ be the depth of a tree and $b$ be the branching factor, he maximum number of nodes expanded in the worst case will be $b^d$.
$$1+b+b^2+b^3+...+(b^d+1) \rightarrow b^d$$
This strategy ensures **completeness**, but doesn't have an **efficient implementation** on single threads.

### Uniform-cost BFS
This search is needed when the costs of each possible "searching move" are different.
The fringe is ordered according to the cost of the exploration. 
When queueing a successor, the **fifo** is always in order of increasing path cost.

## 2. Depth-first search
Depth-first EXPANDS **deepest** nodes first.
It requires less memory occupation ($(b*d)$-nodes storage).
In the worst case, the maximum number of nodes expanded will be $b^d$.

This strategy is **efficient** but **non-complete**, as it could present loops and infinite branches.

## 3. Limited depth search
A DFS variation with a fixed limited depth.
When you reach the maximum depth or a failure, it explores alternative paths (if they exist), then alternative paths at less than one unit of depth, and so forth (backtracking).
This **avoids** cases of **infinite branches**.

The implementation of LDS can be recursive or iterative:

### Recursive DLS
![[Pasted image 20260924174430.png|532]]
### Iterative DLS
```
1. C = 1
2. Apply depth-first with depth limit of C, if you find a solution stop.
3. Otherwise, increase C and go to step 2.
```

This technique avoids the problem of choosing the maximum depth limit by trying all possible depth limits.

It combines **BFS** and **DFS** by exploring a single branch at a time and reaching completeness.

The total number of expansion is:
$$(d+1)1+(d)b+(d-1)b^2+...+3b^{d-2}+2b^{d-1}+b^d$$
which is not considerably worse than the standard strategies.

![[Pasted image 20260924175015.png|509]]