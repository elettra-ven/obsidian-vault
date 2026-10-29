Logic is the systematic study of the form of valid inference, and the most general laws of truth. A valid inference is one where there is a specific relation of logical support between the assumptions of the inference and its conclusion. In ordinary discourse, inferences may be signified by words such as therefore, thus, hence, ergo, and so on. 

There is no universal agreement as to the exact scope and subject matter of logic but it has traditionally included the classification of arguments, the systematic exposition of the 'logical form' common to all valid arguments, the study of proof and inference, including paradoxes and fallacies, and the study of syntax and semantics. 

Historically, logic has been studied in philosophy (since ancient times) and mathematics (since the mid-19th century), and recently logic has been studied in cognitive science (encompasses computer science, linguistics, philosophy and psychology).

## 1. Classical logic

Considers truth and inference. 

>[!question] if $X$ and $Y$ are true, can I deduce that also $W$ is true.

If concerns AI, Logic Languages, specification and verification on software.
## 2. Intuitionistic logic

It considers constructive proofs. 

>[!question] If I can construct a proof for $X$ and $Y$, can I construct a proof also for $W$?

## 3. Linear logic

It considers resources.

>[!question] If I have $X$ and $Y$, can I exchange them for $W$?

## 4. Epistemic logic

It considers knowledge and belief.

>[!question] If I believe that you know $X$ and $Y$, can I conclude that I believe $W$?
## 5. Temporal logic

It considers evolution in time.

>[!question] If $X$ and $Y$ will happen, can I conclude that $W$ could happen?

It handles specification and verification of software.

---
## Logic as a paradox free language

>[!note] Paradox
>Apparently correct reasoning, from apparently correct premises, which allow to derive an apparently contradictory conclusion.
>
>For example:
>- "*I'm a liar*"
>- I'm a liar iff what I'm saying is not true
>- I am liar iff “*I am a liar*” is not true

### 1. Paradoxes in Natural Language
==Natural language== allows paradoxes because of:
- NL **metalinguistic use** 
- Self-application of a meta linguistic concept

#### How to solve this problem

- Abandon Natural Language
- Use suitable language from mathematical logic

### 2. Paradoxes in mathematics

$\mathbf{Russel \ Paradox}:$
$$\text{Let} \ X = \{Y \mid Y \notin Y\}$$
$$\text{Then}\  X \in X \ \text{iff}\ X \notin X$$
#### How to solve this problem

For Russel's paradox in particular, we must define that $\{Y \mid Y \notin Y\}$ is **not a set**.
- Abandon the notion of "set" in a meta-linguistic way (for example, the collection of all sets is not a set).
- Sets can be constructed only selecting elements from sets.

$\implies$ $\{Y \in \text{class of all sets} \mid Y \notin Y\}$ is not a set, but a class, hence it does not contain itself.

### 3. Paradoxes in CS

Many programming languages allow higher order functions where meta-linguistics features exist and auto-application is possible.

---
# Thinking rationally

>[!example] Logic is **normative** rather than descriptive.
>Forms of logic are notations and rules of derivation for thoughts.

>[!info] Rational Behaviour
>"Doing the right thing"
>
>**The right thing**: 
>that which is expected to maximize goal achievement, given the available information.
>It doesn't necessarily involve thinking, but **thinking should be in the service of rational action**.

## Turing Test

We can assess if a machine is "acting humanly" if it passes the **Imitation Game**:
	A human can't tell if they're interacting with a machine or with another human being.

# Definitions of AI

1) Thinking humanly
2) Acting humanly
3) Thinking rationally
4) Acting rationally

>[!quote] [[Artificial Intelligence.canvas | Artificial Intelligence]]
>The ability of a computer to perform tasks commonly associated with intelligent beings.

It can take two main approaches:
- **Symbolic AI**
- **Sub-symbolic AI**


