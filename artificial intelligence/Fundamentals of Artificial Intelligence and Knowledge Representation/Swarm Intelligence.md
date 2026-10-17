Swarm intelligence (SI) is an artificial intelligence technique based around the study of collective behaviour in decentralized, self-organized systems.

SI systems are typically made up of a population of simple agents interacting locally with one another and with their environment. 
Although there is normally no centralized control structure dictating how individual agents should behave, local interactions between such agents often lead to the emergence of global behaviour. 
Examples of systems like this can be found in nature, including ant colonies, bird flocking, animal herding, bacteria moulding and fish schooling.

>[!info] Components of Swarm Intelligence
>- **Multiple interactions between agents** 
>  (either simple or multi agents)
>- **Positive Feedback**
>  with reinforcement of common behaviours and amplification of random fluctuations and structure formation 
>- **Negative Feedback**
>  saturation, competition, exhaust resources

Agents in this SI algorithms often belong to different types, and execute different functions.
These algorithms are very effective for **Swarm Robotics**.

---
## 1. Ant Colony Optimization (ACO)

This is a **probabilistic** and **constructive** algorithm, that builds solution components in an incremental way.
The choice of path is not deterministic.


>[!1] Observation
From this phase, "ants" discover the following information:
>- Ants deposit pheromone trails while walking from the nest to the food and vice versa.
>- Ants tend to choose (more likely, it's not deterministic!!) the paths marked with higher pheromone concentrations.
>- Cooperative interaction leads to the emergent behaviour to find the shortest path.


The ants' steps are stochastics steps on an fully connected graph (**contruction graph**) $G = (C,L)$.
- Vertexes $C$ are solution components 
- Arcs $L$ are connections
- States are paths on $G$

Connections, solution components or both have the following associated information:
- Pheromone $\tau$.
- Heuristic value $\eta$.
  
![[img/Pasted image 20261015094502.png|460]]

```
InitializePheromoneValues() 

while "termination conditions" not met do:
	for all ants a in A do:
		sa <- ConstructSolution(pheromone, heuristicValue) 
	end for
	
	ApplyOnlineDelayedPheromoneUpdate()
	
end while
```

Memory is used to remind past paths.

>[!warning] Probabilistic choice
>The probabilistic choice depends on:
>- The pheromone trail $\tau_{ij}$
>- Heuristics $\eta_{ij} = \frac{1}{d_{ij}}$
>  $$p_{ij} = \begin{cases} \frac{[\tau_{ij}]^\alpha [\eta_{ij}]^\beta}{\sum_{k \text{ feasible}} [\tau_{ij}]^\alpha [\eta_{ij}]^\beta} & \text{if } j \text{ consistent} \\ 0 & \text{otherwise} \end{cases}$$

### Pheromone update
The pheromone is **updated** with the following rule:
$$\tau_{ij} \longleftarrow (1-\mathbf{p})\tau_{ij} + \sum_{k=1}^m \Delta^k\tau_{ij}$$
Where:
$\mathbf{p}$ is the **evaporation** coefficient and,
$$\Delta\tau_{ij} = \begin{cases} 1/L_k & \text{if ant } k \text{ used arc } (i,j) \\ 0 & \text{otherwise}\end{cases}$$

and $L_k$ is the length of the path followed by ant $k$.

### Pseudo-algorithm

```
while termination conditions not met do:
	ScheduleActivities 
	
		AntBasedSolutionConstruction() 
		
		PheromoneUpdate() 
		
		DaemonActions() {optional} 
	
	end ScheduleActivities 
end while
```

>[!info] `AntBasedSolutionConstruction()`
>Ants move by applying a stochastic local decision policy that uses values of pheromone and heuristic on graph components.
>
>While moving, ants take track of the partial solutions (paths) that have been built.

>[!info] `PheromoneUpdate()`
>Ants update the trail during the solution construction. 
>The trail can be updated *backwards* on components used on the basis of the quality of the overall solution.
>
>Evaporation is applied all the time.

>[!info] `DemonActions()`
Are “centralised” actions that cannot be executed by the single ants.
For example:
>-  local search procedure applied to each solution built.
>- collection of global information to decide whether to leave additional pheromone to guide search from a global perspective.

## 2. Honey Bee Colony

This algorithm has different agents with **different roles**. 
- **employed bees** that are associated with a specific nectar source
- **onlookers** that observing the employed bees chose a nectar source
- **scouts** that discover new food sources

Food positions represent solutions, while food quantity represents the fitness.

```
InitializationPhase() 
repeat 
	EmployedBeePhase() 
	OnlookerBeePhase() 
	ScoutBeePhase() 
	Sol=BestSolutionSoFar 
Until (Cycle=MaxCycleNum or MaxCPUtime)
```

>[!info] `InitializationPhase()`
>A set of **food sources positions** are randomly selected by the bees and their nectar amounts are determined.
>Each solution $X_m$ is composed of $n$ variables $X_{mi}$ for $i = 1..n$.
>Each variable is subject to a lower and upper bound.
>$$X_{mi} = lb_i + rand(0,1)*(ub_i-lb_i)$$

>[!info] `EmployedBeePhase()`
>The information about the nectar amount is **shared** between the members of the population.
>
>Every employed bee goes to the food source area visited by herself at the previous cycle since that food source exists in her **memory**, and then chooses a new food source by means of visual information in the **neighbourhood** of the present one (makes a local move). 
>
>**Fitness fuction**:
>$$ftn(X_m) = \begin{cases} \frac{1}{1+obj(X_m)} & \text{if} obj(X_m)\ge 0 \\ 1+|obj(X_m)| & \text{if} obj(X_m)< 0\end{cases}$$
>Where $obj$ is the *objective* function.

>[!info] `OnlookerBeePhase()`
>An onlooker bee chooses a food source depending on the probability value associated with that food source.
>$$p_m = \frac{ftn(X_m)}{\sum_{i=1}^{Npopul.}ftn(X_i)}$$
>

>[!info] `ScoutBeePhase()`
>Scouts chose nectar sources randomly.
>
>The employed bees that cannot improve the solution after a given number of attempts become scout and abandon the food source.

## 3. Particle Swarm Optimization
The research activity starts from the analysis of interaction mechanisms between individuals that compose the swarm.

Each individual entity in the "flock" has three driving **trends**:
1. **Following the neighbours**
2. **Staying in the flock**
3. **Avoiding collisions**

When the flock has a common objective (in this case food) it has two alternatives:
- Moving away from the group to reach for the food (**individualistic** choice)
- Staying in the group (**social** choice)

If more than one individual entity moves toward the food, other flock members do the same.
Gradually, the whole group changes direction towards **promising areas**, as the information propagates.

>[!note] PSO in optimization problems
>- **individuals** = tentative configurations that move and sample the solution $N$-dimensional space.
>- **social interaction**: each individual agent takes advantage from other searches moving toward promising regions (best solution globally found).

Search strategy can be found as a balance between **exploration** and **exploitation** (social behaviour which is the exploitation of other individual successful behaviour).

>[!warning] Neighbourhood and the **concept of proximity**
>Individuals are affected by the actions of other individuals that are closer to them. This behaviour generates **sub-groups**.
>
>Individuals can be part of more than one sub-groups, allowing for global spreading of information.

### Algorithm

> [!note] Particle Swarm Optimization
> 
> #### 1. Definitions & Notations
> - **$S$**: Number of particles in the population
> - **$x_i \in \mathbb{R}^n$**: Position of particle $i$ in the search space
> - **$v_i \in \mathbb{R}^n$**: Speed (velocity) of particle $i$
> - **$p_i$**: Best personal solution found by particle $i$
> - **$g$**: Best global solution found by the entire swarm
> - **$b_{lo}, b_{up}$**: Lower and upper boundaries of the search space
> 
> ---
> 
> #### 2. Initialization phase
> *For each particle $i = 1, \dots, S$:*
> - **Position:** 
>   $$x_i \sim \mathcal{U}(b_{lo}, b_{up})$$
> - **Personal Best:** 
>   $$p_i \leftarrow x_i$$
> - **Global Best Check:** If $f(p_i) < f(g)$, update $g \leftarrow p_i$
> - **Velocity:** 
>   $$v_i \sim \mathcal{U}(-|b_{up}-b_{lo}|, |b_{up}-b_{lo}|)$$
> 
> ---
> 
> #### 3. Main Loop
> *Repeat until a termination criterion is met (e.g., max iterations, target fitness):*
> - For each particle $i = 1, \dots, S$:
>   1. **Random factors:** 
>      $$r_p, r_g \sim \mathcal{U}(0,1)$$
>   2. **Velocity update:** 
>      $$v_i \leftarrow \omega v_i + \phi_p r_p (p_i - x_i) + \phi_g r_g (g - x_i)$$
>   3. **Position update:** 
>      $$x_i \leftarrow x_i + v_i$$
>   4. **Personal Best update:** If $f(x_i) < f(p_i)$, then $p_i \leftarrow x_i$
>   5. **Global Best update:** If $f(p_i) < f(g)$, then $g \leftarrow p_i$
> 
> ---
> 
> #### 4. Output & Key Parameters
> - **Output:** Return $g$ (the best found solution).
> - **Parameters ($\omega, \phi_p, \phi_g$):** Must be carefully selected, as they heavily impact the convergence, effectiveness, and efficiency of the algorithm.



