# Biological Feature Analysis

## Overview

This phase transforms raw human protein-mRNA sequences into a comprehensive biological feature representation for AI-driven discovery of mRNA design principles.

The objective is not only to predict mRNA properties, but also to discover hidden biological patterns and sequence-level rules that influence mRNA stability, translation efficiency, and molecular behavior.

The extracted biological representation will be used for explainable AI models and biological rule discovery in later phases.

---

# Input Dataset

The analysis is performed on a human protein-mRNA paired dataset.

## Dataset Information

- Species: Homo sapiens
- Number of protein-mRNA pairs: 19,037

## Data Sources

- UniProt Human Proteome
- NCBI RefSeq Transcript Database


## Input Information

Each sample contains:

- Protein sequence
- mRNA sequence
- Gene information
- Transcript information
- CDS length
- mRNA length


---

# Feature Extraction Pipeline


The complete workflow:

```
Protein-mRNA Dataset

        ↓

Sequence Feature Extraction

        ↓

Biological Feature Representation

        ↓

AI-based Biological Rule Discovery
```


---

# Extracted Features


## 1. Sequence Length Features

Script:

```
01_sequence_length_features.py
```


Generated features:

- Protein_Length
- Codon_Count
- CDS_length
- mRNA_length


These features describe basic structural properties of protein-coding transcripts.



---

# 2. Nucleotide Composition Features

Script:

```
02_gc_content_analysis.py
```


Generated features:

- GC_Content
- A_Content
- U_Content
- G_Content
- C_Content


These features capture nucleotide-level composition patterns associated with RNA stability and evolutionary constraints.



---

# 3. Codon Usage Features

Script:

```
03_codon_usage_analysis.py
```


Generated feature:

- Codon_Usage_Profile


This captures synonymous codon selection patterns in natural human mRNA sequences.

Codon usage provides information about evolutionary optimization and translation preferences.



---

# 4. Codon Adaptation Index (CAI)

Script:

```
04_calculate_cai.py
```


Generated feature:

- CAI


CAI estimates how well the codon usage of an mRNA sequence matches preferred codon usage patterns.


Current pipeline includes CAI integration structure.

Human codon reference optimization tables will be integrated in future updates.



---

# 5. RNA Folding and Structural Features

Script:

```
05_rna_structure_prediction.py
```


Tool:

ViennaRNA


Generated features:

- RNA_Secondary_Structure
- MFE (Minimum Free Energy)


These features represent RNA folding behavior and structural stability.


MFE provides a thermodynamic estimation of RNA secondary structure stability.



---

# 6. Translation-related Features

Script:

```
07_translation_features.py
```


Generated features:

- Codon_Pair_Profile
- Rare_Codon_Frequency


These features capture translation-related sequence patterns beyond individual codon frequencies.


They describe how codon combinations and rare codon usage may influence translation efficiency.



---

# 7. Sequence Complexity Features

Script:

```
08_sequence_complexity_features.py
```


Generated features:

- Shannon_Entropy
- GC3_Content
- CpG_Frequency
- Dinucleotide_Profile


These features describe:

- Sequence diversity
- Evolutionary constraints
- Nucleotide organization
- Hidden compositional patterns


---

# Final Feature Dataset


The final generated dataset:

```
protein_mrna_features.tsv
```


contains:


## Original Biological Information

- Entry
- Entry_Name
- Protein_Name
- Gene_Name
- Protein_Sequence
- mRNA_Sequence
- Transcript information
- CDS_length
- mRNA_length



## Sequence Features

- Protein_Length
- Codon_Count



## Nucleotide Composition Features

- GC_Content
- A_Content
- U_Content
- G_Content
- C_Content



## Codon Features

- Codon_Usage_Profile
- Codon_Pair_Profile
- Rare_Codon_Frequency
- CAI



## RNA Structural Features

- RNA_Secondary_Structure
- MFE



## Sequence Complexity Features

- Shannon_Entropy
- GC3_Content
- CpG_Frequency
- Dinucleotide_Profile



---

# Large Dataset Download


Due to GitHub file size limitations, the complete feature dataset is hosted externally.


Download:


https://drive.google.com/file/d/1uoq6L2VbdPBWOxdaZ_-3umMgO-vycj_z/view?usp=sharing


After downloading, place the file:


```
protein_mrna_features.tsv
```


inside:


```
data/processed/
```



---

# Software Requirements


Main dependencies:


- Python 3.x
- pandas
- Biopython
- ViennaRNA
- tqdm


Installation:


```
pip install -r requirements.txt
```



---

# Pipeline Execution


Run the complete feature extraction pipeline:


```
python 06_feature_pipeline.py
```


The pipeline executes:


```
Sequence Features

        ↓

Nucleotide Composition

        ↓

Codon Usage

        ↓

CAI Calculation

        ↓

RNA Folding

        ↓

Translation Features

        ↓

Sequence Complexity Features
```



---

# Research Goal


The purpose of this phase is to create a biological representation space where AI models can identify hidden principles governing natural mRNA design.


Main research questions:


- Do natural human mRNA sequences contain hidden design principles?

- Which sequence properties contribute most to RNA stability?

- Which features influence translation efficiency?

- Can AI discover interpretable biological rules from naturally evolved mRNA sequences?



---

# Next Phase


## Phase 03: Biological Rule Discovery


The next phase focuses on:


- Feature correlation analysis

- Biological pattern discovery

- Clustering natural mRNA strategies

- Identifying relationships between sequence features and biological properties

- Developing interpretable biological hypotheses


The final objective is to move from:

```
Sequence Optimization
```

towards:

```
Understanding Biological Design Principles
```
