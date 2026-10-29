>[!abstract] ## [[Automated Planning]]

**Deductive planning** uses logics for representing states, goals and actions and generates a plan as a **theorem proof**.

- ### Situation
	It is a world snapshot describing properties ("fluents") that hold in a given state $s$.
- ### Actions
	Define which fluents are true as a consequence of an action.

Situations and actions are described trough [[First Order Logic|FOL]].

>[!tip] Situation Calculus
>It's used to build a planning based on logic resolutions.
>We must find proofs of a formula containing a **state variable**. At the end of the proof the state variable will be instantiated to the **plan** to reach the goal.
>$$\mathbf{deduction} \longrightarrow \mathbf{goal \ proof}$$
>>[!done] High expressivity, can be used to describe complex problems
>
>>[!fail] Frame problem
>>It's a **knowledge representation problem**.
>>All the fluents must be explicitly listed after every state transition (even if they haven't changed).
>>
>>In complex domain the number of these axioms grows enormously.
>

## Kowalsky'sj formulation

Kowalsky's formulation provides a **logical framework** for reasoning about actions, states, and their changes over time using predicates within situation calculus.

The formulation relies on three primary predicates to model dynamic systems:

- **`holds(rel, s)`**: Describes all **relations** (`rel`) that are true in a given state ($s$), or conversely, made true by the execution of an action.
    
- **`poss(s)`**: Indicates whether a specific state ($s$) is possible, meaning it is reachable within the system.
    
- **`pact(a, s)`**: Indicates that it is possible to execute an action ($a$) in a given state ($s$). 
  This essentially evaluates whether the **preconditions** of action $a$ are satisfied in $s$.

>[!warning] State Transition Rule
>To model how states evolve when actions are performed, the framework uses the function `do(A, S)` to represent the resulting state after executing action $A$ in state $S$.
>
>The foundational transition rule dictates that if a current state is possible and the preconditions for an action are met, the resulting state is also possible:
>
>$$\text{poss}(S) \land \text{pact}(A, S) \implies \text{poss}(\text{do}(A, S))$$
>
>This rule ensures that actions only generate valid, reachable future states when executed from a valid present state under appropriate conditions.

