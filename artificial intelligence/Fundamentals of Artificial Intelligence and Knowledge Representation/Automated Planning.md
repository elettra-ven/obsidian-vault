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


