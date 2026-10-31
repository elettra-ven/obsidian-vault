
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


>[!important] Conclusion
>- Decision trees: the best starting point for supervised learning (it's easy to understand, to implement, and to use)
>- Overfitting controlled by the **maximum tree depth** and other hyperparameters
>- Predict discrete values (the class) from continuous or discrete attributes

