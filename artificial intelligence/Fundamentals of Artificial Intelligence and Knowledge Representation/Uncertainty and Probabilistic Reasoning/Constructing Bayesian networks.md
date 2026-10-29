We can construct a Bayesian Network from an **ordering**:

Assume that the variables are ordered as $X_1, . . . ,X_n$.
For each variable $X_i$ , choose a set of parents $\text{Parents}(X_i) \subseteq \{X_1, . . . ,X_{i−1}\}$ such that all other preceding variables are conditionally irrelevant once the parents are known: 
$$X_i \perp (︁ \{X_1, . . . ,X_{i−1}\} \textbackslash \text{Parents}(X_i)) \mid \text{Parents}(X_i)$$
Equivalently: 
$$P(X_i \mid X_1,...X_{i-1}) = P(X_i \mid \text{Parents}(X_i))$$

>[!note] Why this construction works:
>By the **chain rule**:
>$$\begin{split}P(X_1,...,X_n) 
>& = \prod_{i=1}^n P(X_i \mid X_1,...,X_{i-1}) \\
>& = \prod_{i=1}^n P(X_i \mid (\text{Parents}(X_i))
>\end{split}$$
>
>The resulting network therefore represents the full joint probability distribution.


## Monty Hall puzzle

We model the three random variables:
- $Prize \in \{l,m,r\}$
- $Choice \in \{l,m,r\}$
- $HostOpens \in \{l,m,r\}$

The host's choice **depends** on the position of the price and on the contestant's choice.
The resulting network is:
$$Prize \rightarrow HostOpens \leftarrow Choice$$

![[img/Pasted image 20261012094253.png|275]]

$Prize = l \implies P(HostOpens = m) = \frac{1}{2}$
$Prize = m \implies P(HostOpens = m) = 0$
$Prize = r \implies P(HostOpens = m) = 1$

If the prize is behind the left door, the host can open either remaining door. If it is behind the right door, the host must open the middle door.

Each prize location has prior probability 1/3.

$Prize = l \ \ : \ \frac{1}{3}*\frac{1}{2} = \frac{1}{6}$
$Prize = m : \ \frac{1}{3}*0 = 0$
$Prize = r \ : \ \frac{1}{3}*1 = \frac{1}{3}$

>[!note] Normalization
>Let's normalize these values:
>$$\frac{1}{6}+0+\frac{1}{3} = \frac{1}{2}$$
>
>- $P(prize = l\mid evidence) = \frac{1}{6}*\frac{2}{1} = \frac{1}{3}$
>- $P(prize = r\mid evidence) = \frac{1}{3}*\frac{2}{1} = \frac{2}{3}$

The contestant should therefore switch to the right door.

### Plausible Network Structure
#### 1. Constraint-based methods
- perform **statistical tests of conditional independence**; 
- infer which edges must be absent or may be present;
- search for a **graph** compatible with these constraints.
#### 2. Score-based methods
- define a score that measures how well a candidate network explains the data, while **penalizing** unnecessary complexity;
- search for the structure with the **best score**.
  
---
# Causal networks
A subset of the Bayesian network where arrow stand for **causal** relations.

>[!info] For example:
>$Fire \longrightarrow Smoke$
>and 
>$Fire \longleftarrow Smoke$
>are both valid Bayesian network and represent the same **joint distribution**. 
>However, they represent two different concepts, and are not equivalent.

>[!tip] Causal direction
>A causal arrow $X_j \rightarrow X_i$ states that $X_j$ is a direct input to the mechanism that generates $X_i$.

## Structural equation
For each variable $X_i$ , a structural equation specifies the mechanism that produces its value:
$$X_i = f_i(\text{Parents}(X_i), U_i)$$
An arrow $X_j \rightarrow X_i$ is present when $X_j$ is a **direct argument** of the **mechanism** $f_i$.

==🟣Structural equation represents an autonomous causal mechanism assumed to remain unchanged to measurements and local changes in the environment.==
It remains **stable**.

We can model a system with **unmodeled variables** or ==🔴error terms==:
![[img/Pasted image 20261012101939.png|221]]
$$\begin{split}
& C = f_C(U_C) \\
& R = f_R(C,U_R) \\
& S = f_S(C,U_S) \\
& W = f_W(S,R,U_W) \\
& G = f_G(W,U_G)  
\end{split}$$


A Bayesian network lets us update beliefs after observing evidence.
A causal model also lets us ask what would happen if we actively changed a variable in the system.
	We can act and do **intervention** of the network, meaning we can change the structural equations.

>[!info] **Interventions**:
>It removes all the arrows that are entering in $X$.
>$$do(X=x)$$
>It denotes an intervention that sets $X$ to the value $x$ from outside the system.

For example:
$P(WetGrass \mid Sprinkler = true)$
$P(WetGrass \mid  do(Sprinkler = true))$

The first asks: 
	“What do we believe about the wet grass after observing that the sprinkler is on?” 
The second asks: 
	“What would happen to the wet grass if we turned the sprinkler on?”

---
# Representing conditional distributions

We need a compact way to assign probability to these networks. We do this by exploiting the **Locality exploration**.

>[!tip] A **conditional probability table** (CPT) lists one probability distribution for every combination of parent values.

This is practical only when a node has few discrete parents. Else, the CPT grows exponentially with the number of parents.

## Continuous $vs$ Deterministic variables

For **deterministic** variables, instead of specifying a separate probability for every combination we can find a formula that contains all of the variables.

>[!note] Example:
>$$ NorthAmerican \equiv Canadian \vee US \vee Mexican$$

For **continuous** variables we can define a physical relationship.
Instead of listing infinitely many combinations of continuous values, the equation specifies how the water level changes from its direct causes.

>[!note] Example:
>$$ \frac{\delta Level}{\delta t} = inflow + precipitation − outflow − evaporation$$

>[!warning] **Noisy-OR**
>We use the probabilistic interpretation of the **logical OR** ($\vee$) to define uncertain causal relation:
>
>Noisy-OR is a **compact** conditional distribution for a Boolean effect with several Boolean causes.
>Each active cause can trigger the effect, but may also fail. Conditional on the active causes, these failures are **assumed** to be **independent**.

Noisy-OR distributions model **multiple noninteracting causes**.
1. Parents $U_1, ..., U_k$ include all causes.
2. Independent failure probability $q_i$ for each cause alone:
$$\implies P(x \mid U_1...U_j,\ \neg U_{j+1}...\neg U_k) = 1 - \prod_{i=1}^j q_i$$
That is derived from $P(Y=true \mid X1,...,Xn) = 1- P(Y=false \mid X1,...,Xn) =  1 - \prod_{i=1}^j q_i$.

![[img/Pasted image 20261012104400.png|463]]

We call $0.1, \ 0.2,$ and $0.6$ **inhibition probabilities**.

Noisy-OR allows to incapsulate **uncertainty** into the clauses.

>[!info] Joint probability of two events
>$$P(M,J) = P(M)P(J\mid M) = P(J)P(M\mid J)$$

>[!warning] How do we choose an ordering and parent sets?
>- **No causal knowledge**:
>	We must seek an ordering or a parent set that exploit conditional independences in the domain and make the local conditional distributions easy to assess.	
>
>- **With causal knowledge**:
>	We must use the knowledge for selecting the right order that often exposes conditional independences and therefore leads to a more compact network.

We are not trying to make every variable independent. 
We are trying to find an ordering and a small set of direct parents for each variable, so that the remaining earlier variables do not add further information once those parents are known.

![[img/Pasted image 20261019092114.png|543]]

- The first example presents 5 free parameters:
$$1_{P(A)}+2_{P(M\mid A)}+ 2_{P(A\mid M)} = 5$$
- The second example presents 7:
$$1_{P(M)}+2_{P(J\mid M)}+ 4_{P(A\mid M,J)} = 7$$


---

# Hybrid network

A network with both discrete and continuous variables.
To model these kind of networks we have two options:
1. **Discretization**
	- We replace continuous variables with a finite set of **intervals**.
	- Then we can use ordinary CTPs.
	- It's a trade-off between information and the size of the CPT.
2. **Compact parametric conditional models**
	- We use a **canonical family** specified by a finite number of parameters.
	- A continuous child with continuous and/or discrete parents.
	- A discrete child with one or more continuous parents.

>[!important] Conditional density for a **continuous** child (variable $Y$)
>$$p(y \mid Parents(Y))$$
>
>For every fixed assignment of the parent values, this density is nonnegative and integrates to 1 over the possible values of Y .
>
>A compact **canonical family** represents this conditional density through a finite number of parameters.

>[!important] Conditional probability model for a **discrete** child (variable $Y$)
>Let $X$ be a continuous parent of $Y$.
>$$p(Y=y \mid X = x)$$
>
>Since the parent domain is continuous, these probabilities cannot be listed in a finite CPT. 
>A compact canonical family represents them through a function with a finite number of parameters.

---

# Representing conditional distributions

## Dynamic Bayesian networks
A compact, template-based representation of a probability distribution over the evolution of a system through **time**.

We introduce the **system state** at time $t$:
$$X^{(t)} = \{X_1^{(t)}, ..., X_n^{(t)}\}$$

>[!note] Trajectory
>It's a complete sequence of system states:
>$$(X^{(0)},X^{(1)},...,X^{(T)})$$

We can specify a joint probability distribution over trajectories:
$$P(X^{(0)},X^{(1)},...,X^{(T)})$$
==We can make assumptions on the fact that a state in a certain time step depends only on the previous state==:

>[!info] Markov assumption
>$$P(X^{(t+1)}\mid X^{(0)},...,X^{(t)}) = P(X^{(t+1)}\mid X^{(t)})$$

## Learning conditional distributions

Given a network structure, **parameter learning** estimates the conditional distributions from available data. 
More generally, this is a form of **==density estimation==**.

>[!tip] Common learning approaches
>- **Maximum likelihood**: choose the parameters that make the observed data most likely 
>- **Bayesian learning**: combine a prior belief about the parameters with the observed data 
>- **EM**: estimate parameters when some variables are hidden or some values are missing

---
# Beyond Bayesian networks

## 1. PGM (Probabilistic graphic models)

Graphs used to represent a **joint probability distribution** compactly.

>[!info] Markov networks
>Undirected graphs with **compatibility factors**.
>There are symmetric relationships and constraints between variables.
>
>**Represents a joint distribution through local compatibility relations, rather than through conditional probability tables.**
>
>Its joint distribution is defined from nonnegative factors (compatibility functions):
>$$P(X)=\frac{1}{Z} \prod_{c\in C} \phi_c(X_c)$$
>
>Where $Z$ is a normalization constant.

These models assign **scores** (not probabilities) to the edges of the graph.

