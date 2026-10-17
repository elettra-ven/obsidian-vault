>[!goal] Goals
>The goal of the explorations is to know each variable and how they relate with each other.
>
>This process generates **questions** and **hypotheses** that help choose the best preparation steps.

![[img/Pasted image 20261002102703.png]]

Data can be of various kinds:
- **Record** data
- **Graph** data
- **Ordered** data
- $...$
  
> [!warning] Types of Data
>
> | Type        | Subtype | Description                                                | Examples                                        | Statistics allowed                                  |
> | ----------- | ------- | ---------------------------------------------------------- | ----------------------------------------------- | --------------------------------------------------- |
> | Categorical | **Nominal** | Labels; only distinguish one from another. Operators: $=, \neq$ | Zip code, eye colour, sex                       | Mode, entropy, contingency, $\chi^2$ test           |
> | Categorical | **Ordinal** | Labels with a total order. Operators: $<, >, \leq, \geq$   | Mineral hardness; bad, fair, good, excellent    | Median, percentiles, rank correlation               |
> | Numerical   | **Interval** | Differences are meaningful. Operators: $+, -$             | Calendar dates, temperature in °C or °F         | Mean, std, Pearson correlation, $t$ and $F$ tests   |
> | Numerical   | **Ratio**   | A true zero; all arithmetic operations                     | Kelvin temperature, mass, length, counts        | Geometric and harmonic mean, percentage variation   |
>
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
![[img/Pasted image 20261002104537.png]]

It shows how the data is spread out using **five key values**:
1. Minimum
2. Q1
3. Q2 (or **median**)
4. Q3
5. Maximum
The dots are **outliers**, single points floating past the whiskers that represent unusual high or low values.

## Data quality check

1. noise
2. outliers
3. missing values
4. duplicates, inconsistencies
#### 1. Noise
Modifications of the original values (often measurement errors) or uninteresting data.
The data preparation will need robust methods to "overlook" the noise and "normalize" it.

#### 2. Outliers
Values considerably different from most of the data (rare events or errors).
They can be detected using the **IQR rule**:
$$IQR = Q3-Q1$$
"Fences" can be defined as ($Q1 -1.5*IQR$) and ($Q3+1.5*IQR$). These values indicate the range outside of which values are candidate outliers. 
>[!danger] Never drop according to the $IQR$ rule! Always understand domain first!

#### 3. Missing values
Data can be not collected, not applicable or not existing.
Records with missing values can be **dropped** if they don't hold informative value, or they can be completed with an **estimate** (**Impute**).
Sometimes it's useful to keep the information as an indicator of what was missing.






