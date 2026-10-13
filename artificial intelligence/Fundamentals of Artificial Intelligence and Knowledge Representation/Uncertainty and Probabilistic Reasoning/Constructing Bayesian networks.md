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

>[!warning] Noisy-OR
>We use the probabilistic interpretation of the **logical OR** ($\vee$) to define uncertain causal relation:
>
>Noisy-OR is a conditional distribution for a Boolean effect with several Boolean causes. 
>Each active cause can trigger the effect, but may also fail. Conditional on the active causes, these failures are **assumed** to be **independent**.

Noisy-OR distributions model **multiple noninteracting causes**.
1. Parents $U_1, ..., U_k$ include all causes.
2. Independent failure probability $q_i$ for each cause alone:
$$\implies P(x \mid U_1...U_j,\ \neg U_{j+1}...\neg U_k) = 1 - \prod_{i=1}^j q_i$$
![[img/Pasted image 20261012104400.png|463]]