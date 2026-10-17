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
>  
> ![[img/Pasted image 20261015095005.png]]

### Pheromone update
The pheromone is **updated** with the following rule:
$$\tau_{ij} \longleftarrow (1-\mathbf{p})\tau_{ij} + \sum_{k=1}^m \Delta^k\tau_{ij}$$
Where:
$\mathbf{p}$ is the **evaporation** coefficient and,
![[img/Pasted image 20261015095137.png|335]]

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

## 3. Particle Swarm Optimization
