# Bioenergetics and thermodynamics

>[!info] Equilibrium equation
>For a general reversible reaction:
>$$aA + bB \Longleftrightarrow cC + dD$$
>The equilibrium equation is:
>$$K_{eq} = \frac{[C]^c[D]^d}{[A]^a[B]^b}$$
>Where:
>- $K_{eq}$ is the **equilibrium constant**
>- $[C]^c[D]^d$ are the **products** (concentration)
>- $[A]^a[B]^b$ are the **reactants** (concentration)
>  
> A large value of $K_{eq}$ indicates that the reaction will continue until almost all of the reactants have been converted into products.

>[!info] Standard conditions
>- 298 K
>- 25 °C
>- 1 atm
>- **pH = 7**

## (**Gibbs'**) Standard free-energy change

$$\Delta G'° = -RT\ ln(K'_{eq})$$

Where $R$ is the **ideal gas constant** ($8.314 \ \ J/mol*K$), and $T$ is the temperature.
It is simply an alternative mathematical way of expressing its equilibrium constant.

>[!tip] **Exergonic reactions**
>$$\Delta G < 0$$
>Are spontaneous and release free energy.
>Reactants, after a peak, result in **less product**.

>[!tip] **Endergonic reactions**
>$$\Delta G > 0$$
>Are non-spontaneous and absorb free energy.
>Reactants result in **more product**.

If $\Delta G = 0$ the reaction has reached its **equilibrium**.

According to Gibbs' equation, if $K'_{eq} > 1 \longleftrightarrow \Delta G'°<0$ and reaction goes forward under standard conditions.


>[!danger] **Adenosine triphosphate**
>It's the major carrier of chemical energy in al cells. It represents 100% renewable energy:
>![[Pasted image 20261001163011.png]]

ATP's phosphate groups are tied together by **two high energy bonds**. Breaking down these bonds releases energy.
This process can be done by a special class of **enzymes**, **ATPase**, trough **hydrolysis** of the terminal phosphate group.
The result of this is ADP, $H^+$ and **inorganic phosphate**, which **wont be protonated at neutral pH (7)**. 
$$ATP + H_2O \ \longleftrightarrow \ ADP + Pi + \Delta G$$
or
$$ATP^{4-} + H_2O \ \longleftrightarrow \ ADP^{3-} + HPO_4^{2-} + H^+$$ Under standard conditions, free-energy change for ATP hydrolysis is $-30.5 \ \ kJ/mol$ (between $-50$ and $-65 \ \ kJ/mol$ in intact cells).
==However, ATP provides energy by group transfers, not by simple hydrolysis.==

>[!tip] Energy Charge in cells
>$$\text{Energy Charge} = \frac{[ATP]+0.5[ADP]}{[ATP]+[ADP]+[AMP]}$$

>[!info] Coupled reaction
>A reaction where the free energy of a thermodynamically favourable transformation and a thermodynamically unfavourable one are mechanistically joined into a new reaction.
### How do cells use **ATP**?
**1. Biosynthesis**  
ATP drives anabolic reactions by coupling the energetically unfavourable formation of macromolecules (proteins, nucleic acids, polysaccharides, lipids) to ATP hydrolysis. 
Monomers are first activated (e.g., amino acids to aminoacyl-tRNA, nucleotides to NTPs), and polymerization is then driven forward by pyrophosphate ($PPi$) hydrolysis by pyrophosphatase, which makes the overall $\Delta G$ strongly negative.

**2. Contraction**  
In muscle cells, filaments of protein repeatedly slide past each other to achieve contraction of the cell.
An input of ATP is required for the filaments to reset and slide again.

**3. Chemical Activation**  
Proteins can become activated when a high-energy phosphate from ATP attaches to the protein, activating it.
Other types of molecules can also become phosphorylated by transfer of phosphate from ATP.

**4. Importing Metabolites**  
Metabolite molecules such as amino acids and sugars can be transported into cells against their concentration gradients by coupling the intake of the metabolite to the inward movement of an ion moving down its concentration gradient (**ion pump**), this ion gradient being established using ATP.

**5. Active Transport**  
Most animal cells maintain a low internal concentration of $Na^+$ relative to their surroundings, and a high internal concentration of $K^+$.
This is achieved using a protein called the **sodium-potassium pump**, which, using energy from ATP, pushes out sodium and pumps in potassium.

**6. Cytoplasmic Transport**  
Directed movement of vesicles, organelles, mRNA, and macromolecules along the cytoskeleton by motor proteins, that are attached to the elements with connector proteins and use ATP to power their movement.

**7. Flagellar Movements**  
Microtubules within flagella slide past each other to produce flagellar movements.
ATP powers the sliding of the microtubules.

**8. Cell Crawling**  
**Actin** filaments in a cell's cytoskeleton continually assemble and disassemble to achieve changes in cell shape and to allow cells to crawl over substrates or engulf materials.
The dynamic character of actin is controlled by ATP molecules bound to actin filaments.

**9. Heat Production**  
The energy produced by the hydrolysis of the ATP molecules is transformed into heat.
These reactions often take place in mitochondria or in contracting muscle cells, and may be coupled with other reactions.
The heat generated can be used to maintain an organism's temperature.

>[!tip] ATP production
>It can happen in two ways:
>- **Substrate level phosphorylation**
>- **Oxidative phosphorylation**
>$$C_6H_{12}O_6 + 6O_2 \longrightarrow 6CO_2 + 6H_2O + \text{ATP}$$
## ROLE OF $NAD(P)^+$ AND $NAD(P)H$ IN [[Metabolism|METABOLISM]]

> [!abstract] Summary 
> Cells "burn" fuel (glucose, fatty acids) by **removing electrons** (==oxidation==) from it. 
> **NAD+** charges itself with those electrons (becoming **NADH**) and delivers them to the electron transport chain, where their energy is used to make ATP (catabolism). 
> **NADPH** gives electrons back for building molecules (anabolism).

>[!tip] Memory trick: 
>**OIL RIG** = Oxidation Is Loss, Reduction Is Gain (of electrons).

In carbon compounds, more C–H bonds (**more reduced**) equals more stored energy.

## Oxidation states of carbon

From most reduced (most energy) to most oxidized (least energy):

![[Pasted image 20261002141854.png|519]]

For example:

| Molecule                     | Methane | Methanol | Formaldehyde | Formic acid | CO2 |
| ---------------------------- | ------- | -------- | ------------ | ----------- | --- |
| ΔG°' of oxidation (kJ/mol)   | −820    | −703     | −523         | −285        | 0   |
| ΔG°' of oxidation (kcal/mol) | −196    | −168     | −125         | −68         | 0   |

> [!note] 
> The more negative, the more energy is released when that molecule is fully oxidized to $CO_2$. 
> Each step toward $CO_2$ releases part of the energy. 
> 
> Metabolism does the same thing in **small steps**.

## Catabolism vs anabolism

|                       | **Catabolism**                                              | **Anabolism**                                                |
| --------------------- | ----------------------------------------------------------- | ------------------------------------------------------------ |
| **Direction**         | Breaks molecules down                                       | Builds molecules up                                          |
| **Carbon State**      | Reduced $\rightarrow$ Oxidized                              | Oxidized $\rightarrow$ Reduced                               |
| **Electron Carriers** | $\text{NAD}^+ \rightarrow \text{NADH}$ (receives electrons) | $\text{NADPH} \rightarrow \text{NADP}^+$ (donates electrons) |
| **Energy**            | Releases energy (makes $\text{ATP}$)                        | Consumes energy (uses $\text{ATP}$)                          |
| **Example**           | Glucose $\rightarrow \text{CO}_2$                           | $\text{CO}_2$ / Acetyl-CoA $\rightarrow$ Fatty acids         |


> [!tip] 
> **NAD**H = **Ca**tabolism-ish (NADH is **produced** by breakdown). 
> **NADP**H = **P**roduction/anabolism (NADPH is **used** to build).

## The NAD+/NADH couple

- **NAD** = **N**icotinamide **A**denine **D**inucleotide. 
	The nicotinamide part comes from vitamin **B3 (niacin)**.
- **NAD+ = oxidized form** (empty, ready to take electrons). 
	**NADH = reduced form** (loaded with electrons).

$$\frac{1}{2}O_2 + \text{NADH} + H^+ \longrightarrow H_2O + \text{NAD}^+$$

The reactive part is the **nicotinamide ring** (N).
$$\text{NAD}^+ + 2e^- + H^+ \longrightarrow \text{NADH}$$ (it actually accepts a **hydride ion, : $H^-$** = 1 proton + 2 electrons; the extra $H^+$ stays in solution).

>[!tip] Remember
>**NADP+/NADPH** = same molecule with one **extra phosphate group**. 
>This tiny tag lets enzymes tell them apart: 
>different jobs, different enzymes.

### Energy in NADH

$$\tfrac12 O_2 + NADH + H^+ \rightarrow H_2O + NAD^+ \qquad \Delta G \approx -220\ kJ/mol$$

>[!info] Compare **ATP hydrolysis $vs$ NADH oxidation**: 
>ATP hydrolysis $\approx −30.5 \ kJ/mol$ (standard). 
>So one NADH carries enough energy for **several** ATP.

The cell does not release the $220 \ kJ$ at once (it would be lost as heat). 
It lets electrons fall down the **Electron Transport Chain** in small steps and captures energy to make ATP.

|                       | **ATP Hydrolysis**                                  | **NADH Oxidation (via ETC)**                                                        |
| --------------------- | --------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **Primary Mechanism** | Breaking a chemical bond (hydrolysis)               | Transferring electrons (redox/oxidation)                                            |
| **Energy Released**   | $\sim -30\text{ kJ/mol}$                            | $\sim -220\text{ kJ/mol}$                                                           |
| **Immediate Utility** | Powers direct cellular work (motor proteins, pumps) | Generates multiple ATP molecules via oxidative phosphorylation                      |
| **Metabolic Analogy** | Ready to "spend" immediately anywhere.              | Needs to go through the Electron Transport Chain to be converted into multiple ATP. |

## NADH oxidation is coupled to ATP synthesis

1. NADH gives 2 electrons to a ETC protein $\longrightarrow$ becomes NAD+ (+ $H^+$).
2. Electrons pass through the **ETC** (series of protein complexes).
3. At the end, $\text{electrons} + H^+ + \tfrac12 O_2 \longrightarrow H_2O$ (oxygen is the final electron acceptor).
4. The energy released along the way is used for **controlled synthesis of ATP**.
5. NAD+ is now free to go back and pick up more electrons.

> [!warning] Don't forget NAD+ is **recycled**, not consumed. The cell has a small pool of it, so if NADH is not re-oxidized, catabolism stops.

---
# Enzymes

> [!abstract] Summary
> Almost every reaction in a cell would be far too slow without **enzymes** (mostly proteins) that ==**lower the activation energy**==, speeding the reaction up without changing its equilibrium.

## Why we need enzymes

Complete oxidation of glucose:

|Conditions|Time|
|---|---|
|25 °C, no enzymes|~100 **years**|
|180 °C, no enzymes (fire)|~5 **minutes**|
|25 °C, **in cells** (enzymes)|a few **seconds**|

Cells cannot be heated to 180 °C, so they use enzymes.

## ==Thermodynamics vs kinetics==

- **ΔG** (free energy change) tells you **if** a reaction can happen spontaneously.
- **Activation energy ($E_a$)** tells you **how fast** it happens.

>[!info] Activation energy
>The minimum energy needed to bring molecules to the state where they can react (the "hill" between reactants and products, the **transition state**).

**Example**: 
	ATP hydrolysis is very exergonic ($\Delta$G negative) but ATP is **stable** because $E_a$ is high; it breaks fast only when an **enzyme** catalyses it.

![[Pasted image 20261003104151.png|516]]


>[!important] What enzymes functions
>- **Lower the activation energy** $\longrightarrow$ faster reaction.
>- Are **not consumed**: unchanged at the end.
>- Are very **specific** (substrate), very **efficient**, and **regulated**.
>- Are, with a few exceptions, **proteins** (the exceptions are catalytic RNAs, ribozymes).
>  
>**IMPORTANT:**
>- Enzymes do **NOT** change $\Delta G$ or the **equilibrium** ($K'_{eq}$). They only help reach it faster, in both directions.

## Active site and substrate binding

>[!info] **Substrate** 
>Molecule the enzyme acts on. It binds in a pocket called the **active site**.

$$\text{Enzyme} + \text{Substrate} \rightarrow \text{Enzyme-Substrate complex}  \rightarrow \text{Enzyme} + \text{Product (breakdown of the Substrate)}.$$

| Model                            | How it works                                                                                   |
| -------------------------------- | ---------------------------------------------------------------------------------------------- |
| **Lock-and-key**                 | The active site already has the exact shape of the substrate (rigid).                          |
| **Induced fit** (more acceptive) | The active site is flexible and **changes shape** when the substrate binds, to fit it tightly. |

## How enzymes lower the activation energy

1. **Orientation**: binds two substrates and holds them in the perfect position to react.
2. **Electronic effects**: binding rearranges electrons in the substrate, creating partial $+$ and $−$ charges that favor the reaction.
3. **Strain**: the enzyme bends/stretches the bound substrate toward the **transition state**.

## Cofactors and coenzymes

>[!info] **Cofactor** 
>Non-protein "helper" required for enzyme activity. Two kinds:
>- **Inorganic ions**
>- **Coenzymes**: complex organic molecules, mostly derived from **vitamins**.
>
>A coenzyme that is tightly or even covalently bound is termed a **prosthetic group**.

Coenzymes are transient carriers of specific atoms/groups:

| Coenzyme               | Group transferred       | Vitamin/precursor    |
| ---------------------- | ----------------------- | -------------------- |
| Biocytin               | $CO_2$                  | Biotin               |
| Coenzyme A             | acyl groups             | Pantothenic acid     |
| Coenzyme B$_{12}$      | H atoms, alkyl groups   | Vitamin B$_{12}$     |
| FAD                    | electrons               | Riboflavin (B$_{2}$) |
| Lipoate                | electrons + acyl groups | not required in diet |
| **NAD**                | hydride ion ($:H^-$)    | Niacin               |
| Pyridoxal phosphate    | amino groups            | Pyridoxine (B$_{6}$) |
| Tetrahydrofolate       | one-carbon groups       | Folate               |
| Thiamine pyrophosphate | aldehydes               | Thiamine (B$_{1}$)   |

---
# Enzyme kinetics and inhibition

## Substrate concentration and rate

Like we've seen before, the reaction is: 
$$E + S \longrightarrow ES \longrightarrow E + P$$

- Measure the **initial velocity (V0)**: the speed at the very start, before substrate is used up.
- Plot $V_0$ vs $[S]$ $\longrightarrow$ **hyperbolic curve** (for normal enzymes).
    - **Low $[S]$**: many free enzymes, rate grows almost linearly with $[S]$.
    - **High $[S]$**: all enzyme molecules are busy (**saturated**) $\implies$ rate reaches a plateau = $V_{max}$.
## ==Michaelis-Menten equation==

$$V = \frac{V_{max}*[S]}{K_m + [S]}$$

- **V$_{max}$**: maximum rate of the system, reached at saturating $[S]$.
- **K$_m$** (Michaelis constant): the $[S]$ at which
$$V = \tfrac12 V_{max}$$ 
	==It is numerically equal to the substrate concentration at which the reaction rate is half of Vmax.==
	
>[!note] Remember
>- Low $K_m \ \implies$ enzyme reaches half-speed at low $[S] \ \implies$**high affinity** for the substrate. 
>- High $K_m \implies$ low affinity.

## Lineweaver-Burk (double reciprocal) plot

Take the reciprocal of both sides to get a straight line: $$\frac{1}{V} = \frac{K_m}{V_{max}}\cdot\frac{1}{[S]} + \frac{1}{V_{max}}$$
![[Pasted image 20261003110946.png|443]]

A straight line is easier to read than a curve and it makes the effect of inhibitors visually obvious.

## Reversible inhibitors

Regulation by controlling enzyme kinetics:

- **Competitive Inhibition**:
  A molecule that resembles the normal substrate binds to the enzyme and prevents the substrate from binding.
  Add more substrate and it outcompetes the inhibitor. 
  $V_{max}$ stays the same, but you need more $[S]$ to reach $K_m$.
- **Non-competitive Inhibition**:
  A molecule binds tot he enzyme in a non-active site, hampering substrate transformation.
  $V_{max}$ is lower, but affinity of the working enzymes ($K_m$) is unchanged.
- **Un-competitive Inhibition**:
  A molecule binds near to the active site **after** the binding of the substrate and blocks it in the catalytic site.
  Basically, the inhibitor locks the substrate in the $ES$ complex, pulling the equilibrium toward $ES$ (apparent $K_m$ down) but nothing is released as product ($V_{max}$ down).

|                                        | **Competitive**                       | **Non-competitive**                           | **Un-competitive**                                              |
| -------------------------------------- | ------------------------------------- | --------------------------------------------- | --------------------------------------------------------------- |
| **Binds to**                           | Active site (resembles the substrate) | Different site than active site ($E$ or $ES$) | Only the $ES$ complex (near active site, after substrate binds) |
| **Effect on $V_{max}$**                | Unchanged                             | Decreases                                     | Decreases                                                       |
| **Effect on $K_m$**                    | Increases (apparent)                  | Unchanged                                     | Decreases                                                       |
| **Can be overcome by more substrate?** | Yes                                   | No                                            | No                                                              |
| **Lineweaver-Burk plot**               | Lines cross on the y-axis             | Lines cross on the x-axis                     | Parallel lines                                                  |

---
# Enzyme regulation

> [!abstract] Why regulate? 
> If all enzymes ran at full speed all the time, the cell would waste energy and make things it doesn't need. 
> Cells control **how many** enzymes there are and **how active** they are.

## Map of control mechanisms

```
Control mechanisms
├── Gene expression ........... controls enzyme PRODUCTION (how much enzyme exists)
└── Enzyme ACTIVITY
    ├── Covalent modification ........ enzyme ON or OFF
    ├── Allosteric regulation ........ controls enzyme KINETICS
    ├── Protein–protein interaction .. enzyme ON or OFF
    └── (Inhibitors) ................. see [[03 - Enzyme Kinetics and Inhibition]]
```

## 1. Allosteric regulation

Allosteric enzymes are made of **several polypeptide subunits**.
Each enzyme exists in an **active form** and an **inactive form** that oscillate (in equilibrium).

- Besides the active site, they have **regulatory sites** where effectors bind:
    - **Activator** binds $\rightarrow$ **stabilizes the active form** $\rightarrow$ curve shifts left (works at lower $[S]$).
    - **Inhibitor** binds $\rightarrow$ **stabilizes the inactive form** $\rightarrow$ curve shifts right.

>[!info] **Cooperativity**: 
>Binding of substrate to one subunit makes the neighbours more active ("each polypeptide can amplify the activity of the neighbour").

>[!warning] Feedback in metabolic pathways
>- **Negative feedback**: a final product **inhibits the first enzyme** of a pathway.
>	When there is enough D, the pathway slows down. Most common.
>- **Positive feedback**: a product **activates** the pathway.

## 2. Protein–protein interactions

>[!info] P-P interactions:
>A **regulatory protein** binds to an enzyme to induce a shape change that switches its catalytic activity on or off.

For example:
**PKA = cAMP-dependent protein kinase A.**

1. Inactive PKA = 
	- 2 **regulatory (R)** subunits 
	  \+ 
	- 2 **catalytic (C)** subunits stuck together.
2. **cAMP** (allosteric regulator) binds the R subunits (cAMP is an allosteric regulator).
3. Conformational change → the complex **dissociates**.
4. **Free C subunits are active protein kinases** (they phosphorylate other proteins).

## 3. Covalent modifications

A chemical group is **covalently attached** to the enzyme, switching it on (or off, depending on the enzyme).

|Modification|Group added|
|---|---|
|Phosphorylation|phosphate (by kinases; very common, uses ATP)|
|Adenylation|adenyl group (AMP)|
|Uridylylation|uridine (UMP)|
|ADP-ribosylation|ADP-ribose|
|Methylation|CH3|

---
# Temperature and extremophiles

## Temperature and enzyme activity

- **Low T**: slow, few collisions between enzyme and substrate.
- **Rising T**: more heat energy $\implies$ more collisions $\implies$ faster rate.
- **Optimum**: humans $\approx 37 °C$.
- **Too high**: the protein **denatures** (loses its 3D shape, including the active site) $\implies$ rate falls rapidly.

The plotted curve is a bell-shaped / asymmetric (slow rise, sharp drop).

## 2. Life in extreme environments (growth rate $vs$ T)

|Group|Temperature preference|
|---|---|
|**Psychrophiles** (cryophiles)|cold: about −20 to +10 °C (polar regions, deep sea)|
|Psychrotrophs|tolerate cold but grow best at moderate T|
|**Mesophiles**|moderate, around 20–45 °C (humans, most animals)|
|**Thermophiles**|> 45 °C|
|**Hyperthermophiles**|very hot, up to > 100 °C|

## Taq polymerase and PCR

**Taq polymerase** is a **thermostable DNA polymerase** from _Thermus aquaticus_ (isolated by Chien et al., 1976).

- It is used in **PCR (polymerase chain reaction)**.
	PCR cycles repeatedly heat DNA to $\sim 95 °C$ to separate the strands; normal enzymes would denature, Taq survives and doesn't need to be replaced at every cycle.
