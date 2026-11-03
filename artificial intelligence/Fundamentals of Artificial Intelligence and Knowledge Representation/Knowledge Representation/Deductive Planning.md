>[!abstract] ## [[Automated Planning]]

**Deductive planning** uses logics for representing states, goals and actions and generates a plan as a **theorem proof**.

- ### Situation
	It is a world snapshot describing properties ("fluents") that hold in a given state $s$.
- ### Actions
	Define which fluents are true as a consequence of an action.

Situations and actions are described through [[First Order Logic|FOL]].

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

## Kowalski's formulation

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

>[!abstract] Why reason over time?
>- The environment **changes as time goes by**: categories, objects and properties give only a *static* perception.
>- We may need a **dynamic dimension**: execution of actions, events happening, how events (will) change the environment.
>- **Aims:** reason about the **past**, predict the **future** (planning).

>[!info] Propositional logic for dynamics (Wittgenstein, 1922)
>- The agent's beliefs are a **set of propositions** (only the *true* ones appear).
>- Different sets, put in order, represent the **evolution** of the world.
>- Sets and propositions are marked with a **numerical apex** to give the order ($KB^0, KB^1, \dots$).
>- States are countable, and **actions** make each state evolve into the next. This effect is described by **effect axioms**.

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
$\implies$ the effect axioms can't describe the **frame**.

If we have $m$ actions and $n$ propositions, the set of frame axioms will be $O(mn)$.
This creates a representational frame problem.

>[!done] Solution to the Frame Problem
>A solution would be the **frame axioms**:
>
>==🟢For each proposition that is not affected by the action, we will state that it is unaffected.==
>
>>[!example] Frame axiom for the archer
>>$$shoot^t \implies (hasArrow^t \leftrightarrow \neg hasArrow^{t+1})\quad\text{(effect axiom)}$$
>>$$shoot^t \implies (hasBow^t \leftrightarrow hasBow^{t+1})\quad\text{(frame axiom)}$$
>>$$KB^1 = \{hasBow^0, hasArrow^0, hasBow^1, \neg hasArrow^1\}$$
>
>>[!fail] Problems of frame axioms
>>- **Representational frame problem:** $m$ actions, $n$ propositions $\implies$ $O(mn)$ axioms.
>>- **Inferential frame problem:** reasoning $t$ steps ahead costs $O(n^t)$.
>>- The **locality principle** mitigates both problems, but doesn't eliminate them.
>
>>[!question] Do we really need to assert frame axioms?
>>We would like a "super axiom" saying *everything untouched stays the same*. This is **not expressible in FOL** (it needs higher-order logic). Event Calculus gets the same effect while staying first-order.

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

### *Example*:

>[!example] Blocks world in Situation Calculus
>FOL describes **states**, **clauses** describe **actions**.
>```
>on(b,a,s).   ontable(c,s).
>```
>Action `putOnTable(X)`:
>$$on(X,Y,S) \land clear(X,S) \rightarrow ontable(X,do(putOnTable(X),S)) \land clear(Y,do(putOnTable(X),S))$$
>
>**Plan construction = goal proof:**
>`:- ontable(b,S).` means *does a state S exist where ontable(b) is true?*
>
>$\implies$ YES with `S = do(putOnTable(b),s)`.

### Deductive planning (Green, 1969)

**Planning = theorem proving.** 

World and actions are described in FOL, and a plan is obtained as a by-product of a proof.
>[!quote] Running example (blocks world): 
>`move(X,Y,Z)` moves block X from Y to Z. 
>- Preconditions: `clear(X)`, `clear(Z)`, `on(X,Y)`, `diff(X,Z)`. 
>- Effects: `on(X,Z)` and `clear(Y)`.

**Situations are terms.** 
- `s0` is the initial situation, and `do(a,S)` is the situation reached by doing `a` in `S`. 
So `do(move(a,d,b), do(move(b,e,g), s0))` *is* the plan, read inside-out: 
1. first `move(b,e,g)`, 
2. then `move(a,d,b)`.

**The goal is existential.** `on(a,b,S)` means *does a situation $S$ exist where `on(a,b)` is true?*

The method is **resolution refutation with answer extraction**:
1. Negate the goal: `~on(a,b,S)`.
2. Resolve it with the effect axioms of the actions and the initial facts.
3. Each unification with an effect axiom **binds the state variable** to `do(action, S')`, so the plan is built **backwards** (goal → last action → its preconditions).
4. Reaching the empty clause proves the goal, and the **substitution for $S$ is the plan**.

>[!tip] `on(a,b,S)`
>*Does a state `S` exist in which `on(a,b)` is true?*

>[!fail] Where the frame problem bites
>Goal `on(a,b,S), on(b,g,S)` gives `S = do(move(a,d,b), do(move(b,e,g), s0))`.
>After `move(a,d,b)` the proof must still know that `on(b,g)` holds, but effect axioms say nothing about persistence. So Green needs one frame axiom per unchanged condition, for each action:
>$$on(U,V,S)\land diff(U,X)\rightarrow on(U,V,do(move(X,Y,Z),S))$$
>$$clear(U,S)\land diff(U,Z)\rightarrow clear(U,do(move(X,Y,Z),S))$$
## Kowalski's formulation in Prolog

Kowalski's formulation encodes situation calculus in Prolog with `holds / poss / pact`. The three predicates were introduced above, and here is how they read in practice.

Syntactically, terms and predicates in PROLOG have the same structure. `holds(on(a,b),S)` keeps the meaning of `on(a,b,S)`, but makes `on(a,b)` a **term**. This is called **reification**: the fluent becomes an object we can pass around and compare.

>[!tip] `pact(a,S)`
>*Are the preconditions of the action `a` true in `S`?*

>[!tip] `poss(S)`
>*Is `S` reachable?*

$$poss(s) \wedge pact(a,s) \rightarrow poss(do(a,s))$$

### One frame assertion per action

This is the advantage over Green: 
	instead of one frame axiom per (action, fluent) pair, we need **one frame assertion per action**. It says that everything not in the **delete list** persists:
$$holds(V,S)\land diff(V,clear(Z))\land diff(V,on(X,Y))\rightarrow holds(V,do(move(X,Y,Z),S))$$
Every fact different from `clear(Z)` and `on(X,Y)` remains true after `move`.

The price is that we still have to write the delete list of each action by hand.

### Example: `move(X,Y,Z)` in Prolog

```prolog
% Initial state
poss(s0).
holds(on(a,d),s0).   holds(on(b,e),s0).   holds(on(c,f),s0).
holds(clear(a),s0).  holds(clear(b),s0).  holds(clear(c),s0).  holds(clear(g),s0).

% Effects
holds(clear(Y), do(move(X,Y,Z),S)).
holds(on(X,Z),  do(move(X,Y,Z),S)).

% Preconditions
pact(move(X,Y,Z),S) :-
    holds(clear(X),S), holds(clear(Z),S), holds(on(X,Y),S), X\=Z.

% Frame
holds(V, do(move(X,Y,Z),S)) :-
    holds(V,S), V\=clear(Z), V\=on(X,Y).

% State reachability
poss(do(A,S)) :- poss(S), pact(A,S).

% Goal
:- poss(S), holds(on(b,g),S), holds(on(a,b),S).
% Yes: S = do(move(a,d,b), do(move(b,e,g), s0))
```

>[!example] Action `pickup(x,pos)` modelled in the Kowalski form
>```
># Initial State
>holds(ontable(X_N,pos_N), s0).        # for every N
>
># Effects
>holds(holding(X), do(pickup(X,pos),S)).
>
># Preconditions
>pact(pickup(X,pos), S) :-
>	holds(ontable(X,pos),S),
>	holds(clear(X),S),
>	holds(handempty,S).
>
># Frame
>holds(P, do(pickup(X,pos), S)) :-
>	holds(P,S),  P\=ontable(X,pos),
>	P\=clear(X), P\=handempty.
>```

## Event Calculus

Proposed by **Marek Sergot and Robert Kowalski (1986)**. It's a strategy that allows us to avoid frame problems.

It is based on **points of time** and **reifies both fluents and events** into terms: `HoldsAt(fluent, time)`. Fluents are properties whose truth value changes over time. It has the advantages of a second-order formulation, yet it stays first order. It allows linking several events to the same fluent, lets a change depend on other states, and allows reasoning on **meta-events** of change (*clip* and *de-clip*).

The formulation has 3 parts:
1. EC **ontology** (fixed)
2. **Domain-independent** axioms (fixed)
3. **Domain-dependent** axioms (application-specific)

>[!info] EC ontology
>| Predicate | Meaning |
>|---|---|
>| `HoldsAt(F,T)` | fluent F holds at time T |
>| `Happens(E,T)` | event E (an executed action) happened at T |
>| `Initiates(E,F,T)` | E causes F to hold at T (domain-dependent) |
>| `Terminates(E,F,T)` | E causes F to cease to hold at T (domain-dependent) |
>| `Clipped(T1,F,T)` | F was made false between T1 and T, with $T1<T$ (domain-independent) |
>| `Initially(F)` | F holds at time 0 |

### Domain-independent axioms

Two axioms say when a fluent is true:
$$HoldsAt(F,T) \Leftarrow Happens(E,T_1)\land Initiates(E,F,T_1)\land (T_1<T)\land\neg Clipped(T_1,F,T)$$
$$HoldsAt(F,T) \Leftarrow Initially(F)\land\neg Clipped(0,F,T)$$

One axiom defines clipping:
$$Clipped(T_1,F,T_2) \Leftarrow Happens(E,T)\land (T_1<T<T_2)\land Terminates(E,F,T)$$

>[!tip] Inertia
>A fluent stays true until some event terminates it, so **no frame axioms are needed**. This is how EC solves the frame problem.

### Domain-dependent axioms

A collection of `Initially(F)`, `Initiates(Ev,F,T)` and `Terminates(Ev,F,T)` clauses:
- `Initially(F)`: F holds at the beginning.
- `Initiates(Ev,F,T)`: the happening of `Ev` at time T makes F hold (it can carry many (pre)conditions).
- `Terminates(Ev,F,T)`: the happening of `Ev` at time T makes F stop holding.

>[!done] Pros
>- Allows the representation of a system and its **evolution** in FOL
>- Easy formalism
>- Declarative
>- Used for **monitoring** of systems, **simulation** of system evolution, and as a principled framework for representing evolution and reactiveness

>[!fail] Cons
>- Computationally costly
>- Not safe if fluents contain variables: it is easy to implement in Prolog, but the `¬Clipped` test relies on **negation as failure (NAF)**
>- **Deductive only:** the input is the domain-dependent axioms plus the happened events, and the output is the fluents true afterwards. If a **new event** is observed, a new query is needed and everything is **recomputed from scratch**

### Reactive Event Calculus

It overcomes the purely deductive nature of Sergot & Kowalski's formulation:
- New events can be **added dynamically**, so the result is **updated, not recomputed**.
- It allows events to arrive in the **wrong order**.
- It is more efficient, and can be implemented with both **backward and forward reasoning**.

## Allen's Logic

EC is based on the notion of **events**, i.e. the happening of things. 

Are events instantaneous, or do they have a duration? 
	There are pros and cons for both choices, but there is a consensus that a **duration-based** representation is richer. 
	A durative event is represented by a **start and an end point**, and an instantaneous event has **duration zero**.

Before that, how do we measure the passing of time? 
	Every time scale is an **arbitrary reference system**: 
- we need an **origin** (e.g. 1 January 1970) 
- and a **unit** (e.g. seconds).
	and points in time are measured as the distance from the origin.

**Allen** proposed to reason about **intervals** rather than points, since intervals are more natural categories for humans. An interval $i$ begins at a time point returned by `Begin(i)` and ends at the one returned by `End(i)`.

>[!info] Allen's relations
>Allen proposed 13 temporal relations: 6 relations, their 6 inverses, and `Equals`.
>
>| Relation | Definition | Inverse |
>|---|---|---|
>| `Meet(i,j)` | $End(i) = Begin(j)$ | met-by |
>| `Before(i,j)` | $End(i) < Begin(j)$ | `After(j,i)` |
>| `During(i,j)` | $Begin(j) < Begin(i) < End(i) < End(j)$ | contains |
>| `Overlap(i,j)` | $Begin(i) < Begin(j) < End(i) < End(j)$ | overlapped-by |
>| `Starts(i,j)` | $Begin(i) = Begin(j)$ | started-by |
>| `Finishes(i,j)` | $End(i) = End(j)$ | finished-by |
>| `Equals(i,j)` | $Begin(i) = Begin(j) \land End(i) = End(j)$ | (symmetric) |

In Allen's original definition `Starts` also requires $End(i)<End(j)$, and `Finishes` also requires $Begin(j)<Begin(i)$, so that the 13 relations are **mutually exclusive**.

## Comparison

| | Situation Calculus (Green) | Kowalski formulation | Event Calculus |
|---|---|---|---|
| Basis | situations, `do(A,S)` | `holds / poss / pact` | points in time, `HoldsAt / Happens` |
| Planning | resolution, state variable → plan | Prolog goal `poss(S), holds(...)` | deduction (what holds after the events) |
| Frame problem | $O(mn)$ frame axioms | **1 frame assertion per action** | solved via inertia (`Clipped`) |
| Weakness | too many axioms | delete list per action | NAF unsafe with variables, recompute on new events |