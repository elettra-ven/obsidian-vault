>[!example] Bayes Theorem
>- Hypothesis $H$
>- Evidence $E$
>
>$$Pr(H|E) = \frac{Pr(E|H)Pr(H)}{Pr(E)}$$
>
>- $Pr(H)$: prior probability
>- $Pr(H|E)$: posterior probability

We make the following **assumption**:
	Each attribute is independent from each other **within the class**.
$$Pr(d_1 = v_1, d_2 = v_2\mid c) = Pr(d_1= v_1\mid c)*Pr(d_2= v_2\mid c)$$
	This is a very strong assumption, nevertheless, the methos works (even if it's not fully satisfied).

## Weather/Play Data

![[img/Pasted image 20261029154123.png]]

- likelihood **play = yes** = $\frac{2}{9}\times \frac{3}{9} \times \frac{3}{9} \times \frac{3}{9} \times \frac{9}{14} = 0.0053$
- likelihood **play = no** = $\frac{3}{5}\times \frac{1}{5} \times \frac{4}{5} \times \frac{3}{5} \times \frac{5}{14} = 0.0206$

Which normalized is:

- $Pr(yes) = 20.5\%$
- $Pr(no) = 79.5\%$

With the Bayes method we can split evidence into pieces, one per attribute:
$$Pr(c|E) = \frac{Pr(E_1|c)\times Pr(E_2|c) \times...\times Pr(E_D|c) \times Pr(c)}{Pr(E)}$$
>[!info] It's called *naive* because the independence assumption is simplistic.

>[!fail] In the table there is a **singularity**: **Zero-frequency problem**
>`Pr(overcast|no) = 0`
>However we know that the value is frequent with many attributes and many distinct values.
>**One zero should not veto all the other evidence**.
>>[!success] How can we solve this?
>>### Laplace smoothing
>>$$Pr(d=v_i \mid c) \approx \frac{af_{d=v_i,c}+\alpha}{af_c+\alpha V}$$
>>- $af_{d=v_i,c}$: absolute frequency of value $v_i$ of attribute $d$ in class $c$
>>- $af_c$: absolute frequency of class $c$
>>- $V$: number of distinct values for $d$
>>- $\alpha$: smoothing parameter $\in [0,1]$
>>  
>>$$Pr(overcast\mid no) = (0+1)/(5+3) = 0.125$$

## Missing values
There is no need to discard a record with missing values.
- **If it's a testing record, to classify**, 
  We omit the attribute from the product.
- **If it's a training record**,
  We don't count the attribute. The frequencies are calculated over the present values, not over the total number of records.

---
# Gaussian Naïve Bayes classifier
This implementation assumes that all continuous features follow a normal distribution within each class.

>[!danger] **The frequencies are not applicable**...
>...because frequency data is discrete, non-negative, and heavily skewed, which directly violates Gaussian Naïve Bayes' core assumptions that features are continuous, unconstrained, and normally distributed.

Given the mean $\mu$ and the standard deviation $\sigma$, we can use the **density** instead:
$$f(x) = \frac{1}{\sqrt{2\pi}\sigma}\exp(-\frac{(x-\mu)^2}{2\sigma^2})$$

## Log loss
Is a performance metric used for evaluating binary classification models that output probabilities between $0$ and $1$.
It measures the **uncertainty of a model** by comparing its predicted probabilities against the actual true labels, ==heavily penalizing predictions that are both **wrong and confident**==.

*For example:*
We've trained a binary classifier: 
	for every test we have a probability $p$ of class "yes" or class "no".

We can calculate the **log loss** as the average of $\mathcal{l}$:
$$\mathcal{l} = -y \ln(p) - (1-y)ln(1-p)$$
The lower, the better.

>[!question] Why log loss?
>- [[Performance Measures of a Classifier#The ROC curve|AUC]]: only the ranking of the records 
>- [[Performance Measures of a Classifier#The precision–recall curve|Precision, recall]]: only the decisions at one threshold 
>
>Neither says whether a predicted 30% really means 30%.

---

>[!done] Pros
>- **Clear semantics**: probabilistic knowledge
>- **Training is counting**: very fast, also with many attributes
>- Often **excellent** **ranking**, even when the assumption is false

>[!fail] Cons
>- Degrades when the assumptions fail
>- Probabilities often too extreme