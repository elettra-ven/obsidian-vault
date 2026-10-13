Independence identifies situations in which learning the value of one variable does not change an agent’s beliefs about another variable.
## Marginal/unconditional independence
Two events $A$ and $B$ are **independent**, written $A \perp B$, if learning whether $B$ occurs does not change the agent’s belief in $A$:
$$P(A \mid B) = P(A)$$
$$P(B \mid A) = P(B)$$
$$P(A \wedge B) = P(A)P(B)$$
>[!important] Benefits
>For $n$ mutually **independent** Boolean variables, only $n$ parameters are needed, rather than $2^n − 1$.

## Conditional independence
Two variables $X$ and $Y$ are conditionally independent given $Z$ ($X \perp Y \mid Z$), if **knowledge is added to the system**, or if, once $Z$ is known, learning the value of $Y$ does not change the agent’s probability distribution over $X$:
$$P(X \mid Y,Z) = P(X\mid Z)$$
$$P(Y \mid X,Z) = P(Y\mid Z)$$
It can also be written as a **factorization**:
$$P(\text{Toothache}, \text{Catch} \mid text{Cavity}) = P(\text{Toothache} \mid text{Cavity}) P(\text{Catch} \mid text{Cavity})$$

>[!important] Local relevance
>Conditional independence captures **local relevance**: 
>once the directly relevant variables are known, many other variables provide no additional information.
>
>In most cases, the use of conditional independence reduces the size of the representation of the joint distribution from exponential in $n$ to linear in $n$.

## Reversing conditional probabilities
For example:
$$P(+ \mid \text{Disease}) \text{ and } P(+ \mid \neg\text{Disease})$$

The probability of a positive result given a disease is not the same as the probability of a disease given a positive result. 
**Bayes’ rule** allows us to reverse the conditioning.

>[!info] Bayes' rule I
> Using the product rule, the joint event “the patient has the disease and the test is positive” can be **factorized** in **two ways**:
> $$P(A\mid B) = \frac{P(B\mid A)P(A)}{P(B)}$$
>It can be normalized with the constant $\alpha$:
>$$\alpha = \frac{1}{P(B)}$$

$$\text{posterior belief} = \frac{(\text{test result if disease is present}) (\text{prior belif})}{\text{overall probability od a positive result}}$$

### Naïve Bayes I model
A naïve Bayes model consists of one hypothesis variable $H$ and a set of observation variables $E_1, . . . , E_n$. It assumes that the observations are conditionally independent given $H$:
$$P(H,E_1,...,E_n) = P(H) \prod_{i=1}^n(E_i \mid H)$$
![[img/Pasted image 20260928095835.png|229]]

If $H$ has $k$ values and each observation has at most $r$ values, the model requires $(k-1)+nk(r-1)$ free parameters ($o(n)$).

# Bayesian network representation
A [[Constructing Bayesian networks|Bayesian network]] represents a joint probability distribution compactly by combining a directed graph with local conditional probability distributions. The graph makes conditional-independence assumptions explicit and determines how the full joint distribution factorizes.

>[!info] Bayesian network
>For a set of random variable ($X_1,...X_n$) is made of **one node for each variable**.
>The network can be represented ad a **directed acyclic graph** (the edges have directions and it's impossible to come back to a certain node following the directions of the arrows).
>
>Each node has **one local conditional probability** distribution given the knowledge of the parent:
>$$P(X_i \mid \text{Parents}(X_i))$$

The topology of the network matters in terms of independence.

>[!info] Conditional probability tables
>When the variables are discrete, each local distribution can be represented by a conditional probability **table** (CPT). 
>
>For every combination of **parent values**, the corresponding row gives a probability distribution over the possible values of $X_i$.

**A Bayesian network compactly represents a joint probability distribution:**
$$P(\text{Query} \mid \text{Evidence})$$

### Reasoning patterns

#### Predictive (causal) reasoning
Predicts an outcome from known causes. 
It gives a prediction
#### Diagnostic (evidential) reasoning
Infers an unobserved explanation from observed evidence.
It gives an explanation.
#### Intercausal reasoning
Revises one possible explanation after observing the outcome and another possible explanation.

>[!info] Compactness
>A **CPT** for Boolean $X_i$ with $k$ Boolean parents has 2 $k$ rows for the combinations of parent values Each row requires one number p for $X_i = \text{true}$ (the number for $X_i = \text{false}$ is just $1 − p$).
>
>![[img/Pasted image 20260928102107.png]]

>[!warning] Global semantics of a Bayesian network
>The local conditional probability distributions associated with all nodes jointly define the full joint probability distribution:
>$$P(x_1,...,X_n) = \prod_{i=1}^n P(x_i \mid pa_i)$$
>Where $pa_i$ is the value of former knowledge assigned to the parents of $X_i$ in the complete assignment $(x_1,...,x_n)$.

### Example
![[img/Pasted image 20260928102403.png]]

- $P \models (L \perp ...?)$ 
- $P \models (S \perp ...?)$ 
- $P \models (G \perp ...?)$ 
- $P \models (I \perp ...?)$ 
- $P \models (D \perp ...?)$ 
#### Solutions:
- $P \models (L \perp I, D, S\mid G)$ 
- $P \models (S \perp G, D, L\mid I)$ 
- $P \models (G \perp S \mid I)$ 
- $P \models (I \perp D)$ 
- $P \models (D \perp I, S)$ 
- $...$

>[!info] Flow influence
>How does X influence Y ?
>- $X \rightarrow Y$ **(direct cause)**
>- $X \leftarrow Y$ **(direct effect)**
>- $X \rightarrow Z \rightarrow Y$ **(causal trail)**
>- $X \leftarrow Z \leftarrow Y$ **(evidential trail)**
>- $X \leftarrow Z \rightarrow Y$ **(common cause)**
>- $X \rightarrow Z \leftarrow Y$ **(common effect)**

If we are capable to build a path/trail between two variables, I can't say that they are **independent**.

>[!info] Chain trail (in-ed)
$X \rightarrow Z \rightarrow Y$ or **(causal trail)**.
>$$\text{Rain} \rightarrow \text{Wet Grass} \rightarrow \text{Slippery Path}
>$$
>![[img/Pasted image 20260928103242.png|238]]
>
>When $\text{Wet Grass}$ is observed, knowing whether it rained provides no additional information about $\text{Slippery Path}$.

>[!success] Active trail
An **active trail** is a path obtained by following connected nodes, **regardless of the direction of the arrows**.
>
> Le $Z$ be a set of **observed variables**. A **trail** from $X_1$ to $X_n$ is "active given $Z$" if, for every $X_i$:
> - if $X_{i-1} \rightarrow X_i \leftarrow X_{i+1}$, the $X_i$ (or one of its children) $\in Z$ 
> - otherwise, $X_i \notin Z$

Every intermediate node on the trail is either a **collider** or a **non-collider**:
- If it is a **collider** then the node, or one of its descendants, must be observed in order to open a trail.
- If it is a **non-collider**, observing it blocks the trail

### D-separation 
Two sets of nodes $X, Y$ are d-separated given $Z$ if there is no active trail between any $X \in X$ and $Y \in Y$ given $Z$.

For every probability distribution represented by the Bayesian network, if $X$ and $Y$ are d-separated given $Z$ $\implies$ $X \perp Y \mid Z$.

>[!info] How to determine if $X$ and $Y$ are independent given $Z$?
>1. Traverse the graph bottom-up marking all nodes in $Z$ or having descendants in given $Z$. 
>2. Traverse the graph from $X$ to $Y$ , stopping if we get to a **blocked node**.
>3. If we can’t reach $Y$, then $X$ and $Y$ are independent.

### ==🟠Guided D-separation example==

![[img/Pasted image 20261012091821.png|246]]

The relevant trails are:
$$T_1 : C \leftarrow A \rightarrow D$$

$$T_2 : C \leftarrow B \rightarrow D$$

$$T_3 : C \rightarrow E \rightarrow F \rightarrow D$$

#### **Step 1.**
$$C\perp D \ ?$$
$C$ and $D$ are **not independent**.
The trails through $A$ and $B$ are active. 
The collider trail through $F$ remains blocked because neither $F$ nor one of its descendants is observed.

#### **Step 2.**
$$C\perp D \mid A \ ?$$
Observing the non-collider $A$ **blocks** $T_1$. 
However, $T_2$, through the unobserved common cause $B$, is still **active**.

#### **Step 3.**
$$C\perp D \mid A \mid B\ ?$$
Observing $A$ and $B$ blocks both common-cause trails. 
The remaining trail is still blocked at the unobserved collider $F$.

#### **Step 4.**
$$C\perp D \mid A, B, J ?$$
$C$ and $D$ are **not independent**.
$J$ is a descendant of the collider $F$. 
Observing $J$ opens the collider trail $T_3$.

#### **Step 5.**
$$C\perp D \mid A, B, E, J ?$$
$C$ and $D$ are **independent**.
Observing $J$ opens the collider at $F$, but observing $E$, a non-collider on that trail, blocks it again. 
All trails between $C$ and $D$ are now blocked.


>[!important] **Local Semantics**
>For every node $X$, once its parents are observed, $X$ is conditionally independent for all its non-descendants that are not parents:
>$$X \perp (\text{NonDescendants(X)}\textbackslash \text{Parents(X)}) \mid \text{Parents(X)}$$
>
>To assess how likely a node is, it is sufficient to know the values of its direct parents. 
>Once they are known, learning about any other non-descendant provides no additional information.

>[!waring] Theorem
>For a Bayesian network, the local Markov property is equivalent to the global factorization of the joint probability distribution:
>$$\text{local semantics} \Longleftrightarrow \text{global semantics}$$

