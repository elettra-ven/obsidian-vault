Unlike the algorithms that we've seen before, **local search algorithms** start from an **initial solution** and iteratively try to improve it through **local moves**.
These algorithms are used when the path to reach the goal is **irrelevant**, and all the information necessary for understanding the goal (understanding $\text{state}=\text{goal}$) are already given in the state description $\implies$ ==the starting point of the problem is already a **complete configuration**==.

>[!info] **Local moves**
>They must define a neighbourhood in which action can be taken.
>$$N : S \rightarrow 2^S$$
>Given a set of states $S$, the function assigns to every $s \in S$ a set of neighbours $N(s) \subseteq S$, where $N(s)$ is called the "neighbourhood" of $s$.

# TSP
Given an undirected graph, with n nodes and each arc associated with a positive value, find the Hamiltonian tour with the minimum total cost.

>[!info] **K-exchange** (K-cycle)
>We can "remove" and exchange an arbitrary number of arcs within a path/Hamiltonian tour (this algorithm is called *k-opt*).
>
>We procede to remove **k** edges from the current tour and we rearrange other **k** connections so to form a new valid tour.

### Iterative Improvement (**Hill Climbing**)
Very basic local search algorithm 
1. A move is only performed if the solution it produces is better than the current solution (also called **hill-climbing**).
2. The algorithm stops as soon as it finds a local minimum.

	This approach has several variants: best, first, stochastic first, etc.

$$\begin{split} a \longleftarrow & \text{GenerateInitialSolution()} \\
& \mathbf{repeat}: \\
& \\
& s \longleftarrow \text{BestOf(s, \ N(s))}\\
& \\
& \mathbf{until} \text{ no improvement is possible}
\end{split}$$

>[!note] It's not effective in exploring the search space (e.g., it stops at the first **local optimum**/minimum encountered).
>- "Local" withing the single neighbourhood.
>
>Hill Climbing algorithm is "*like climbing Everest in thick fog with amnesia*".

## Meta Heuristics 
