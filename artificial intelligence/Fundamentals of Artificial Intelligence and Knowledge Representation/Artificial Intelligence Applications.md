- Decision support system
- Games/formal systems
- NLP
- Computer Vision
- Robotics and Autonomous systems

## Knowledge based systems
Such as **Decision support systems**.
The main bottleneck of these systems is the retrieval of the knowledge.
Knowledge can change in time, can be ambiguous or come from different sources.

Agentic AI provides **decision automation**, that performs the action directly excluding human intervention.

- **Descriptive analytics**: 
	uses data to describe the system, with the help of human intervention.
- **Diagnostic analytics**:
	uses data to understand the causes (fault/root cause diagnosis).
- **Predictive analytics**:
	uses data to predict future evolutions thanks to simulations, digital twins, series prediction and ML classification/regression.
- **Prescriptive analytics/Decision support**:
	Optimize the system selecting preferred scenarios and calculating impacts from the simulations provided by the previous analytics.

## Power Capping
The **predictive model** gives an estimate of the power consumption, while de **decision/prescriptive model** operates as a power-aware job dispatcher.
The consume of a specific task cannot be known in advance.

Malfunctions are detected automatically by DL models:
An autoencoder is trained only on normal behaviours, so that it can be used to reconstruct error to detect anomalies.