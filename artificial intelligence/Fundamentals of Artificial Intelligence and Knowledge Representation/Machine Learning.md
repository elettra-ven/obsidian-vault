>[!info] Definition 1
>"Learning is constructing or modifying representations of what is being experienced."

This first definition is related to the concept of **supervised** machine learning, which mainly refers to the knowledge that can be extracted from the existing system.

>[!info] Definition 2
>"Learning denotes changes in the system that are adaptive in the sense that they enable the system to do the same task or tasks drawn from the same population more efficiently and more effectively the next time."

This last definition is **operational**, and focuses on the specific tasks and capabilities that the machine can perform (also called **reinforcement learning).

## Types of **learning**:

+ **Supervised Learning**: 
	+ It starts from a set of examples given by a teacher ("training set"). 
	+ It solves problems of classification/regression (ex. patterns recognition).
	
	The "teacher/supervisor" provides data and "ground truths" that are already completely labelled, so the learning of the machine is very effective.
	However, labelling data is very **expensive**, and requires a lot of time and resources.
+ **Unsupervised Learning**: 
	+ Through observations and discovery.
	+ From the outside it does not get any help, but the system that is in charge of analysing the information available, to classify and structure them and to discover patterns. 
	+ Clustering/data mining.
	
	The machine receives data that is not organised or labelled, and tries to organise it by itself.
	This kind of learning is less expensive but more prone to error.
+ **Reinforcement Learning**: 
	+ Learning optimal behaviour from past experiences.
	+ Observation of good and bad choices made (through rewards and punishments), and modify the behaviour accordingly. 
	+ Mainly learns from mistakes.
	+ Finds many applications in robotics.
	
	This type of learning allows the system to be more **flexible**, but it can be applied only if the enterprise can actually afford errors in the training process.

## Applications

- Classification of any kind
- Shares price prediction
- ==Diagnosis based on clinical data==
- Games
- Image recognition
- Robotics
- ==Molecule design and drug discovery==
- Text translation

## Tasks

1. [[Classification]]
2. [[Regression]]
3. [[Clustering]]

## Symbolic an sub-symbolic learning 

**Symbolic learning** is the field of artificial intelligence that focuses on an **high-level**, human-readable representation of ML problems. 
It usually follows a set of fixed and explicit rules to **structure** the representation.

>[!note] An **artificial neuron** works like a biological neuron. Similarly an artificial **neural network** doesn't change its number of cells while training, but it modifies the connections between them, in order to store information, relationships between topics, etc … 

On the other hand, **sub-symbolic learning** learns from vast amounts of data through processes of discovery and pattern-recognition.

---
# Deep Neural Networks and Deep Learning

>[!info] Deep Learning
>models and algorithms that use neural networks with multiple **layers** in order to learn complex functions to identify the most relevant data.

DNNs can have up to hundreds of layers in their stucture.

In Deep Learning concepts are learnt through a **hierarchy of features**, from the simplest to more abstract and complex. 
Representation is implicitly distributed in different layers.

No labels are needed, the feature are extracted by network during the **unsupervised learning**. These features are unknown due to the **black-box** nature of DL architectures. 
The following phase is the **fine tuning**, where performances are improved with a hybrid learning method that is both supervised and unsupervised.

