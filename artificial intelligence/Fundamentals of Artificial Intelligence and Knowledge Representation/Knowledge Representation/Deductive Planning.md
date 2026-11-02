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

---
# Time Deductive Planning

>[!Example] 
>A child has a bow and an arrow. She can shoot the arrow, throw the bow, but she can also run, hide, and crouch.
>
>0) Knowledge at state 0:
>$$KB^0 = \{hasBow^0, hasArrow^0\}$$
>
>- ==The child shoots the arrow.==
>  
>1) Knowledge at state 1:
>The agent **observes** the following:
>$$KB^1 = \{hasBow^0, hasArrow^0, hasBow^1, \neg hasArrow^1\}$$

We are interested to focus on the dynamic, or rather how the world evolves from $KB^0$ to $KB^1$.

>[!warning] What does it mean to "shoot an arrow"?
>$$shoot^t \implies (hasArrow^t \leftrightarrow \neg hasArrow^{(t+1)})$$
>
>$$KB^0 = \{hasBow^0, hasArrow^0\}$$
>$$KB^1 = \{hasBow^0, hasArrow^0, \neg hasArrow^1\}$$
>
>>[!danger] Which is different from $KB^1 = \{hasBow^0, hasArrow^0, hasBow^1, \neg hasArrow^1\}$
>>- *Does the child still have the bow after the shoot?*
>>
>>This is called the **Frame Problem**.

## The Frame Problem

The **effect axioms** fail to state what remains unchanged as the result of an action.
The background (**frame**) remains unchanged, while the "foreground" is subjected to the effects.
$\implies$ the effect axioms can't descrive the **frame**.

If we have $m$ actions and $n$ propositions, the set of frame axioms will be $O(mn)$.
This creates a representational frame problem.

>[!done] Solution to the Frame Problem
>A solution would be the **frame axioms**:
>
>==🟢For each proposition that is not affected by the action, we will state that it is unaffected.==

## Situation Calculus

- **Situation**
  A world snapshot $s$, that describes some fluents.
- **Actions**
  Define which fluents are true as a consequence of an action.

Situation Calculus can be used to build a **planning** based on **logic resolution**.

>[!done] Pros
>- Highly expressive
>- Can describe complex problems

>[!fail] Cons
>- Frame problem

>[!tip] `on(a,b,S)`
>*Does a state `S` exists in which `on(a,b)` is true?*


## Event Calculus

It's a strategy that allows us to avoid frame problems.

### Kowalski's Formulation

- Event calculus is based on the following three **predicates**:
	1) `holds`
	2) `pact`
	3) `poss`

>[!tip] `holds(on(a,b),S)`
>We have a "meta-predicate" `HoldsAt(fluent, situation/action)`, that reifies both fluents and events into terms.

Syntactically, terms and predicates in PROLOG have the same structure.
The function `HoldsAt(on(a,b),S)` maintains the meaning of `on(a,b,S)`, making the argument `on(a,b)` a **term**.

>[!tip] `pact(a,S)`
>*Are the preconditions of the actions `a` true in `S`?*

>[!tip] `poss(S)`
>*Is `S` reachable?*

$$poss(s) \wedge pact(a,s) \rightarrow poss(do(a,s))$$

>[!example] Action `pickup(x,pos)` modelled in the Kowalski form
>```
># Initial State
>holds(ontable(X_N,pos_N), s0)        # for every N
>
># Effects
>holds(holding(x), do(pickup(x,pos),s))
>
># Preconditions
>pact(pickup(X,pos), S) :-
>	holds(ontable(X,pos),S),
>	holds(clear(X),S),
>	holds(handempty,S)
>
># Frame
>holds(P,do(pickup(X,pos)), S) :-     # where P is a property
>	holds(P,S),      P\=ontable(X,pos),
>	P\=clear(X),     P\=handempty
>```

>[!done] Pros
>- Allows the representation of a system and its **evolution** in FOL
>- Easy formalism
>- Declarative

>[!fail] Cons
>- Computationally costly
>- Not safe if fluents contain variables

### Allen's Logic
...
