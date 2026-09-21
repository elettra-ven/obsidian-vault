## Types of uncertainty

* **Partial observability**: 
	relevant information missing, delayed, noisy... 
* **Uncertain outcomes**: 
	the same action may lead to different results.
* **Dynamic environments**: 
	world may change while reasoning.

Agents need to act under uncertainty, so we should provide them techniques and methods to manage these situations.
For example, we can build AI models without handling *noise*.

![[Pasted image 20260921094318.png|505]]

>[!tip] An intelligent agent must often choose an action without knowing its outcome with certainty. 
>Probability represents beliefs about uncertain outcomes; 
>utility represents preferences over their consequences.

### Nonmonotonic reasoning
It is a formal logic where the conclusion doesn't always "grow" with the addition of new information. 

>[!info] "All birds are black". 
>But when i see a white bird I refrain from my previous knowledge.

Non-monotonicity indicates that learning a new piece of knowledge does in fact **reduce** the set of what is known.
This type of reasoning starts from the assumption that all conditions are in favour of the successful event, until contradicted by evidence.

### Rule-based systems with heuristics confidence weights
Heuristics weights are empirically motivated by **causal and diagnostic reasoning** real world experiences that the model observes.

---
### Probability

>[!important] Probability provides a formal language to describe possible worlds, events, random variables, and an agent’s degree of belief in uncertain propositions

While **logical assertions** distinguish worlds that are possible from worlds that are impossible, **probabilistic assertions** assign a value (plausibility) to each possible world.

>[!info] Probability $vs$ Fuzzy logic
>Probability represent the uncertainty about a fact (incomplete knowledge), while fuzzy logic measures the vagueness of a concept (used when the problem has no sharp boundaries).

Probability has different interpretations:
* **Frequentist**:
	Probability is the **long-run** relative frequency of an event in repeated, comparable trials.
	
	Example: 
		“In similar journeys, 6% arrived at the airport on time.”
	
* **Bayesian**:
	Probability represents an agent’s **degree of belief**, given the evidence currently available.
	
	Example:
		“Given what I know now, I assign probability 0.06 to arriving at the airport on time."
	$P(\text{AtAirportOnTime } | A_{25}, \text{no reported accidents}) = 0.06$
	The value 0.06 describes the agent’s current degree of belief about this trip. 
	Different agents may assign different probabilities if they have different evidence or background knowledge.
	$\implies P(\text{AtAirportOnTime } | A_{25}, \text{no reported accidents}, 5 \text{ a.m.}) = 0.06$
	A new evidence has changed the agent’s belief.

Once we know the probabilities of each agent, in order to decide which agent to follow, we must look at the preferences of the problem ("**Utility Theory**").

>[!definition] $\Omega$ **is the sample space**: the set of all possible worlds (logical assertion).
>Each $\omega \in \Omega$ is a **sample point** or possible world/atomic event. 
>An event is any subset $A \subseteq \Omega$.

The sample points are exhaustive (one of them must occur) and mutually exclusive.

>[!definition] Probability Space
>A probability space is a triple $(\Omega, F, P)$.
>Where:
>- $\Omega$ is the sample space
>- $F$ is a $\sigma$-algebra of events, with $F \subseteq 2^{\Omega}$. It specifies which subsets of $\Omega$ are events to which we can assign a probability.
>- $P:F\rightarrow [0,1]$ is a probability measure, such that $P(\Omega)=1$
>$$P(\bigcup_{i=1}^{\infty} A_i) = \sum_{i=1}^{\infty} P(A_i)$$

To each $A_i \in A$, is assigned a probability model $P(A) = \sum_{\omega \in A} P(\omega)$ for each possible world $\omega \in \Omega$.

>[!definition] Random Variable
A random variable is a function 
$$X : \Omega \rightarrow \chi$$ 
which associates each possible world with a value in its range $\chi$ (e.g., the reals or Booleans).

The probability measure $P$ induces a probability distribution for every random variable $X$.
The probability distribution of $X$ assigns a probability to every variable $x_i \in \chi$:
$$P_x(x_i) = P(X=x_i)$$

### Propositions
A proposition denotes the event consisting of all possible worlds in which it is true.

Let *a* be a proposition. Its probability is the  probability of each atomic event where *a* is true.
Therefore, a proposition is a disjunction of mutually exclusive atomic events:
$$a \vee b ≡ (a \wedge b) \vee (a \wedge \neg b) \vee (\neg a \wedge b) $$$$P(a \vee b) = P(a \wedge b) + P(a \wedge \neg b) + P(\neg a \wedge b)$$

#### Syntax for propositions
- **Propositional** or Boolean random variables 
	e.g., **Cavity** (do I have a cavity?) 
	"**Cavity = true**" is a proposition, also written *cavity* 
- **Discrete** random variables (finite or infinite) 
	e.g., Weather is one of $\langle$sunny, rain, cloudy, snow$\rangle$ 
	"**Weather = rain**" is a proposition 
	Values must be exhaustive and mutually exclusive 
- **Continuous** random variables (bounded or unbounded) 
	e.g., **Temp** = 21.6; **Temp** < 22.0 
* **Arbitrary** Boolean combinations of basic propositions

### Probability densities
A probability density function describes how probability is locally distributed over the possible values of the variable.
The number that would be assigned to a single "point" is now assigned to a "region" (density).

### Distributions:
- #### Uniform
- #### Gaussian

>[!definition] Prior probability
>The prior or unconditional probability of a proposition expresses an agent’s belief before incorporating new evidence.

- #### Joint probability distribution
	It assigns a probability to every complete assignment of values to those variables.

## Conditional Probability
(NOT causal)