>[!info] **Classification** is the task of approximating a **mapping function** ($f$) from input variables ($X$) to discrete/categorical output variables ($y$), often called **labels**, **categories** or **classes**.

It's a **supervised** learning task, which means that the machine needs a large training dataset of labelled data.

It can be **binary** or **multi-class** depending on the number of possible classes assignable, and it can be **single** or **multi-label** depending on the number of assignable classes that can be labelled to a single prediction.

The **test-set** is a portion of the labelled dataset that is used to calculate the **classification accuracy**, with the help of specific metrics.

## (Two input) perceptron

![[img/Pasted image 20260917102621.png|424]]

The pattern belonging to the class will be those such that:
$$w_1 x_1 + w_2 x_2 - \theta > 0$$
Where $\theta$ is the *bias* of the perceptron.
This equation results in a line in a bidimensional space:

![[img/Pasted image 20260917102821.png|379]]

## $\mathbf{n}$-layer networks

For example a 3-layer network is able to separate convex regions number of edges $\leq$ number hidden neurons.
![[img/Pasted image 20260917103056.png|394]]


The **perceptron** can represent only linear functions. 
If, however, we use multi-layer networks, the expressive power increases substantially. 

>[!warning] Universal approximation theorem: 
>A feed-forward network with one hidden layer and a finite number of neurons can approximate any continuous function with desired accuracy.

---

## Supervised classification
Given:
- A dataset $X: N$ individuals, $D$ attribute values each.
- A class vector $Y:$ for each individual $x$ in the class $y(x)$.
- A finite set of $C$ class values.
- Class values given by the **supervision**.
The main goal is to guess $y(x)$ for individuals **not examined**.

The algorithm, given and individual with unknown class, must be able to compute the class.

>[!important] Decision function
>$$M(x,\theta) = y(x)_{pred}$$
>
>$\theta$ represents the values of the parameters.

>[!info] Learning
>Given $X$ and $Y$, find $\theta$ that **reduces the prediction error** as much as possible.

## Vapnik–Chervonenkis dimension
Classification models differ in their power to **shatter** the data set into subsets with homogeneous classes.

The shattering power of a classification model (binary case only, for simplicity).

- $N$ elements  $\rightarrow 2^N$ possible labelings (learning problems)
- If $M(\cdot,\theta)$ can shatter all of them (a suitable $\theta$ exists for every labelling) $\rightarrow$ VC dimension $\geq N$
- A straight line in the plane has VC dimension **3**
- In real cases data often make even a line "not so bad"

## Two flavors of classification

- **Crisp**: one label per individual
- **Probabilistic**: a probability for each possible label

## Measuring a classifier

- **Training error**: 
  mistakes on the data used for learning
- **Generalization error**: 
  mistakes on new data (the one we care about, but unknown: new data have no labels yet)
- Training error is optimistic: 
  a lookup table scores 0% training error
- More flexibility $\implies$ lower training error,
- **Underfitting**: 
  model too simple for the pattern $\implies$ high training error, high test error
- **Overfitting**: 
  model learns the noise too $\implies$ low training error, much higher error on new data
- Goal: 
  the **simplest model that captures the pattern** (the "sweet spot" between underfitting and overfitting on the error vs complexity curve)


>[!note] **Workflow**
>
>1. **Learn** the model: 
>   training set with known labels (ground truth), representative (obtained by a random process)
>2. Estimate its **accuracy**: 
>   test set with labels known but hidden from the model; compare predicted and true labels
>3. Use the model on **new individuals**

### Cross-validation
One split gives one estimate; a different random split gives a different test error. This can vary a lot on small data sets.

**Cross Validation** splits data into $k$ folds (e.g. $k=5$).
In the $i$-th round, fold $i$ is the **test set** and the others the **training** **set**.
- $k$ models, each tested on data it has not seen; report **mean and standard deviation** of the $k$ errors

**The test set is the future:** never learn from it, never choose by looking at it (otherwise its error is no longer an honest estimate). 
Same for anything computed from data before the split $\implies$ ==data leakage==.

## Decision trees

>[!info] Run-time classifier (**node execution**):
>```
>if node is inner:
>	if test on attribute d of element x:      execute node_yes
>	    else:                                  execute node_no
>	else:  # leaf
>	    predict class of x as c
>```

## Learning a tree (model generation)

Given a set $X$ of elements with known class:

- all elements of class $c$, or $X$ is small $\implies$ **leaf** labelled $c$
- otherwise: choose a test on a single attribute (two or more outcomes), the test becomes the root with one branch per outcome, partition $X$ by outcome, **recurse** on each subset

## Tree building

In the beginning, the root node contains the entire training-set. At every step, the tests split the population in different nodes, reducing the classification range. The choice of the test is fundamental for the efficiency and accuracy of the splitting.

## What's in a node

Each node of a (scikit-learn) tree shows:

- **test**: attribute and threshold, e.g. `petal width <= 0.75` (internal nodes only)
- **entropy**: impurity of the node
- **samples**: coverage, % of the dataset reaching the node
- **value**: distribution of the classes in the node, e.g. `[0.373, 0.32, 0.307]`
- **colour**: darker = lower entropy
- Internal nodes have a test and children; **leaves** have none and give the predicted class (the majority one)


In the beginning, the root node contains the entire training-set. 
At every step, the tests **split** the population in different nodes, reducing the classification range.

>[!info] The choice of the **test** is fundamental for the efficiency and accuracy of the splitting.


## Information Theory

>[!warning] **Information theory**
>Information theory is a mathematical branch of probability and statistics that deals with quantifying, storing, and communicating data through the exploration of certain statistical distributions.
>
>*For example*:
>Two weather stations send one symbol per day: 
>- **A** always sunny; 
>- **B** sunny, cloudy, rainy or snowy, equally often.
> 
>Whose messages carry more information?
>	==🔵Station B, because you cannot predict tomorrow’s symbol before receiving it==
>

**The general case is**:
Source $X$ with $V$ possible values, probabilities
$$P(v_1) = p_1, ... , P(v_v) = p_v$$
The average number of bits for the transmission is:
$$H(x) = - \sum_jp_j \log_2(p_j)$$
We call $H(x)$ the **entropy** of the source $X$.
	The higher the value of the entropy ($\max 1$), the more the probabilities are similar.

>[!important] Entropy in **Classification**
>Low entropy of the class labels is representative of:
>- Low diversity
>- High purity
>- Clear majority

For $C$ classes the maximum entropy is $\log_2 C$ (uniform distribution). With 3 classes: $\log_2 3 = 1.585$.

---

# Information gain

The test of a node is the one that **maximises the information gain** (IG): the entropy of the parent minus the weighted entropy of the children.

$$IG = H(p) - \sum_{i=1}^{ds} \frac{N_{p,i}}{N_p} H(p_i)$$

For a numeric attribute and a binary split, try every candidate threshold $t$ (children: $d < t$ and $d \geq t$) and keep the best.

## Algorithm (binary splits)

```
buildTree(dataset X, node p):
    if all class values of X are c:
        return p as a leaf, label c
    if no attribute gives a positive information gain in X:
        c = most frequent class in X
        return p as a leaf, label c
    find attribute d and threshold t with maximum IG in X
    create children p_left, p_right
    X_left  = selection on X with d <  t ; buildTree(X_left,  p_left)
    X_right = selection on X with d >= t ; buildTree(X_right, p_right)
```

- The label of each part is the **majority class**
- Recursion goes on in every subset with a **non-empty minority**
- It is a recursive, ==greedy algorithm==
	**Recursion ends when**:
	- the node is pure, or
	- it is not pure but no test gives a positive gain

---
# Errors and overfitting

## Training set error
It is the error on the data used to _build_ the model.
It's probably a **lower limit** of the error on new data. 
==🔴We want an **upper limit**, or at least a realistic value.==

>[!danger] **Causes of non-zero training error**
>- the limits of decision trees in general (tests on single attribute values can fail)
>- insufficient information in the predicting attributes

## Test set error
More indicative of the behaviour on **new** data.
The test error so much worse because of **overfitting**.

>[!warning] Overfitting
>
>- The learning is affected by **noise**: the performance on the test set is (much) worse than on the training set.
>
>A decision tree is a _hypothesis_ $h$ of the relationship between predicting attributes and class.
>
>- $error_{train}(h)$: error of $h$ on the training set
>- $error_{\mathcal{X}}(h)$: error of $h$ on the entire data set
>
>$h$ **overfits** the training set if there is an alternative hypothesis $h'$ such that
>$$error_{train}(h) < error_{train}(h')$$ $$error_{\mathcal{X}}(h) > error_{\mathcal{X}}(h')$$

**Causes of overfitting**
1. Presence of **noise**: bad values in predicting attributes or class labels, unusual cases; the model is influenced by partly wrong data
2. Lack of **representative** instances: some situations under-represented or absent in the training set (it's quite common)

A good model has low **generalization error**, which means that it works well on examples different from the training ones.

---
# Pruning

## Pruning and hyperparameters

 >[!info] **Pruning**: 
 >Simplifying the model when using a decision tree.
 
 >[!info] **Hyperparameters**: 
 >Settings of the learning algorithm, _not learned from data, chosen by us_.
 >Each model family has its own.
 >
 >The hyperparameters are often chosen through **cross-validation** on the training set.

---

# Impurity functions

Look for the split with maximum **purity**. A measure of the purity of a node: 
- two classes in the same proportion $\implies$ **low purity** 
- only one class $\implies$ **highest purity**

Measures of the impurity of a node:
- **Entropy**
- **Gini index**
- **Misclassification error**

## Gini index

>[!question] Gini index
>Node $p$ with $C_p$ classes. 
>Assign a class _at random_, following the class frequencies of the node.
>**How often are we wrong?**

- For class $j$: frequency $f_{p,j}$, other classes $1 - f_{p,j}$
- Probability of a wrong assignment: $f_{p,j}(1 - f_{p,j})$
- Gini index = **total probability of a wrong classification**:

$$GINI_p = \sum_j f_{p,j}(1 - f_{p,j}) = \sum_j f_{p,j} - \sum_j f_{p,j}^2 = 1 - \sum_j f_{p,j}^2$$

### **Splitting** and the Gini index 
Node $p$ split into $ds$ descendants $p_1, \dots, p_{ds}$; $N_{p,i}$, $N_p$ = records in the $i$-th descendant and in $p$. 
Choose the split with the maximum reduction of the Gini index:

$$GINI_{split} = GINI_p - \sum_{i=1}^{ds} \frac{N_{p,i}}{N_p} GINI(p_i)$$
---
# Data leakage

It happens when information that will **not be available at prediction time** reaches the model during learning.
- As an effect, the evaluation will be **too optimistic** (great test score, poor results in production)

Data leakage can mainly happen in two ways:
1. from the **test set** into the training
2. from the **future** into the features

## Spotting leakage with a decision tree

- Symptoms:
    - results too good to be true
    - one attribute with an enormous information gain
    - the tree is a single stump on that attribute
 
- Remedy: 
	split first, 
	prepare on training only, 
	check every feature's timing.

>[!warning] Complexity of DT induction
>Given:
>$N$ instances and $D$ attributes in $\mathcal{X}$, the tree height is $O(\log N)$.
>
>**Overall cost:** $$O(DN \log N)$$
>

## Greedy algorithms
DT building is a **greedy** algorithm, it doesn't guarantee the best possible result.

- At each decision point: the choice with the maximum **immediate gain**
- A sequence of individually sub-optimal choices could lead to a better final result (greedy can get stuck in a local optimum)

---

>[!important] Conclusion
>- Decision trees: the best starting point for supervised learning (it's easy to understand, to implement, and to use)
>- Overfitting controlled by the **maximum tree depth** and other hyperparameters
>- Predict discrete values (the class) from continuous or discrete attributes




