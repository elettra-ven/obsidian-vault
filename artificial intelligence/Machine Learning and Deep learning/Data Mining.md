**Professor**: claudio.sartori@unibo.it

---

>[!NOTE] Knowledge comes from an understanding of **information**, which is the result of collecting and organising raw **data**.

>[!NOTE] **Insight**
>An **insight** is a meaningful and actionable understanding derived from discovered **patterns** that can support decision-making.

![[Pasted image 20260916102234.png]]

Eventually, data can generate a sequence of actions.

>[!DEFINITION] Business Process
>It's a set of activities (often in the enterprise area) that, once completed, will achieve an organisational/business goal.

When the state of the enterprise is changed, one of the following events happen:
* **Transaction**:
	When executed, it generates or modifies data stored in a DB, to reflect the triggering change.
- **Signal**:
	Is the reading of a measure produced by a sensor. It is collected from the source and can be stored or processed by an actuator.

>[!NOTE] **OLTP** (On-Line Transaction Processing)
>SW programs that support **transaction**-oriented applications.
>They are designed to record basic and necessary routines.
>They must be **available**, **fast**, **concurrent** and **recoverable**.

## Layers of Information Systems 

IS can be layered to simplify and abstract operations in the business workflow.
![[Pasted image 20260916103706.png]]

## Business Intelligence (BI)

> A set of methodologies, processes, architectures, and technologies that transform raw data into meaningful and useful information used to enable more effective strategic, tactical, and operational insights and decision-making.

The **BI Architecture** is necessary in big organisations and is layered as follows:
1. **Data Warehouse**: aggregates and organises the data to obtain a synthetic view of the system. It is structured to support queries and analysis actions.
2. **Staging Layer**: extracts the data and transforms it to correctly load it in the DW.
3. **Data**: is the lowest layer of the "stack", and is composed by raw and un-organised elements.

![[Pasted image 20260916104259.png|405]]

## Analytics vs Data Mining

- **Analytics**:
	Structured decisions driven by data.
- **Data Mining**
	Unstructured decisions driven by data.
	Sometimes they can provide insights in order to define a new structured decision.

### Structured vs Unstructured Decisions
![[Pasted image 20260916104820.png]]

Structured decisions are similar to rules or mechanical and deterministic pipelines.
Unstructured decisions are made "on the fly", and require a knowledge of the external environment to understand the set of possibilities and potential actions.
### Analytics
- **Descriptive**:
	Highest level of analytics. They can be visualised with charts and graphs.
	Answer the question "*What happened?*".
	1. Aggregate data with DB techniques
	2. Understand data
	3. Description through statistics and unsupervised machine learning
* **Diagnostic**:
	They focus of understanding the reasons behind past outcomes.
	Answer the question "*Why did it happen?*".
	Requires domain knowledge and an understanding of the causes.
- **Predictive**:
	Answer the question "What's going to happen?".
	They calculate the most probable value of a variable in a future time, given the history of a set (sequence) of variables.
	It's also where [[Machine Learning]] lives.
- **Prescriptive**:
	Answer the question "How can we make something happen?".
	They suggest actions to be taken to obtain the desired effect, choose among options and strategies and optimize.

## Paradigm Shift

Machine Learning and Generative AI are more and more used as tools to process and organise data, substituting data mining and big data.

More data has been created in the past two years than in the entire previous history of the human race.
Nowadays the stream of data has new sources, such as IoT sensors, devices, wearables, Social Networks, … (organizations, machines and people all produce huge amounts of data).
It has become easier to extract value from **Big Data** (**3Vs**: Big Volume, Big Velocity and Big Variety).

## Cloud Computing

Is a delivery model, similar to an utility, that gives access to a shared pool of configurable computing, resources, storage, …
These services are offered by a provider and can be SW, platforms or whole infrastructures (SaaS, PaaS and IaaS).

Big Data can also be processed without Cloud Computing. In many cases Cloud Computing is a key asset to be able to deal with Big Data, because in presence of one or more of the V it is difficult to use traditional databases or traditional data processing.

---

# Data Mining

It's an intersection between statistics, pattern recognition and DB systems, and it is strictly tied to Machine Learning:
The current consensus sees Data Mining as the discovery process from data sources to  knowledge, and ML for Data Mining as the core of learning models and algorithms which allow the extraction of patterns.

![[Pasted image 20260916111306.png|532]]


We can select data according to our ML task. 
Then ML extracts the patterns and models to be evaluated (probabilistic or statistical evaluations) and trigger some type of action (whether it's a enterprise action or a personal decision).
The resulting informed decision changes the state of the system, and the cycle repeats for the next evaluation.

## Examples
$\rightarrow$ [[Running example - Nordic Mart]]

>Data mining can be used to extract **actionable** patterns or knowledge from existing data.

To be "actionable", a pattern must be useful for enterprise decision-making:
- The pattern must have a good percentage of certainty.
- Timing must be relevant to the problem.

>[!note] **Supervised activities** in Data Mining
Ground Truths are provided to the system in a controlled, labelled way. This data is necessary to produce an informed forecast.

## CRISP-DM Standard Process
*CRoss-Industry Standard Process for Data Mining*
During the development of a project there has to be a cooperation between different subjects, such as tech, law, marketing, etc ...
To allow the different parts to work together they have to speak a **common tongue** $\implies$ a **standard**.

+ ### CRISP-DM cycle
	It focuses on **data-driven decisions**.
![[Pasted image 20260917154747.png|324]]

1. **Business Understanding** 
	What problem are we actually solving.
2. **Data Understanding** 
	What data do we have, is it any good.
3. **Data Preparation** 
	Clean, join, transform for modelling.
4. **Modelling** 
	Apply the mining / ML technique.
5. **Evaluation** 
	Does the result actually answer the business question.
6. **Deployment** 
	Put it to use, and keep it working.

The third step, **Data Preparation**, is the most expensive and consuming phase of the cycle. It should take up to $60-80\%$ of project time.
