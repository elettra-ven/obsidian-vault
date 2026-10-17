Unlike the algorithms that we've seen before, **local search algorithms** start from an **initial solution** and iteratively try to improve it through **local moves**.
These algorithms are used when the path to reach the goal is **irrelevant**, and all the information necessary for understanding the goal (understanding $\text{state}=\text{goal}$) are already given in the state description $\implies$ ==the starting point of the problem is already a **complete configuration**==.

>[!info] **Local moves**
>They must define a neighbourhood in which action can be taken.
>$$N : S \rightarrow 2^S$$
>Given a set of states $S$, the function assigns to every $s \in S$ a set of neighbours $N(s) \subseteq S$, where $N(s)$ is called the "neighbourhood" of $s$.

Local search can be seen as **search process over a graph** of neighbourhood.
![[img/Pasted image 20261014124524.png|472]]
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
They propose strategies to avoid ending in local optimums.
They are based methods like:
- the sporadic acceptance of **non-improving** solutions, within the algorithm.
- the changing of the neighbourhood or of the cost function, during the search.
- the use of high-level search strategies.

>[!info] Intensification
>Concentrating on the single neighbourhood of a given solution.

>[!info] Diversification
>Escaping from the single neighbourhood of a given solution.

Local search must alternate between phases of Intensification and Diversification.

---
# Algorithms:
## 1. Simulated Annealing
The probability of accepting solutions of worse quality than the current solution **decreases** during the search.
$\implies$ at the beginning of the search, diversification moves are the most probable.
Usually:
$$p(\text{accept down-hill move s}') = \frac{exp(−(f(sʹ)−f(s)))}{T}$$

![[img/Pasted image 20261014125717.png|449]]

The **temperature** $T$ can be update in different ways, such as logarithmic (very slow but always convergent), geometric and non-monotonic ... 

## 2. Tabu Search
It introduces the notion of **memory** through a **Tabu list**.
This list keeps track of recent moves or recently visited solutions, that become **forbidden states**. This reduces the risk of cycles and local minimums.

![[img/Pasted image 20261014130231.png|292]]

more in detail...

![[img/Pasted image 20261014130439.png|481]]

Storing a list of solutions is sometimes **inefficient**, therefore moves are stored instead.

The **Aspiration Conditions** by accepting a forbidden move toward a solution better than the current one.

## 3. Iterated Local Search
It uses two type of steps:
- **Subsidiary local search steps** for reaching local optima as efficiently as possible (**intensification**)
- **Perturbation steps** for effectively escaping from local optima (**diversification**)

![[img/Pasted image 20261014130704.png|372]]

$s*$ is the result of an hill climbing.
The solution is then perturbated until the algorithm is accepted.

It keeps an history, just like the Tabu Search.

>[!abstract] Considerations:
>High-level search strategies have to be applied to effectively explore the search space (intensification/diversification).

---

# Population based metaheuristics

They are based on the evolution of a set of points in the search space, by learning correlations between "good" solution components.

## 1. Genetic Algorithms
Genetic algorithms are inspired by evolution. 
Three key components:

- **Adaptation**: organisms are suited to their habitats  
- **Inheritance**: offspring resemble their parents 
- **Natural** **selection**: new, adapted types of organisms emerge and those that fail to change adequately are subject to extinction

The *fitness* function finds the individuals that have a high chance of having numerous "offspring".

>[!warning] GAs are not meant to simulate the biological evolutionary processes, but rather aimed at exploiting these key concepts for problem solving.

![[img/Pasted image 20261014131937.png|440]]

These algorithms **rely heavily** on **probability**. They would work if implemented deterministically.

### Basic Evolutionary Cycle
![[img/Pasted image 20261014132043.png|328]]

- **Recombination**: 
  combines the genetic material of the parents. It's also called **crossover** (cross-combination of two chromosomes) and it's tied to **linear combination**:
  $$z = \lambda_1x + \lambda_2y, \text{ with } \lambda_1, \lambda_2 \text{ such that } a≤z ≤b.$$
  Crossover combines good parts from good solutions (but it might achieve the opposite effect).
- **Mutation**: 
  introduce random variability (diversity) in the genotypes through **perturbations**. 
- **Selection**: 
  acts in the choice of parents whose genetic material is then reproduced with variations.
  It drives the population towards high fitness.
- **Replacement/insertion**: 
  defines the new population from the new and the old one.

```
Initialize Population 
Evaluate Population 

while Termination conditions not met do 
	while New population not completed do 
	
		Select two parents for mating 
		Apply crossover 
		Apply mutation to each new individual 
		
	end while 
	
Population ← New population 
Evaluate Population 

end while
```

| **Pros**                     | **Cons**                     |
| ---------------------------- | ---------------------------- |
| Extremely simple             | Coding is crucial            |
| General purpose              | Too simple genetic operators |
| Tractable theoretical models |                              |
