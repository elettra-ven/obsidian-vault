>[!info] **Classification** is the task of approximating a **mapping function** ($f$) from input variables ($X$) to discrete/categorical output variables ($y$), often called **labels**, **categories** or **classes**.

It's a **supervised** learning task, which means that the machine needs a large training dataset of labelled data.

It can be **binary** or **[[#Multi-class classification|multi-class]]** depending on the number of possible classes assignable, and it can be **single** or **multi-label** depending on the number of assignable classes that can be labelled to a single prediction.

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
## Multi-class classification

>[!tip] From binary to multi-class
>It can be handled in 2 ways:
>1) **extend** the algorithm and the model 
>2) **combine** several binary classifiers

### Combination strategies

1) *one-vs-rest*
2) *one-vs-one*

>[!info] OVR

>[!info] OVO


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

### [[Model Selection and Reliable Estimates#Cross-validation|Cross-validation]]
![[img/Pasted image 20261022155256.png|448]]

---
# Types of classificators

- [[Decision Trees]]
- [[Naïve Bayes classifier|Naïve Bayes]]
- [[Logistic Regression]]
- 

---
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
# $\rightarrow$ [[Performance Measures of a Classifier]]

