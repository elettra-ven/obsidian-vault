Games with opponents can be defined as a [[Problem-Solving.canvas|search problems]] within a multi-agent environment.

## Game properties
- 2-player games (**MIN** and **MAX**, opposite objective functions)
- games with **perfect knowledge**
- players must play at their best

The development of a match can be interpreted as a **==tree==** in which the root is the starting position and the leaves are the final positions.

---
# 1. MIN-MAX Algorithm

This algorithm is designed to determine the optimal strategy for MAX, and to suggest its first best move.

MIN is assumed to play at its best.

>[!danger] **We are not interested in the path** but only in the next move!

Levels in this algorithm are labelled with $1$ (victory for MAX) and $-1$ (victory for MIN).
In case of parity the label is $0$.

![[img/Pasted image 20261021123930.png|442]]



```
Algorithm EVALUATE-NODE(n):
    Input:  A game tree node n
    Output: The evaluated value/label of node n

    1. EXPAND the entire game tree rooted at n
    2. FOR EACH leaf node L in the expanded tree:
           EVALUATE L as a winning state for MAX or MIN
           IF parity / draw THEN
               L.label = 0
           END IF

    3. WHILE node n is unlabeled DO:
           FIND an unlabeled node n' whose children are all labeled
           
           IF no such node n' exists THEN
               BREAK
           END IF

           IF n' is a MIN node THEN
               n'.label = MIN( child.label FOR EACH child OF n' )
           ELSE IF n' is a MAX node THEN
               n'.label = MAX( child.label FOR EACH child OF n' )
           END IF
       END WHILE

    4. RETURN n.label
```

The evaluation of a node $n$ is similar to the evaluation in DFS algorithms.
Let's see the MIN-MAX algorithm more in detail:

1. **Initialize:** Put node $n$ into $L$ (the list of open/unexpanded nodes).
2. **Check Completion:** Let $x$ be the first node in $L$. If $x = n$ and it has an assigned value, return that value.
3. **Update Parent:** If $x$ has an assigned value $V_x$, find its parent $p$ and provisional value $V_p$:
	- If $p$ is a **MIN** node, update $V_p = \min(V_p, V_x)$.
	-  If $p$ is a **MAX** node, update $V_p = \max(V_p, V_x)$[.
	-  Remove $x$ from $L$ and repeat from *step 2*.
4. **Leaf Node Evaluation:** If $x$ has no value and is a leaf, **or we decide not to expand it further** assign it **1, -1, or 0** (or the **evaluation function**, as we'll see below). 
   Put $x$ in $L$ to update its ancestors, then repeat from step 2.
5. **Non-Terminal Expansion:** If $x$ has no value and is not terminal:
	-  Assign $V_x = -\infty$ if $x$ is a **MAX** node.
	- Assign $V_x = +\infty$ if $x$ is a **MIN** node.
	- Add the children of $x$ to $L$ and repeat from step 2.


>[!question] **Complexity:** 
>$b^d$ *(where $b$ is the branching factor and $d$ is the depth)*

>[!success] MIN-MAX Properties
>- Complete
>- Optimal
>- $O(b^d)$
>  
> We need to **==🔴prune the tree==**!

## Min-Max Algorithm Revised

* **Infection & Complexity:** Developing the entire tree is very inefficient and grows exponentially. 
* **Node Count:** If $b$ is the branching factor and $d$ is the depth, the total number of nodes becomes $b^d$.
* **Evaluation Function:** An evaluation function is used to estimate the quality of a specific node:
  * $e(n) = -1$ if MIN wins.
  * $e(n) = +1$ if MAX wins.
  * $e(n) = 0$ if they have the same probability.
  * Intermediate values can also be used for $e(n)$.

Example of weighted sum of values:
$$Evals(s) = w_1f_1(s)+ w_2f_2(s) + ... + w_nf_n(s)$$

There must be a trade-off between search and evaluation functions.

### Pseudocode

```
function MINIMAX-DECISION(state) returns an action
    v <- MAX-VALUE(state)
    return the action in SUCCESSORS(state) with value v

function MAX-VALUE(state) returns a utility value
    if TERMINAL-TEST(state) then return UTILITY(state)
    v <- -∞
    for a, s in SUCCESSORS(state) do
        v <- MAX(v, MIN-VALUE(s))
    return v

function MIN-VALUE(state) returns a utility value
    if TERMINAL-TEST(state) then return UTILITY(state)
    v <- +∞
    for a, s in SUCCESSORS(state) do
        v <- MIN(v, MAX-VALUE(s))
    return v
```

## Pruning MIN-MAX

>[!warning] ***Alpha-beta* cuts**
>**Alpha-Beta Pruning** is an optimization technique for the MIN-MAX algorithm that skips branches which cannot possibly influence the final decision. 
>- It returns the exact same move/result as standard MIN-MAX while evaluating significantly fewer nodes. 
>#### Key Parameters 
>- **$\alpha$ (Alpha):** The best (highest) score that the **maximizing** player can guarantee so far. (Initially $-\infty$) 
>- **$\beta$ (Beta):** The best (lowest) score that the **minimizing** player can guarantee so far. (Initially $+\infty$) 
>- **Pruning Condition:** Whenever $\alpha \geq \beta$, the remaining children/branches can be safely pruned because the opponent will force a worse outcome anyway.

With Alpha-Beta cuts, we **generate a DFS tree**, left to right, and then we **propagate** the estimated value of MIN-MAX nodes.
