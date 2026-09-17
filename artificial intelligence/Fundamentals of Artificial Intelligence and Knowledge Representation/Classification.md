>[!info] **Classification** is the task of approximating a **mapping function** ($f$) from input variables ($X$) to discrete/categorical output variables ($y$), often called **labels**, **categories** or **classes**.

It's a **supervised** learning task, which means that the machine needs a large training dataset of labelled data.

It can be **binary** or **multi-class** depending on the number of possible classes assignable, and it can be **single** or **multi-label** depending on the number of assignable classes that can be labelled to a single prediction.

The **test-set** is a portion of the labelled dataset that is used to calculate the **classification accuracy**, with the help of specific metrics.

## (Two input) perceptron

![[Pasted image 20260917102621.png|424]]

The pattern belonging to the class will be those such that:
$$w_1 x_1 + w_2 x_2 - \theta > 0$$
Where $\theta$ is the *bias* of the perceptron.
This equation results in a line in a bidimensional space:

![[Pasted image 20260917102821.png|379]]

## $\mathbf{n}$-layer networks

For example a 3-layer network is able to separate convex regions number of edges $\leq$ number hidden neurons.
![[Pasted image 20260917103056.png|394]]


The **perceptron** can represent only linear functions. 
If, however, we use multi-layer networks, the expressive power increases substantially. 

>[!warning] Universal approximation theorem: 
>A feed-forward network with one hidden layer and a finite number of neurons can approximate any continuous function with desired accuracy.
