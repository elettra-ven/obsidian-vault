>[!info] From scores to probabilities
>A weighted sum of the attributes can be defined as a score:
>$$z = w_0+w_1x_1+w_2x_2+...+w_Dx_D = \mathbf{w}*\mathbf{x}+w_0$$
>$z\in (-\infty,+\infty)$
>We can **compress** it into a $(0,1)$ interval, with the function **==sigmoid==**:
>$$Pr(y=1|x)$$

![[img/Pasted image 20261029162905.png|355]]
The **sigmoid** is monotonic, therefore **larger score = larger probability**.

>[!note] Odds
>$$\frac{p}{1-p}$$

>[!note] Log-odds (logit)
>$$\ln(\frac{p}{1-p})$$
>It ranges over $(-\infty,+\infty)$.

In **logic regression** the log-odds are a **linear function** of the attributes.
![[img/Pasted image 20261029163351.png]]

## Maximum likelihood

$$\mathcal{L}(w) = \prod^N_{i=1}p_i^{y_i}(1-p_i)^{1-y_i}\qquad p_i = \sigma(w*x_i+w_0)$$

Maximum likelihood estimates the weight $w$ that maximizes $\mathcal{L}$.

### How to interpret the weights

>[!info] Weight $w_j$ : 
>change of the log-odds when $x_j$ grows by 1, all the other attributes remain fixed.

**Correlated attributes share the weight**, whereas single values are unstable, and must be read with care.

>[!warning] Standardization
>Useful when attributes are on very different scales.
>$$\text{z-score}: x' = (x-\mu)/\sigma$$
>where:
>- $\mu$ is the mean
>- $\sigma$ is the standard deviation
>>[!danger] Avoid **leakage**
>>Compute $\mu$ and $\sigma$ **only on the training set**, never on the whole pre-splitting dataset.

---

>[!done] Pros
>- **Simple**, fast, interpretable weights 
>- Outputs **probabilities**, usually **well calibrated**
>- Strong baseline for any binary problem

>[!fail] Cons
>- **Linear** in the log-odds (non-linear patterns need new attributes)
>- Sensitive to correlated attributes (**unstable**)
>- Needs **scaling**
>- Needs complete data

