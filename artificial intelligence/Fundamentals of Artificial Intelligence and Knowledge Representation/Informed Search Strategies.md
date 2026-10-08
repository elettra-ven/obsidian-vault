These strategies make use to **heuristics domain knowledge** (==**evaluation functions**==) to try to **predict** the cost of a certain path/node expansion, instead of exploring the whole decisional world.

This is pretty useful in certain complex problems that would not make the $b^d$ cost acceptable.

>[!info] Heuristics/evaluation functions
>They give a computational estimate of the effort to reach the goal.
>
>The more complex the function is the more accurate is the heuristics. However this implies a greater cost of calculation *per node* (for a smaller set of nodes if the heuristics are good enough).
>
>A trade-off is needed between:
>- the time it takes to solve the problem (**baseline**)
>- time spent in reasoning on top of it (**meta-level**)


## 1. **Best** First Search
It computes a number that represents the **immediate desirability** of the node expansion.

The "**best-first**" means that the chosen node is the one considered as the most desirable.
In the successors queue the order of the nodes is by desirability.

It's **not** always **optimal**. There are cases in which the heuristics can make an over-estimation while choosing the path of node-explosions.
Looking only forward and never backwards can be a problem i certain situations.
It also can be **incomplete** (same problems as the **depth-first search**).

In the worst case, if the depth is $d$ and the branching factor $b$ the maximum number of expanded nodes will be $b^d$.
### Greedy Search

>[!info] Greedy Algorithm
>1. Let $L$ be a list of the initial nodes of the problem, ranked according to their distance from the goal (ascending order);
>2. If $L$ is empty $\implies$ **fail**;
>   Otherwise let $n$ be the first node of $L$.
>3. If $n$ is the goal return the solution;
>4. Otherwise remove $n$ from $L$ and add to $L$ all the **children of $n$**.
>   Then order the entire list $L$ based on an estimate of the relative distance from the goal (**desirability**).
>   **Return to step 2.**


### A* Search
It's the most important search algorithm in AI.

>[!important] Instead of only considering the distance to the goal, also consider the "**cost**" in reaching the node $n$ from the root.
>We expand the nodes for increasing values of the function $f(n)$:
>$$f(n) = g(n) + h'(n)$$
>Where:
>- $g(n)$ is the real depth of the node.
>- $h'(n)$ is the estimated distance from the goal (heuristic).
>
>(*greedy algorithms and "hill climbing" only use* $h'(n)$,* while uniform searches only use* $g(n)$)

The algorithm **does not guarantee to find the optimal path**, as it depends on the heuristic function.

If we always have $h'(n) \le h(n)$ (where $h(n)$ is the true distance between the current node and the goal), we can say that the heuristic function is **optimistic** and therefore **feasible**.

>[!warning] Theorem
>If $h'(n) \le h(n)$ is true for each node, then the A* algorithm **always finds the optimal path** to the goal.

>[!info] Detail
>If $h' = 0$ we always obtain a feasible heuristic function, which is equal to the **breadth-first search** algorithm.

#### Optimality proof
Suppose you have created a sub-optimal goal $G_2$ and to have it in the queue. 
Let $n$ be an unexpanded node in the queue such that $n$ is on the shortest path to the optimal goal $G$.

- as $h(G_2)=0$:
$$f(G_2) = g(G_2)$$
- as $G_2$ is **sub-optimal**:
$$g(G_2) > g(G)$$
- as $h(G)=0$:
$$f(G) = g(G)$$
$$\implies f(G_2) > g(G_2)$$
- as $h'$ is feasible permissible:
$$h'(n) \le h(n)$$
$$\implies g(n)+h'(n) \le g(n)+h(n) = f(G)$$
	it means that $n$ is on the path to $G$.
$$f(n) = f(G)$$
then $f (G_2)> f(n)$, and A* will never select $G_2$ for expansion.
It will instead look for optimality, so for $G$.

>[!tip] Between two heuristics that are both optimistic (lower bound) always choose the greater (closer to the actual goal).

## How to "invent" heuristics?
Heuristics are defined by **problem** **relaxation** (often the cost of an exact solution of a relaxed problem is a good heuristic for the original problem).

### `GRAPH-SEARCH`
![[img/Pasted image 20261008093101.png]]

>[!important] **A\* for graphs**
>We hold two lists:
>- **closed nodes:** expanded nodes are removed from the list to avoid further examination;
>- **open nodes:** nodes that still to be examined.
>
>A* searching in a graph instead of a tree (A graph can become a tree with repeated nodes).
>
>1. Let $L_a$ be the open list of initial nodes of the problem.
>2. Let $n$ be the node for which $g (n) + h '(n)$ is **minimal**. If the list is empty, fail.
>3. If $n$ is the goal then stop and return the path to reach it.
>4. Otherwise remove n from $L_a$, enter it in the list of closed nodes $L_c$ and add to $L_a$ all the children of $n$, labelling them with the cost from the starting node to $n$.
>5. If a child node is already in $L_a$, do not add it, but update is label in case its cost (root to node) is smaller than the one it had.
>6. If a child node is already in $L_c$, do not add it to $L_a$, but if its cost is better, update its cost and the one of its children and descendant.
>7. **Return to step 2.**


### Consistent/**monotone** heuristics

>[!info]
>A heuristic is **consistent** if for each node $n$, any successor $n'$ of $n$ generated by each action $a$ we can say:
>- $h(n) = 0$ if the corresponding status is the **goal**.
>- $h(n) \ge c(n,a,n') + h(n')$ otherwise.

![[img/Pasted image 20261008092601.png|156]]
If $h$ is consistent we have that:

$$\begin{equation}
\begin{split}
f(n') & = G(n') + h(n') \\
 & = G(n)+c(n,a,n')+h(n') \\
 & \ge g(n)+h(n) \\
 & f(n)
\end{split}
\end{equation}$$

>[!important] Theorem
>If $h(n)$ is consistent then **A\* using**  `GRAPH-SEARCH` **is optimal**.

