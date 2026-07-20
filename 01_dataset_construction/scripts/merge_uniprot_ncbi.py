import pandas as pd
from pathlib import Path


# ===============================
# Paths
# ===============================

folder = Path(r"D:\1405\mrna\makh")

uniprot_file = folder / "uniprot.tsv"
mrna_file = folder / "protein_mRNA_final.tsv"

output_file = folder / "protein_mrna_merged_final.tsv"


# ===============================
# Load files
# ===============================

print("Loading UniProt...")

uniprot = pd.read_csv(
    uniprot_file,
    sep="\t",
    dtype=str,
    low_memory=False
)

print("UniProt rows:", len(uniprot))


print("Loading mRNA dataset...")

mrna = pd.read_csv(
    mrna_file,
    sep="\t",
    dtype=str,
    low_memory=False
)

print("mRNA rows:", len(mrna))


# ===============================
# Rename UniProt columns
# ===============================

uniprot = uniprot.rename(columns={

    "Entry Name": "Entry_Name",
    "Protein names": "Protein_Name",
    "Gene Names": "Gene_Name",

    "Sequence": "Protein_Sequence",

    "RefSeq": "RefSeq_Protein",
    "Ensembl": "Ensembl_ID",
    "MANE-Select": "MANE_Transcript"

})


# ===============================
# Rename NCBI columns
# ===============================

mrna = mrna.rename(columns={

    "Protein": "Protein_Accession",
    "Transcript": "Transcript_ID",
    "mRNA": "mRNA_Sequence"

})


# ===============================
# Clean RefSeq
# ===============================

# UniProt RefSeq sometimes:
# NP_xxxxx.1; NP_xxxxx.2;

uniprot["RefSeq_Protein_clean"] = (
    uniprot["RefSeq_Protein"]
    .fillna("")
    .str.split(";")
    .str[0]
    .str.strip()
)


# ===============================
# Merge
# ===============================

print("Merging...")

merged = pd.merge(

    uniprot,

    mrna,

    left_on="RefSeq_Protein_clean",

    right_on="Protein_Accession",

    how="inner",

    suffixes=("_uniprot", "_ncbi")

)


print("Merged rows:", len(merged))


# ===============================
# Fix Entry column
# ===============================

if "Entry_uniprot" in merged.columns:

    merged = merged.rename(
        columns={
            "Entry_uniprot": "Entry"
        }
    )

elif "Entry_x" in merged.columns:

    merged = merged.rename(
        columns={
            "Entry_x": "Entry"
        }
    )


# ===============================
# Select final columns
# ===============================

final_columns = [

    # Protein information
    "Entry",
    "Entry_Name",
    "Protein_Name",
    "Gene_Name",
    "Protein_Sequence",

    # IDs
    "RefSeq_Protein",
    "Ensembl_ID",
    "MANE_Transcript",

    # NCBI information
    "Transcript_ID",
    "Protein_Accession",

    # mRNA information
    "CDS_length",
    "mRNA_length",
    "mRNA_Sequence"

]


# only existing columns

final_columns = [
    c for c in final_columns
    if c in merged.columns
]


final = merged[final_columns].copy()


# ===============================
# Remove duplicates
# ===============================

print("Removing duplicates...")

if "Entry" in final.columns and "Transcript_ID" in final.columns:

    final = final.drop_duplicates(
        subset=[
            "Entry",
            "Transcript_ID"
        ],
        keep="first"
    )


# ===============================
# Statistics
# ===============================

print("==============================")
print("Final rows:", len(final))
print("Columns:")
print(list(final.columns))


print("\nDuplicate check:")

print(
    final["Entry"]
    .value_counts()
    .head(10)
)


# ===============================
# Save
# ===============================

final.to_csv(

    output_file,

    sep="\t",

    index=False,

    encoding="utf-8"

)


print("==============================")
print("DONE")
print("Saved:")
print(output_file)
