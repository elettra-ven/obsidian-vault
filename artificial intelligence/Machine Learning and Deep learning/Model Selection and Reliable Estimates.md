We must estimate the run-time performance of the models in order to correctly compare the alternatives.
Every estimate must take into account a **random** component.

## Holdout, validation and test

>[!info] Holdout
>It's a data-splitting technique (training set and test set) used to evaluate how well a model generalizes to unseen data.
>>[!quote] Stratification
>>A random split has a high probability to have the same class proportions in both parts.
>>This phenomenon is called **stratification**.
>
>If the set is smaller or the classes are unbalanced we need to be able to ==🔵guarantee the stratification==.

We decide a random split for the supervised data $\mathcal{X}$. The **test error** will give a close estimate of the run-time error.


|                  | **Bigger training set** | **Bigger test set** |
| ---------------- | ----------------------- | ------------------- |
| Data set size    | small data set          | large data set      |
| Model complexity | flexible models         | simple models       |
| Run-time stakes  | low-stakes domain       | critical domain     |

The **[[#Cross-validation|cross-validation]]** ensures a trade-off between the sizes of the test set (more stable estimate) and the training set.

### Train, validation, test
![[img/Pasted image 20261022154213.png]]
For each configuration of the cross-validation, the learning is done on the training set and the results are scored on the validation set.

The **best configuration** is then chosen and it can be scored on the test set.

>[!warning] The test set can't be involved in the validation or it would make the selection of the test scores **optimistic**. 

#### Pros and cons:

>[!done] Fast, ensures that the hyperparameters chosen on data independent of the final test

>[!failure] Choice based on a single, smaller portion, holds less data for training

## Cross-validation 

One split gives one estimate; a different random split gives a different test error. This can vary a lot on small data sets.

**Cross Validation** splits data into $k$ folds (e.g. $k=5$).
In the $i$-th round, fold $i$ is the **test set** and the others the **training** **set**.
- $k$ models, each tested on data it has not seen; report **mean and standard deviation** of the $k$ errors

**The test set is the future:** never learn from it, never choose by looking at it (otherwise its error is no longer an honest estimate). 
Same for anything computed from data before the split $\implies$ ==data leakage==.

#### Pros and cons:

>[!done] The score is averaged over the $k$ rounds and the final model learns on all the training records

>[!fail] The train/validate loop is repeated $k$ times (not very efficient)

---
# Model selection recipes

| recipe                                             | chooses on     | estimate                | trainings       | use                         |
| :------------------------------------------------- | :------------- | :---------------------- | :-------------- | :-------------------------- |
| **0 zero level**                                   | $-$ (defaults) | training error: useless | $1$             | never as an estimate        |
| **1 quick holdout**                                | $-$ (defaults) | honest, for defaults    | $1$             | baseline, in a hurry        |
| **2 tune on test**                                 | test           | optimistic              | $c$             | avoid                       |
| **3 [[#Train, validation, test\|train/val/test]]** | validation     | good                    | $c + 1$         | large data, slow algorithms |
| **4 [[#Cross-validation\|cross-validation]]**      | $k$ folds      | best                    | $c \cdot k + 1$ | default choice              |

> **Note:** $c$: number of hyperparameter configurations

# Hyperparameter search

- **Grid search**
- **Random search**
  (fixed budget of random combinations)

---
## Test set

It is defined as a sample of the run-time data.

>[!warning] Bernoulli process
>**Empirical error frequency**:
>$$f = E/N$$
>Where $E$ are the errors and $N$ are the test records.
>
>==🟠Each test record is an independent binary experiment.==

We choose a **confidence level** $1-\alpha$ and we focus on the interval that contains $p$ (approximation of $f$) with probability $1-\alpha$ (for example $95\%$).

![[img/Pasted image 20261022162818.png|421]]

For example,
![[img/Pasted image 20261022162857.png|418]]

Every estimate has an **error bar** that shrinks as $1/\sqrt{N}$

### Consequences of model selection

- Two models whose intervals overlap widely: no evidence of a difference
- Report estimate and uncertainty, never the estimate alone
- Prefer the simpler model, when noise is heavily present

We can use the calculated error of decision tree leaves to **[[Decision Trees#Pruning|prune]]** statistically the branches (sub-trees) that would be too small and too uncertain.

>[!quote] Statistical pruning
>- $e_i :$ weighted pessimistic error of its leaves
>- $e_r :$ pessimistic error of its root turned into a leaf
>  
> Prune if $e_r \le e_i$
> 

