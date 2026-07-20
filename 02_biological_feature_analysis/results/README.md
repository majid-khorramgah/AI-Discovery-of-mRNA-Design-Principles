# Biological Feature Analysis Results

This directory contains all intermediate and final feature representations generated during the biological feature engineering phase of the project:

**AI Discovery of mRNA Design Principles**

The goal of this phase is to transform natural human mRNA sequences into a comprehensive biological representation containing:

- Sequence-level features
- Nucleotide composition features
- Codon usage patterns
- Codon adaptation metrics
- RNA structural properties
- Translation-related features
- Statistical summaries and correlations

All datasets are generated from the human protein-mRNA integrated dataset and are provided as intermediate checkpoints to ensure full reproducibility.

---

# Dataset Processing Pipeline

The feature generation workflow follows this order:

```
Raw Human Protein-mRNA Dataset

        |
        v

01 Sequence Length Features

        |
        v

02 GC Content Analysis

        |
        v

03 Codon Usage Analysis

        |
        v

04 Codon Adaptation Index (CAI)

        |
        v

05 RNA Secondary Structure Prediction

        |
        v

06 Translation Features

        |
        v

Feature Statistics & Correlation Analysis

        |
        v

Final Biological Feature Dataset
```

---

# Available Files

## 01_length_features.tsv

**Size:** 48.5 MB

Description:

Contains sequence length-related biological features.

Generated features include:

- Protein length
- mRNA length
- CDS length
- Codon count

Download:

https://drive.google.com/file/d/1AXtYvn5IIny8pxx0IS3I6o673hujEAuD/view?usp=sharing


---

## 02_gc_features.tsv

**Size:** 49.1 MB

Description:

Contains nucleotide composition features.

Features:

- GC Content
- A Content
- U Content
- G Content
- C Content


Download:

https://drive.google.com/file/d/16TYTaspgH5-gFxfbQbqABtV7fk_NPact/view?usp=sharing


---

## 03_codon_features.tsv

**Size:** 61.9 MB

Description:

Contains codon-level representation of human mRNA sequences.

Features:

- Codon usage profile
- Codon frequency distribution


Download:

https://drive.google.com/file/d/1ZC28X3PiMaWRkF72LLv1_mUGnk6cX7wB/view?usp=sharing


---

## 04_cai_features.tsv

**Size:** 62 MB

Description:

Contains Codon Adaptation Index (CAI) calculated using human codon usage preferences.

Reference:

human_codon_usage.tsv


Feature:

- CAI


Download:

https://drive.google.com/file/d/1vW19DeMj7DtiARelqvBO5PfZE46Q0CIW/view?usp=sharing


---

## 05_rna_structure.tsv

**Size:** 92.2 MB

Description:

Contains RNA structural properties predicted using ViennaRNA.

Features:

- RNA Secondary Structure
- Minimum Free Energy (MFE)


Download:

https://drive.google.com/file/d/1rzsY2lV7sNkr7HbhivQYmTqgK-BohIXg/view?usp=sharing


---

## 06_translation_features.tsv

**Size:** 214.4 MB

Description:

Contains translation-related biological features.

Features include:

- Codon pair information
- Rare codon statistics
- Translation-related sequence properties


Download:

https://drive.google.com/file/d/1k01vC-lM8OWZUkR5tV5TxJLRWBLapB26/view?usp=sharing


---

# Statistical Analysis Files


## feature_statistics.csv

**Size:** 1 KB

Description:

Summary statistics of extracted biological features.

Includes:

- Mean
- Median
- Standard deviation
- Minimum
- Maximum
- Missing values


Download:

https://drive.google.com/file/d/1vONkgzOo5syabD-6hgBaUippkUxRguj4/view?usp=sharing


---

## feature_correlation.csv

**Size:** 5 KB

Description:

Pairwise Pearson correlation analysis between biological features.

Used for:

- Discovering feature relationships
- Identifying biological dependencies
- Understanding mRNA design patterns


Download:

https://drive.google.com/file/d/1xJXkV_UNyYfh882TBm8aEgc75kN1a_jE/view?usp=sharing


---

# Reference Dataset


## human_codon_usage.tsv

**Size:** 783 bytes

Description:

Human codon frequency reference table used for CAI calculation.

Source:

Human codon usage database.


Download:

https://drive.google.com/file/d/19_IwseqkJfoLoEzGl1Dc_HMGUb7ucJTi/view?usp=sharing


---

# Final Integrated Dataset


## protein_mrna_features_final.tsv

**Size:** 218 MB

Description:

Complete integrated biological representation of human mRNA sequences.

Contains:

- Protein information
- mRNA sequences
- Length features
- Nucleotide composition
- Codon usage
- CAI
- RNA structural features
- Translation features


This dataset represents the final output of the biological feature engineering stage and serves as the input for downstream machine learning and biological rule discovery.


Download:

https://drive.google.com/file/d/1kqIE9jQLeyoAqpjIveexu0-tyqt67Rfj/view?usp=sharing


---

# Reproducibility

All datasets can be regenerated using the scripts provided in:

```
../scripts/
```

Pipeline scripts:

```
01_sequence_length_features.py

02_gc_content_analysis.py

03_codon_usage_analysis.py

04_calculate_cai.py

05_rna_structure_prediction.py

06_feature_pipeline.py
```

---

# Purpose in the Research Framework

These datasets provide the foundation for discovering hidden biological principles governing natural mRNA design.

The extracted representations will be used for:

- Biological rule discovery
- Explainable AI analysis
- Protein-to-mRNA relationship modeling
- Generative mRNA design
- Multi-objective optimization
