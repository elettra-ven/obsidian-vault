A [[Independence#Bayesian network representation|Bayesian network]] represents a joint probability distribution in a compact way.
==We now study how to compute posterior probabilities directly from its local conditional distributions.==

# Inference tasks

>[!info] Probability query
>A probability query asks for the conditional distribution of query variables $Y$, given observed evidence $E = e$:
>$$P(Y\mid E=e)$$

We can query the network asking for posterior probabilities:
- **==Marginal query==**
  *How likely is this event to occur?*
  $$P(X_i\mid E=e)$$
- **==Joint query==**
  *How likely is each combination of events?*
  $$P(X_i,X_j \mid E=e)$$
- **Explanation**
- **Optimal decisions**
- **Value of information**
- **Sensitivity analysis**

## 1. Inference by enumeration

>[!example] Both my neighbours John and Mary call to say that my alarm is ringing. The alarm may have been triggered by a burglary, but occasionally also by a minor earthquake. **How likely is a burglary?**
>
>$$P(B\mid j,m)$$
>$$P(B\mid j,m) = \frac{P(B,j,m)}{P(j,m)}$$
>The denominator is shared by both values of B:
>$$P(B\mid j,m) = P(b,j,m) + P(\neg b,j,m)$$
>The sum of both the possible values of B.

>[!warning] Procedure
>1) Fix the evidence $j, m$. 
>2) For each value of $B$, enumerate the assignments of $E, A$. 
>3) Multiply the corresponding **CPT** entries and sum to obtain $q_b$ and $q_{\neg b}$. 
>4) Normalize:
>   $$P(B\mid j,m) = \alpha <q_b,Q_{\neg b}>,\qquad \alpha=\frac{1}{q_b+q_{\neg b}}$$

### Evaluation tree
![[img/Pasted image 20261102095041.png]]

- Enumeration is quite expensive (space: $O(n)$, time: $O(d^n)$)
- Enumeration is inefficient (same values are evaluated in different branches)

## 2. Inference by **variable elimination**

Is an exact inference algorithm that sums out hidden variables one at a time, **storing** intermediate results as factors to avoid repeated computation.

>[!info] Factor 
>A factor is a nonnegative function of a set of variables. 
>
>For discrete variables, it can be represented as a table with one value for each assignment. 
>Its scope is the set of variables on which it depends.

>[!warning] Procedure
>1) **Fix the evidence:** 
>   restrict the local distributions to the observed values, obtaining initial factors.
>2) **Choose an order** for eliminating hidden variables.
>3) For each hidden variable Z:
>	- **collect** all current factors involving Z
>	- **multiply** them and sum out Z
>	- **replace** the collected factors with the resulting factor
>4) **Multiply** the remaining factors.
>5) **Normalize**

Each local model is a table of nonnegative values. We can exclude the models that are **given** (in the former example, $j,m$).

![[img/Pasted image 20261102095553.png|397]]

- The standard time bound is $O(n*d^k)$, the computation is **complex**.

>[!done] Polytrees
>A Bayesian network is a polytree if any two nodes are connected by at most one path when arrow directions are ignored.
>
>- **The calculation is linear for polytrees**
>>[!fail] However, exact probabilistic inference in **unrestricted Bayesian networks** is NP-hard!


---

## Simplifications

### 1. non-ancestors nodes

>[!example] $$P(JohnCalls \mid Burglary=true) = P(J\mid b)$$
>- Query variable: $J$. 
>- Evidence: $B = true$. 
>- Hidden variables: $E, A, M$.

All the nodes that are not ancestors of the query variable can be eliminate, as they do not provide valuable information:

![[img/Pasted image 20261102100840.png|196]]

### 2. [[Independence#D-separation|D-separation]]

>[!danger] Theorem
>If $Y$ is **d-separated** from the query variable $X$ by the evidence variables $E$, then $Y$ is irrelevant as additional evidence for the query: 
>$$P(X | E = e, Y = y)= P(X | E = e)$$
>whenever the conditioning event has positive probability.

---

# Exam-style exercise

>[!abstract] Online shop
>You are designing a new e-commerce system, to sell products online. You can display advertisements (“ads”) of three types: book ads, toy ads, and holiday ads.
> However, your web site can only display ==one ad at a time==. 
> 
> **Your system should guess which type of ad has a higher chance of being clicked.**
> 
>You don’t have verified profile information on each customer.
>You can, however, guess at least some profile features, based on your domain knowledge and on your observations about which ads the customer does or doesn’t click on (“clicking behaviour”).
>
>In particular
>>[!example] profile features
>>- Young: is this a young customer $(y, \neg y)$
>>- Married: is the customer married $(m, \neg m)$ 
>>- Wealthy: is the customer wealthy $(w, \neg w)$
>>- Children: does the customer have children $(c, \neg c)$
>
>>[!example] clicking behaviour
>>- Holiday: the customer clicks on a holiday ad $(h, \neg h)$
>>- Book: the customer clicks on a book ad $(b, \neg b)$
>>- Toy: the customer clicks on a toy ad $(t, \neg t)$


>[!question] Q0.
>How would you model this domain using a Bayes net?

![[img/Pasted image 20261102101928.png]]

>[!question] Q1. 
>You first display a sequence of ads and record which types of ads get clicked; then, you use that data to infer some of the customer’s profile features.
>
>1) **Which reasoning pattern are you following?**
>2) **Show a query that uses the customer’s observed clicking behaviour as evidence.**

>[!question] Q2. To fully define this Bayesian network, how many independent values are needed?
>
>>[!done] Solution

>[!question] Q3. Define a CPD for Children
>
>>[!done] Solution

>[!question] Q4.
>Assume this is your network, with its parameters:
>$...$
>- $$Calculate $P(c|h)$ using variable elimination.$$
>>[!done] Solution

$...$