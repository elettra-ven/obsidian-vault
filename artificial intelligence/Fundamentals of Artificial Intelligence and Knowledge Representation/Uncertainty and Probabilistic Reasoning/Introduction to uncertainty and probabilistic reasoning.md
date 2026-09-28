## Types of uncertainty

* **Partial observability**: 
	relevant information missing, delayed, noisy... 
* **Uncertain outcomes**: 
	the same action may lead to different results.
* **Dynamic environments**: 
	world may change while reasoning.

Agents need to act under uncertainty, so we should provide them techniques and methods to manage these situations.
For example, we can build AI models without handling *noise*.

![[img/Pasted image 20260921094318.png|505]]

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

The probability distribution of $X$ assigns a probability to every variable $x_i \in \chi$:
$$P_x(x_i) = P(X=x_i)$$
Therefore, the probability measure $P$ induces a probability distribution for every random variable $X$.

Random variables can also be used to define **events**:
>[!tip] An **event** is specified by stating which value, or values, a random variable may take.
### Propositions

>[!tip] A **proposition** denotes the event consisting of all possible worlds in which it is true.

Let *a* be a proposition. Its probability is the  probability of each atomic event where *a* is true.
Therefore, a proposition is a disjunction of mutually exclusive atomic events:

![[img/Pasted image 20260921180612.png]]

For example:
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
A probability density function (**pdf**) describes how probability is locally distributed over the possible values of the variable.
The value that would be assigned to a single "point" is now assigned to a "region" (density).

>[!info] Example:
>A dart lands uniformly at random on a circular dartboard of radius 10 cm.
>Let $L$ denote the location where the dart lands. The dartboard is a continuous space: 
>there are infinitely many possible landing locations. The centre is a single point with no area, so: $$P(L=\text{centre})=0$$
>An exact point is too small to have positive probability in a continuous space.

For a continuous random variable, probabilities concern regions of possible values, rather than exact individual values.

>[!important] Probability density function (pdf)
>Let $X$ be a continuous random variable with values in $\chi$. 
>A nonnegative integrable function: $$p_X : \chi \rightarrow \mathbb{R}_{\geq 0}$$ 
>	Is a **pdf** for $X$ if: $$\int_{\chi} p_X(X)\ \mathrm{d}x = 1$$

Therefore, the probability that $X$ falls in an interval $[a,b]$ is the area under its density curve, $\int_{a}^{b}p_X(X)\mathrm{d}x$.
### Distributions:
- #### Uniform
	![[img/Pasted image 20260921203640.png|301]]
	$$p_X(x) = \begin{cases} \frac{1}{b - a} & \text{if } a \le x \le b, \\ 0 & \text{otherwise.} \end{cases}$$
- #### Gaussian (Normal)
	![[img/Pasted image 20260921204325.png|305]]
	If:
	$$X \sim \mathcal{N}(\mu, \sigma^2)$$
	Then its pdf is:
	$$p_X(x) = \frac{1}{\sqrt{2\pi}\sigma} e^{\frac{-(x-\mu)^2}{2\sigma^2}}$$
	- $\mu$ is the **mean** (0 in standard Gaussian)
	- $\sigma$ is ste SD (1 in standard Gaussian)

>[!definition] Prior probability
>The prior or unconditional probability of a proposition expresses an agent’s belief before incorporating new evidence.

- #### Joint probability distribution
	The joint probability distribution over a set of random variables assigns a probability to every complete assignment of values to those variables.
	$$\begin{aligned} P(\text{Weather} = \text{sunny}) &= P(\text{Weather} = \text{sunny} \land \text{Cavity} = \text{true}) \\ &\quad + P(\text{Weather} = \text{sunny} \land \text{Cavity} = \text{false}) \\ &= 0.144 + 0.576 = 0.72 \end{aligned}$$

## Conditional Probability
$$P(X \ | \ \text{Evidence} = e)$$
It represents an agent's belief about X given $\text{Evidence} = e$.
It is **not a logical or causal rule**.

For two propositions $a$ and $b$, with $P(b)\neq0$:
$$P(a \mid b) = \frac{P(a \land b)}{P(b)}$$
Product rule:
$$P(a \land b) = P(a \mid b) P(b) = P(b \mid a) P(a)$$

By applying the product rule to every combination of values of two random variables, we can construct their **joint probability distribution**.

>[!note] General Product Rule
>$$\begin{aligned}
P(X_1, \dots, X_n) &= P(X_1, \dots, X_{n-1}) P(X_n \mid X_1, \dots, X_{n-1}) \\
&= P(X_1, \dots, X_{n-2}) P(X_{n-1} \mid X_1, \dots, X_{n-2}) P(X_n \mid X_1, \dots, X_{n-1}) \\
&= \dots \\
&= \prod_{i=1}^{n} P(X_i \mid X_1, \dots, X_{i-1})
\end{aligned}$$

# Inference using **full joint distributions**
If we know a complete joint probability distribution, we can answer any probability query by **summing** **the entries** corresponding to the possible worlds in which the query is true.
In our table, for any proposition $\phi$, we sum the events in which $\phi$ is true:
$$P(\phi) = \sum_{\omega : \omega \models \phi} P(\omega)$$
We can also use the full joint table to compute **conditional probabilities**.
For example:

>We start with the following joint distribution
![[img/Pasted image 20260928092525.png]]

$$P(\neg\text{cavity} \mid \text{toothache}) = \frac{P(\text{cavity} \land \text{toothache})}{P(\text{toothache})}$$
$$\implies P(\neg\text{cavity} \mid \text{toothache}) = \frac{0.016+0.064}{0.108+0.012+0.016+0.064}$$

## Normalization I
A vector of probabilities contains the probability mass of the two alternatives in the original joint distribution.

>[!info] Norm I
>We redistribute this mass over the two remaining alternatives so that their probabilities sum to 1, while preserving their relative weights.

The normalization factor can be denoted by $\alpha$ :
$$\alpha = \frac{1}{P(\text{probability mass of the original joint distribution})}$$

### Probability query
A probability query asks for the agent’s posterior joint probability distribution over one or more query variables $Y$ , given observed values $E = e$ of some evidence variables:
$$P(Y \mid E=e)$$

- $X$: all random variables in the domain.
+ $Y$: query variables, whose posterior distribution we seek;
+ $E$: evidence variables, whose values e have been observed;
+ $H = X \\ (Y \cup E)$  hidden variables

>[!info] Conditional inference
>Is an enumeration of  possible worlds with evidence.
>1. Fix the observed evidence $E = e$. 
>2. For each possible value of $Y$ , sum the probabilities of all compatible worlds, varying the hidden variables $H$. 
>3. Normalize the resulting values using $\alpha$, so that the distribution over $Y$ sums to 1.

The queries can be answered by fixing the evidence and summing over every possible assignment $h$ of the hidden variables:
$$P(Y \mid E=e) = \alpha P(Y,E=e) = \alpha \sum_h P(Y, E=e, H=h)$$




