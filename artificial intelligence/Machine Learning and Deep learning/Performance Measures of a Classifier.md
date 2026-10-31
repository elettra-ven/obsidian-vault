## "Best" according to what?

When we say a classifier is the best one, best according to which yardstick?
## The confusion matrix 

For a **binary prediction problem** we call one class positive and the other negative. 
Every test record falls into one of four cells depending on its true class and the predicted class: 
- true positives (**TP**)
- false negatives (**FN**)
- false positives (**FP**) 
- true negatives (**TN**). 

Accuracy is simply the fraction of records on the diagonal:
$$(TP+TN)/N_{test}$$and the error rate is one minus that.

![[img/Pasted image 20261028093649.png|334]]

>[!important] Why accuracy is not enough
>When we have an instance of **imbalanced classes**, accuracy is dominated by the majority class, so a model can look excellent while being useless on the class we actually care about.

Classifiers have qualities that no single number captures: 
	**speed** and **scalability**, 
	**robustness** to noisy labels and rare special cases, 
	and **interpretability**. 

Most importantly, ==errors have different consequences==. 
- In medicine a false negative (a sick patient sent home) is usually worse than a false positive, unless the follow-up exams are invasive. 
- In machinery, retiring a healthy machine is a different kind of mistake from missing a real failure. 

This is the seed of cost-based thinking.

---
## Precision, recall, specificity and F1

To look at the positive class properly we need measures that separate the two kinds of error.

### **Precision** is $TP/(TP+FP)$: 
among the records we _predicted_ positive, how many truly are? It tells you how trustworthy an alarm is. 

### **Recall** (also called sensitivity) is $TP/(TP+FN)$: 
among the records that truly are positive, how many did we catch? It tells you how much of the real phenomenon you find. 

### **Specificity** is the mirror image for the negative class, $TN/(TN+FP)$: 
among the true negatives, how many did we correctly leave alone?

Since we often want one number, the **==F1 score==** combines precision and recall using the ==_harmonic_ mean==:

$$F_1 = 2\frac{\text{precision}\cdot\text{recall}}{\text{precision}+\text{recall}}$$

The harmonic mean is deliberately harsh: 
- it is high only when _both_ precision and recall are high 
- it is dragged down by whichever is lower. 

>[!quote] F1 is also called the balanced F-score.

>[!Example] Rule of thumb 
>- **Accuracy** is a first feeling and is misleading with imbalanced classes (it also generalizes to more than two classes). 
>
>- **F1** is always worth a look because it rewards models that are good and balanced on both precision and recall. 
>
>- When the cost of errors is clearly different for positives and negatives, look at **precision** and **recall** separately rather than fusing them.

---

## **Multi-class** confusion matrix

With $C$ classes the confusion matrix becomes $C\times C$. 
Accuracy becomes the sum of the diagonal divided by $N$, and for each class we get a **precision** $TP_i/P_i$ and a **recall** $TP_i/T_i$, simply by treating that class as "positive" and all the others as "negative".

![[img/Pasted image 20261028100525.png|386]]

The worked example has three classes and 200 test records:

|true \ pred|a|b|c|total|
|---|---|---|---|---|
|a|88|14|18|120|
|b|10|40|10|60|
|c|2|6|12|20|
|total|100|60|40|200|

Per class we get: 
![[img/Pasted image 20261028100729.png|267]]

### Averaging the per-class numbers

Tools such as `GridSearchCV` need a **single score**, so we must average the per-class values.
There are three standard ways to do so:

1) The **==macro==** average gives every class the same weight: $$m_{macro}=\frac1C\sum_i m(c_i)$$. 
2) The **==weighted==** average weights each class by its number of true records: $$m_{weighted}=\frac1N\sum_i T_i,m(c_i)$$
3) The **==micro==** average pools all the $TP_i$, $FP_i$, $FN_i$ across classes and computes the measure once, so every _record_ counts the same.

>[!warning] Remember
>- weighted recall
>- micro-average 
>- accuracy 
>  
> **==are always the same number.==**

>[!tip] How to remember which to use?
The easiest way to remember which to use is to ask what question each one answers. 
>- **Micro** asks "how good is each _decision_?"
>- **Weighted** asks "how good is each _class_, scaled by its size?"
>- **Macro** asks "how good is each _class_, all treated equally?"

---

## Taking chance into account: Cohen's κ and MCC

Even a good-looking number can be partly luck. 

>[!example] Example
>If a disease affects 2% of patients, saying "no disease" for everybody gives 98% accuracy without any intelligence. 
>
>The idea is to treat the chance level as a baseline and measure only the improvement over it.

Let's take the three-class classifier again. 

![[img/Pasted image 20261028214858.png|333]]

It predicts a, b and c in the proportion 
$$100:60:40$$
Imagine a **virtual random classifier** that predicts the classes in exactly those proportions but ignores the record, so each row of the true matrix gets split in the same proportions. 

Its matrix has diagonal entries 60, 18 and 4, so it would get $$60+18+4=82$$
**82 records** right by **pure luck**. 

Our real classifier gets **140** right, so it is 58 correct answers _beyond chance_. 

A perfect classifier would get 200, which is 118 beyond chance.

### Cohen's K
**Cohen's κ** is the fraction of the possible improvement that we achieved:

$$\kappa=\frac{58}{118}=0.49\quad(\text{while accuracy was }0.70)$$

In general, if $\Pr(o)=\sum_i TP_i/N$ is the observed agreement between predicted and true labels and $\Pr(e)=\sum_i T_iP_i/N^2$ is the agreement expected by chance, then

$$\kappa=\frac{\Pr(o)-\Pr(e)}{1-\Pr(e)}$$

For two classes this simplifies to $$\kappa=\dfrac{2(TP\cdot TN-FP\cdot FN)}{(TP+FP)(FP+TN)+(TP+FN)(FN+TN)}$$
- κ of 1 means perfect agreement
- 0 means no better than chance
- negative values mean worse than chance (−1 is only reached in special binary cases, a perfect swap).

### Matthews correlation coefficient
The **Matthews correlation coefficient (MCC)** is another chance-aware measure. It is the correlation between the observed and predicted classes:

$$\text{MCC}=\frac{TP\cdot TN-FP\cdot FN}{\sqrt{(TP+FP)(TP+FN)(TN+FP)(TN+FN)}}$$

It ranges from:
- −1 (total disagreement)...
- ...through 0 (chance)... 
- ...to 1 (perfect), uses all four cells of the matrix and is therefore robust with imbalance.

---
## Probabilistic classifiers

A classifier can give a **crisp** prediction (just a class label) or a **probabilistic**, or _soft_, prediction (one probability per class). 

The choice depends on the use: 
- if the decision is **immediate** and **automatic**, a **crisp** label is enough
- if the prediction is one step in a **larger process**, such as ranking, a limited budget or a human check, the **probabilities** are far more useful.

>[!info] Many classifiers that look crisp actually hide probabilities. 
>A decision tree leaf contains training records of various classes, and the fractions of those records are the predicted probabilities.

How to go from probabilities back to a crisp label:
- Binary case:
	We choose a **threshold** $t$ on $P(\text{positive})$. 
	The default is $t=0.5$, but any value is legitimate. 
- Multi-class problems:
	we simply pick the class with maximum probability. 

### Lift and cumulative gains
The **cumulative gains** curve plots the percentage of all positives found within the top $x\%$ of the ranking; 
- random choice gives a straight diagonal line 
- a perfect model climbs steeply to 100% and then stays flat.

>[!info] Lift
>$$Lift = \frac{gains}{x}$$
>For example:
>*How many times better than random selection we are at that depth?* 

### The ROC curve

The ROC (Receiver Operating Characteristic) curve comes from radar signal detection in World War II, where the problem was the trade-off between the hit rate and false alarms in a noisy channel. 
![[img/Pasted image 20261029153905.png|379]]

The picture is of signal plus noise: 
	two overlapping distributions, one for negatives and one for positives, and a threshold somewhere between them. 

Moving the threshold trades hits against false alarms, and the practical problem is to set it according to the requirements of the application.

The more separated the two distributions, the more the curve bulges toward the top-left corner:
![[img/Pasted image 20261031125429.png|448]]
#### AUC

The **area under the ROC curve (AUC)** summarizes the whole curve in one number, independent of any threshold. 
- $1$ for a perfect ranking 
- $0.5$ for a random ranking

>[!info] AUC probabilistic meaning
> It is the probability that a randomly chosen positive gets a higher score than a randomly chosen negative. 
> It is also insensitive to class proportions.

### The precision–recall curve

Using the same thresholds but plotting recall against precision gives the **precision–recall curve**. 
Its random level is not a diagonal but a horizontal line at the positive rate. 

>[!info] When to use it
>It is more informative than the ROC curve when positives are rare, because ROC can look comfortable when there are very many negatives (the **False Positive** ($FP$) rate stays small even if there are lots of false alarms in absolute terms, which hurts precision).
