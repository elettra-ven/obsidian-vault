Automated Planning is an important problem solving activity which consists in synthesizing a sequence of actions performed by an agent that leads from an initial state of the world to a given target state (**goal**).

Given:
- an initial state
- a set of actions
- a state to achieve (goal)
We must find:
- a **plan**

>[!success] Plan
>It's a partially or totally ordered set of actions needed to achieve the goal from the initial state.

>[!note] Automated **planner**
>Is an intelligent agent that operates is a certain **domain**, in which the given data is well **represented** (in [[First Order Logic]]).

We have to shape the **actions** according to the skills and possibilities of the automated planner.

## Action representation

Each action is identified by a name and declaratively modelled through **preconditions** is **postconditions**.

- **Preconditions**:
  Are the conditions which must be true to ensure that the action can be executed.
- **Postconditions**:
  Are the effects of the action of the world.

The ==solving process== for deciding the steps (actions) that solve a planning problem is:
- **Non decomposable**
- **Reversible**

>[!success] A planner is **complete** and **correct** if
>1. It always finds a plan when it exists
>2. The solution found leads from the initial state to the goal.

The ==execution== of the plan is:
- **Irreversible**
- **Non deterministic**

>[!info] Planning techniques
>- Deductive planning 
>- Planning as search 
>- Linear planning 
>- Nonlinear planning - Partial Order Planning (POP) 
>- Hierarchical planning 
>- Conditional planning
>- Graph-based planning

## Generative Planning

It produces the whole plan before execution.
It works on a **snapshot** of the current state.

>[!warning] Assumptions
>- **Atomic time**: 
>  actions are not interruptible
>- **Deterministic** effects
>- **Fully known initial state**
>- The plan execution is the **only cause of changing in the world**

Some of these assumptions (especially the third about "full knowledge") can be **relaxed**.

>[!tip] Planning can be seen as a **search activity**
>The nodes of the search tree are the **states** and the operators are the **actions**.
>
>==🟢The search stops when find a state that is a **superset of the goal** is reached.==
>
>This is called **Forward Search**.

>[!note] Forward Search
>The search starts from the initial state and proceeds when it finds a state that is a superset of the goal.
>
>**Cons**:
>- When there are a lot of actions to be executed, the search can be quite inefficient.
>- It's not driven by the goal.

>[!note] **Backward Search**
>This time, we start **from the goal** and we apply a *goal regression*.
>$$\mathbf{postconditions} \rightarrow \mathbf{preconditions}$$
>### Goal regression
>It's a mechanism that reduces a goal in **sub-goals** during search by applying rules.
>
>Given a goal $G$ and a rule $R$:
>$PRECOND: Plist$
>$DELETE: Dlist$ 
>$ADD: Alist$
>```
>Regr[G,R]: True if G in Alist
>Regr[G,R]: False if G in Dlist
>Regr[G,R]: G else
>```


---
# STRIPS (Stanford Research Institute Problem Solver)

It's based on the 3 lists action representation (PRECONDITIONS, DELETE, ADD).
Sometimes ADD and DELETE list are glued in an **EFFECT** list, that holds positive and negative literals/axioms.

It only acts following **syntactic rules**.

> [!abstract] Goal Stack Planning (Linear Planner)
> **Goal Stack Planning** is a classical automated planning technique using **backward search** (means-ends analysis) from the target goals to the initial state.
> 
> ### Key Characteristics & Assumptions
> - **Search Strategy**: Backward search (starts with target goals and works backward to find actions).
> - **Closed World Assumption (CWA)**: The initial state is fully known. Any predicate not explicitly stated as true in the current state is assumed to be false.
> - **Linearity**: Processes subgoals sequentially by maintaining a single stack.
> 
> ### Core Data Structures
> 1. **Goal Stack**: Tracks remaining goals, subgoals, compound goal expressions, and chosen operators/rules.
> 2. **Current State ($S$)**: Complete description of the facts currently true in the world.
>    It proceeds **forwards**.
> 
> ---
> 
> ### Algorithm
> 
> 3. **Initialization**:
>    - Push the main target goal (or conjunction of subgoals) onto the **Goal Stack**.
>    - Set the **Current State ($S$)** to the initial state.
> 
> 4. **Loop**: Repeat while `stack` is **not empty**:
> 
>    - **Case 1: Goal $a$ is already satisfied in state $S$** ($a\theta \subseteq S$)
>      - **Action**: Pop $a$ from stack and apply substitution $\theta$ to the rest of the stack.
>      
>    - **Case 2: Top item is a single unsatisfied goal $a$**
>      - **Action**: 
>        1. Select an action/rule $R$ whose effects satisfy $a$ (i.e., $a \in \text{Addlist}(R)$).
>        2. Pop $a$.
>        3. Push action $R$ onto the stack.
>        4. Push action $R$'s preconditions ($\text{Precond}(R)$) onto the stack.
> 
>    - **Case 3: Top item is a composite goal** ($a_1 \wedge a_2 \wedge \dots \wedge a_n$)
>      - **Action**: Push individual subgoals $a_1, a_2, \dots, a_n$ onto the stack.
>      - *Note*: The order of pushing subgoals is **non-deterministic**. Because goal operations can interfere with each other (==interacting goals==), satisfaction of compound goals must be re-verified.
> 
>    - **Case 4: Top item is an action/rule $R$**
>      - **Action**: Pop $R$ from the stack, execute it to update the current state $S$ ($\text{Addlist}$ added, $\text{Dellist}$ removed), and append $R$ to the plan output sequence.
>
>In order to execute an action we must always check if its preconditions are met. 
> 
> ---
> 
> > [!warning] Interacting Goals & Non-determinism
> > The order in which subgoals $a_1, \dots, a_n$ are pushed onto the stack is a critical **choice point**. 
> > Because achieving one subgoal may inadvertently undo a previously achieved subgoal (Sussman's Anomaly / interacting goals), compound goals must be re-checked after individual subgoals are met.
>  
>  

## Using STRIPS for Block Stacking

>[!warning] Problem
>***Given three blocks labelled A, B, and C, the objective is to stack Block A on Block B, and Block B on Block C.***

The initial state of the environments is:

```
OnTable(A)
OnTable(B)
OnTable(C)
```

>[!done] Goal
>$$On(A,B) \wedge On(B,C)$$
>```
>On(A,B)
>On(B,C)
>```

### Actions
#### `MoveBlock(X,Y)`
Moving block `X` on block `Y`.
- **Preconditions**:
	- `OnTable(X)`
	- `Clear(Y)`
- **Effects**:
	- `On(X,Y)`
	- `Clear(X)`
	- `¬OnTable(A)`
	- `¬Clear(B)`

We can achieve the following sub-goals:
1. `On(A,B)`
2. `On(B,C)`
## Sussman Anomaly

The Sussman Anomaly is a famous classical problem in AI planning that demonstrates the limitations of **Goal Stack Planning (Linear Planners)**.

When a linear planner (like Goal Stack Planning) processes a compound goal by breaking it down and solving subgoals sequentially, it tries to achieve one complete subtree/subgoal before moving to the next.

- If the planner tackles the subgoal `On(A,B)` first:
	Then it tries to achieve the second subgoal, but to do so it must pick up `B` and mode it to `C`, which **destroys** the already achieved goal `A` on top of `B`.
	This creates a **conflict**.

This proves that subgoals are often **not independent**; achieving one can inadvertently undo another.

---

# Non-linear Planning

>[!idea] Intuition
>Up to now we've seen planning approaches that can be seen as search strategies in a search tree (where nodes are states and edges are actions).
>
>Now we try to change perspective:
>Instead of considering the states as nodes, we consider them as **refinements of an initial empty plan**, towards a **complete** one.
>

1) Empty plan
	$\vdots$
2) **Refinement steps**
3) Goal (Complete plan)

The initial state is a sort of "fake action", with no preconditions, only effects (the opposite can be said for the goal state). 

>[!done] Least commitment planning
>*Why do I have to choose something if I don't have to?*
>
>It mean that we should never impose more restrictions than those that are strictly necessary.
>
>Suppose that we have a plan to put socks and shoes of the left/right foot.
>The **actions** are:
>- WearShoe(Foot) 
>  ```
>  PRECOND: socksOn (Foot) 
>  EFFECT: shoeOn (Foot)
>  ```
>- PutSocks(Foot) 
>  ```
>  PRECOND: ¬ socksOn (Foot) 
>  EFFECT: socksOn (Foot)
>  ```
>  
>  We only care that the preconditions are met, we don't care if we act first on the left or the right foot.
>  
>  **This choice does not require commitment.**

## Non-linear Planning Representation

- A set of actions
- A set of orderings between actions
- A set of **causal links**

At each step either the set of operators or the set of orderings or the set of causal links is increased until all goals are met.

>[!abstract] Partial Order Planning
>### Algorithm
>- `while` the plan is not **complete**:
>	1) select an action $SN$ that has a precondition not satisfied
>	2) select an action $S$ that hac $C$ among its effects
>	3) add the **order constraint** $s<SN$
>		- if $S$ is a new action add the constraint $Start<S<Stop$
>	4) add the **causal link** $<S,\ SN,\ C>$
>	5) solve any threat on causal links

>[!danger] Causal Link
>Is a triple that consists of **two operators**, $S_i$ and $S_j$ and a **subgoal** $c$, which should be **precondition** of $S_j$ and **effect** of $S_i$.
>$$S_i \stackrel{c}{\longrightarrow} S_j$$


## Purchasing Schedule

>[!info] Initial state
>```
>at(home)
>sells(HWS,drill)
>sells(sm,milk)
>sells(sm,banana)
>```

>[!done] Goal
>```
>at(home)
>have(drill)
>have(milk)
>have(banana)
>```

### Actions

```
Go (X, Y): 
	PRECOND: at (X) 
	EFFECT: at (Y), ¬ at (X) 
	
Buy (S, Y): 
	PRECOND: at (S), sells (S, Y) 
	EFFECT: have (Y)
```

![[img/Pasted image 20261029104144.png|513]]

### Conflicts

- We find a **contradiction** (a threat) to our **causal link** `go(home,hws), at(home)`:

![[img/Pasted image 20261029104354.png|506]]

>[!fail] In particular, it's threatened by `at(sm)` that follows `go(home,sm), at(home)`
>If the agent performs `go(home, hws)` it cannot be `at(home)` to perform `go(home, sm)` and viceversa.

>[!done] How to solve the conflict
>
>$$% Causal link
A \xrightarrow{\,p\,} B
C \text{ threatens } A \xrightarrow{\,p\,} B
>$$
>$$\neg p \in \mathrm{Effects}(C)
\;\wedge\;
\text{ordering constraints allow } A < C < B$$
>We have 2 options:
>1) **Demotion**
>	- order the threatening step _after_ B (B < C).
>2) **Promoting**
>	- order the threatening step _before_ A (C < A).
>3) **Backtrack:** 
> 	- if neither ordering is consistent, undo an earlier choice, such as how a precondition was satisfied, or add a new step that re-establishes p.
> 	  
> **Why ordering fails.**
>- _Promotion:_ a step can’t be placed before Start.
>- _Demotion:_ each step is itself the consumer of `at(home)`, so putting one after the other just moves the threat around. 
>  If `go(home, hws) < go(home, sm), at(home)` is already gone when `go(home, sm)` runs, and vice versa.
>  
>  **The only fix is to backtrack `at(X)`**
>  

![[img/Pasted image 20261029105935.png]]

