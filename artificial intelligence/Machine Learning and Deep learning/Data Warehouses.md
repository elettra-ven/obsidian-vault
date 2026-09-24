Data warehouses are useful when data is already clean, conformed and aggregated.
It's a good fit for features that are naturally roll-up style, but it performs poorly for raw and event-level data.
## OLTP $vs$ OLAP

![[Pasted image 20260923094355.png|508]]

## ETL process

![[Pasted image 20260923095603.png|508]]

>[!info] Extraction & Loading
 can be a **Snapshot** or an **incremental** extraction (occurs every time the data is changed). 
 >
>**Loading** can also be done on **full load** or **incrementally**.

The system must be able to pull from multiple, different sources (OLTPs).

>[!info] Transform
>Operations such as **cleaning**, **conforming**, deduplication, etc ...

The system must follow the defined business rules. In order to do so data must be frequently checked and maintained.

---

# The Dimensional Fact Model
The warehouses is deliberately **denormalized** into a specific model called **Dimensional Fact Model** (DFM).
This new shape is more intuitive and more useful for human queries.

The model is divided different tables and elements:

>[!info] Facts
>This table represents data obtained from an **analysis** of the business process.

>[!info] Measures
>It represents the numeric value to **aggregate**.
>The measure can be:
>- **additive**: summable across every dimension (quantity, revenue) 
>- **semi-additive**: summable across some dimensions, not time (inventory level)
>- **non-additive**: never meaningfully summed (unit price, ratios)

>[!info] Dimension
>This table describes the context of the data.
>The description are often denormalized into a *flattened* structure for query semplicity.

Dimensions are organized with a hierarchical system for the descriptive attributes:
![[Pasted image 20260923100547.png|339]]

### "Grain"
Is the representation of a single row of the **facts** table.


![[Pasted image 20260923102551.png|497]]
- *Star Schema*

>[!note] Example
>**In order to answer the question: "which product categories get returned most, by region and quarter?"
>
>Which should the grain of the *Star Schema* be?**
>
>The finer the grain is, the more versatile it is.
>A good grain would be **quantity**, **category**, **region**, **quarter**.
>
>**What should the measures of the *Star Schema* be?**
>An appropriate aggregate value would be **quantity**. In this case it would be an **additive measure**.
>Attributes like *time* or *category* are dimensions, and NOT measures.
>
>**What should the dimensions of the *Star Schema* be?**
>Time, product, store, customer is the finer grain we can achieve with this Schema.

# Data Cube
![[Pasted image 20260923104059.png|344]]
## Operations
- Slicing
- Dicing
- Roll-up
- Drill-down
- Pivot

#### Slicing and Dicing
The dimension of the cube is the number of **dimensions** (it's an hypercube).
- The cube can be "**sliced**" over a certain dimension to address a specific smaller cube, that contains the measures we're interested in.
- Slices for every dimension in the cube can form a **dice**: a smaller cube inside the original dimensional space.

#### Roll-up and Drill-down
**Rolling-up** and **drilling-down** are opposite operations that, respectively, aggregate to an upper-level and go deeper on a more specific level.

#### Pivot (or rotation)
Swaps columns and rows within a certain table. The data remains the same.

