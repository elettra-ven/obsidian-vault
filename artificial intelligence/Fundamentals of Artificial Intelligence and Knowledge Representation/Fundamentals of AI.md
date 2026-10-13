**Recommended Textbook**: Russel&Norvig *Artificial Intelligence: A modern approach*.
**Professor**: michela.milano@unibo.it

---

>[!NOTE] Intelligence
>It can be described as the capacity of logic, understanding, self-awareness, learning, creativity, problem-solving, …
>Some feature of human intelligence can be simulated by machines.

To be deemed as "intelligent", the machine must pass the **Turing Test** and have the following abilities:
- NL Processing
- Knowledge representation
- Automatic reasoning
- [[Machine Learning]]

### Weak AI vs Strong AI
Weak AI act *as if* they were intelligent, while Strong AI are deemed intelligent and conscious.

### General AI vs Narrow AI
General AI copes with generalised tasks much like a human, while Narrow AI refer to AI who can handle just particular tasks, but with enhanced and "super-human" performances.

## AI approaches

- **Top-down/symbolic** AI
	- symbolic representation of knowledge
	- logics, ontologies, rule-based systems, …
	- human-understandable models
	It can perform deductive and inductive reasoning, hypotheticals, analogies and can constraint reasoning and optimization.
	These models are reliable and can be trusted (it can give guarantees of success).
- **Bottom-up/connectionist** AI
	- neural networks
	- encoded representation of knowledge
	- concepts learned by examples
	- not understandable by humans

## [[PROLOG]] (PROgramming in LOGic)
Declarative programming language.
A **PROLOG Program** is a set of clauses representing **facts**, **rules** and **goals**:

![[img/Pasted image 20260916135423.png]]
![[img/Pasted image 20260916135444.png|288]]

The programmer provides the knowledge about the goal task. 
The inference engine takes the knowledge provided and finds the correct solution to the task.
The knowledge is **independent** from its use, in order to maximalise flexibility, determines the correctness and the efficiency of the system.

### Declarative definition of **sum**
Let `s(X)` be the successor of `X`.

**FACT**: 
```
sum(0,X,X).
```
$$x+0 = x$$
**RULE**: 
```
sum(s(X),Y,s(Z)):- sum(X,Y,Z).
```
$$x+y=z \implies (x+1)+y=(z+1)$$

*For example:*
#### Deduction

```
:- sum(s(0),s(0),Y). 
:- sum(s(0),Y,s(s(s(0)))). 
:- sum(X,Y,s(s(s(0)))). 
:- sum(X,Y,Z). 
:- sum(X,Y,s(s(s(0)))), sum(X,s(0),Y).
```

translate to:

$$ 1+2 = Y $$
$$ 1+Y = 3 $$
$$ X+Y = 3 $$
$$ X+Y = Z $$
$$X+Y = 3 \space, \space X+1 = Y$$
from the last rule, we can deduct that:
$$X=1$$
$$Y=2$$

### Induction
Induction infers a rule that can return true or false, depending on the existing information.
![[img/Pasted image 20260916142410.png|455]]
### Abduction
Produces an hypothesis on the basis of previous knowledge and observation (for example using integrity constraints to control hypothesis).
![[img/Pasted image 20260916142526.png|499]]

---
# Automated Planning
Planning is a **symbolic model** that synthesise a sequence of actions performed by an agent.
Given a **goal** and an **initial state**, planning allows to generate a chain of actions that point to the target state.

>[!info] Plan
>A partially or totally ordered set of actions needed to achieve the goal from the initial state.

An **automated planner** operates in a domain described by:
1. a representation of the initial state
2. a representation of the goal
3. a description of the **executable actions**/operators.

>[!info] Operators
>Operators are defined by two lists:
>1. **Preconditions** that need to be true for the action to be executed.
>2. **Changes/consequences** to the actions.


A planner must be **correct** and **complete**.
- **Correct**:
	The plan that is produced reached the goal.
- **Complete**:
	If a plan exists, then the planner is able to find it.

## Swarm intelligence
Distributed (no central coordination) intelligence inspired from nature, similar to genetic algorithms.
The agents in the swarm cooperate and self-organise until an intelligence algorithm emerges. This system is very adaptive and doesn't need supervision.

## Reinforcement learning
RL can also be used for planning tasks.
![[img/Pasted image 20260923124550.png|361]]

Given an $input$ the learner suggests a response (an action) that is actually **performed** on the system ("**on-line planner**").
Depending on whether the system ends up in a negative state or in a positive state, the learner is either **punished** or **rewarded**.

>[!reminder] Only use RL if the system can afford errors.

