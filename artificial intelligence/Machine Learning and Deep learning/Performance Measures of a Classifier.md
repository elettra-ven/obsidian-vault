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

## The cost of errors

In practice predictions drive decisions and mistakes cost money or worse. Granting a loan to a bad payer is not the same as refusing a good one; a false oil-spill alarm is not the same as an undetected spill; an unexpected plant failure is usually more expensive than a false fault prediction; mailing someone who won't buy is cheaper than ignoring a promising customer.

The tree beats "nobody" but loses to "everybody", which is embarrassing for a model, and raises the question of whether we can do better with the very same model.

There are two main ways of making a classification pipeline cost-aware. The first is **cost-sensitive learning**, where we make the learner itself weigh the expensive errors more. This can be done by _resampling_ (altering the class proportions in the training data, for instance duplicating the examples of the costly class, which is also a remedy for imbalanced classes) or by _instance weights_ if the algorithm supports them, as in `DecisionTreeClassifier(class_weight={0: 1, 1: 10})` or `class_weight="balanced"`, which weights classes inversely to their frequency. The second way is to keep the model as it is and change the decision threshold, which is the subject of the next section.

---
## Probabilistic classifiers

A classifier can give a **crisp** prediction (just a class label) or a **probabilistic**, or _soft_, prediction (one probability per class). The choice depends on the use: if the decision is immediate and automatic, a crisp label is enough, but if the prediction is one step in a larger process, such as ranking, a limited budget or a human check, the probabilities are far more useful.

Many classifiers that look crisp actually hide probabilities. A decision tree leaf contains training records of various classes, and the fractions of those records are the predicted probabilities. In the iris example, the rightmost leaf holds 26 flowers split 1/2/23, giving the probability vector $(0.04, 0.08, 0.88)$. The caveat is that small leaves give unreliable probabilities, and the NordicMart tree has only 13 leaves, hence only 13 distinct probability values.

To go from probabilities back to a crisp label, in the binary case we choose a **threshold** $t$ on $P(\text{positive})$. The default is $t=0.5$, but any value is legitimate. For multi-class problems we simply pick the class with maximum probability. Changing $t$ changes the confusion matrix: lowering it makes the model predict positive more often, so recall goes up while precision usually goes down.

The NordicMart plot of precision, recall and F1 against the threshold shows exactly this seesaw. At very low thresholds recall approaches 1 but precision collapses toward the base rate of 12%. Around the default 0.5, precision is about 0.48 and recall about 0.24, and past roughly 0.73 nobody is flagged any more, so everything drops to zero. Plotting the total cost against the threshold is where the payoff comes: with a threshold of about 0.15 the cost falls to €6,460, better than both trivial strategies (€10,800 and €7,920). Nothing about the model changed; only the operating point did.

### Lift and cumulative gains

If we only care about _ranking_ customers, we can sort the test records by decreasing $P(\text{positive})$ and look at the top $x\%$. The **cumulative gains** curve plots the percentage of all positives found within the top $x\%$ of the ranking; random choice gives a straight diagonal line, and a perfect model climbs steeply to 100% and then stays flat. **Lift** is gains divided by $x$, i.e. how many times better than random selection we are at that depth. Notice that only the order of the scores matters here, not the actual probability values. For NordicMart, lift starts very high among the first few customers contacted (above 5) and decays toward 1 as we contact everybody, since contacting 100% of customers is by definition random.

### The ROC curve

The ROC (Receiver Operating Characteristic) curve comes from radar signal detection in World War II, where the problem was the trade-off between the hit rate and false alarms in a noisy channel. The picture is of signal plus noise: two overlapping distributions, one for negatives and one for positives, and a threshold somewhere between them. Moving the threshold trades hits against false alarms, and the practical problem is to set it according to the requirements of the application.

Each threshold gives one point in a plane whose axes are the **TP rate** $TP/T_{pos}$ (which is just recall) and the **FP rate** $FP/T_{neg}$ (which equals 1 − specificity). Sweeping the threshold from high to low draws the curve. The more separated the two distributions, the more the curve bulges toward the top-left corner; with no separation it hugs the diagonal.

To draw it from data: sort the test records by decreasing $P(\text{positive})$ and start at $(0,0)$, which corresponds to a threshold above every probability (nothing predicted positive). Lower the threshold to the next probability value; if the record that enters is a true positive, take a step up, if it is a negative, take a step right, and if several records tie, take a diagonal step. You end at $(1,1)$, where everything is predicted positive. The slide's hand-drawn example uses 20 NordicMart customers, 5 churners and 15 non-churners, and gives an area of 0.76.

On the full NordicMart test set (900 customers, only 13 distinct probabilities, hence a curve with 13 corner points), the default threshold $t=0.5$ corresponds to TP rate 0.24 and FP rate 0.04, a conservative point in the bottom-left. The threshold $t=0.15$, the cost-optimal one, sits at TP rate 0.51 and FP rate 0.15, a point further up and right on the same curve. The two operating points live on one and the same model.

The **area under the ROC curve (AUC)** summarizes the whole curve in one number, independent of any threshold. It is 1 for a perfect ranking and 0.5 for a random one. It has a nice probabilistic meaning: it is the probability that a randomly chosen positive gets a higher score than a randomly chosen negative. It is also insensitive to class proportions. In scikit-learn you use `roc_auc_score`, or `scoring="roc_auc"` for model selection. The NordicMart tree has AUC = 0.71.

### The precision–recall curve

Using the same thresholds but plotting recall against precision gives the **precision–recall curve**. Its random level is not a diagonal but a horizontal line at the positive rate (12% here). It is more informative than the ROC curve when positives are rare, because ROC can look comfortable when there are very many negatives (the FP rate stays small even if there are lots of false alarms in absolute terms, which hurts precision). Its summary number is the **average precision**, 0.29 for NordicMart, to be compared with the 0.12 of random guessing.

-
