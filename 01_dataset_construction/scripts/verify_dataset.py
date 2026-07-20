import pandas as pd
import os


input_file = "../data/processed/protein_mrna_merged.tsv"


print("="*60)
print("Dataset Quality Control")
print("="*60)


# Load

df = pd.read_csv(
    input_file,
    sep="\t"
)


print("\nDataset size:")
print(df.shape)


print("\nColumns:")
for c in df.columns:
    print("-", c)



# Missing values

print("\nMissing values:")
missing = df.isnull().sum()

print(
    missing[missing > 0]
)



# Duplicate entries

print("\nDuplicate Entry IDs:")

duplicates = df[
    df.duplicated(
        subset=["Entry"],
        keep=False
    )
]


print(
    len(duplicates)
)



# Protein validation

valid_aa = set(
    "ACDEFGHIKLMNPQRSTVWY"
)


def check_protein(seq):

    if pd.isna(seq):
        return False

    return set(seq).issubset(valid_aa)



df["protein_valid"] = (
    df["Protein_Sequence"]
    .apply(check_protein)
)



# mRNA validation

valid_rna = set("AUGC")


def check_mrna(seq):

    if pd.isna(seq):
        return False

    return set(seq).issubset(valid_rna)



df["mrna_valid"] = (
    df["mRNA_Sequence"]
    .apply(check_mrna)
)



print("\nProtein sequence errors:")
print(
    (~df.protein_valid).sum()
)


print("\nmRNA sequence errors:")
print(
    (~df.mrna_valid).sum()
)



# Length check

print("\nLength statistics")

print(
    df[
        [
        "CDS_length",
        "mRNA_length"
        ]
    ]
    .describe()
)


print("\nQC Completed Successfully")
