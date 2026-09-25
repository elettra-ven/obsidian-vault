Modelling based on **schema-on-read** paradigm:
>Data is written in its raw format (as-is) and structure is imposed only when a **reading** operation occurs.

![[img/Pasted image 20260923110522.png]]

A data lake should NOT turn into a **Data Swamp**:

>[!note] Data Swamp
>Write-only dump with no structure (zones, catalogue, ownership, etc ...)
>Extractions are difficult and unthrustwothy.

## ETL

The pipeline for Data Lakes is described as:
1. **Ingestion**
2. **Storage**
3. **Processing**

### 1. Ingestion
Data must be monitored, validated and secured on ingress. 
These operation are handled during the ingestion process through a decoupling and a distinction of the data that allows it to find its own source.

It can be **batch** ingestion or **streaming** ingestion.

### 2. Storage
Raw storage but cleaned and curated zone patterns are applied.

### 3. Processing
Contrary to ETL transformations, that transform before loading, lake-centric pipeline often operate the **loading first** and only **then transform** the data, **on demand**.


