>[!goal] Goals
>The goal of the explorations is to know each variable and how they relate with each other.
>
>This process generates **questions** and **hypotheses** that help choose the best preparation steps.

![[Pasted image 20261002102703.png]]

## Summary statistics

>[!note] Location: **mean**, **median**.
>If 
>$$\text{mean} > \text{median}$$
>we have a **right skewed distribution**, with a long tail to the right.

**Right skews** can be read more clearly on a **==log== scale** (this transforms a product of many factors into a sum, which is roughly **bell shaped**).

>[!note] Spread
>Standard deviation ($std$), Interquartile Range ($IQR$), ...
>$$IQR = Q3 \ (75\%) - Q1 \ (25\%)$$

### Histograms
We can plot the shape of a distribution with an **histogram**, and we can chose its bin width to better represent the data.

>[!tip] Common bin numbers:
>- $\lceil log_2 N \rceil + 1$
>- $2* IQR / (N^{1/3})$

### Box plots
![[Pasted image 20261002104537.png]]

It shows how the data is spread out using **five key values**:
1. Minimum
2. Q1
3. Q2 (or **median**)
4. Q3
5. Maximum
The dots are **outliers**, single points floating past the whiskers that represent unusual high or low values.

