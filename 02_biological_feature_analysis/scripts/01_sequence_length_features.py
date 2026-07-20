import pandas as pd


input_file = "../data/input/protein_mrna_merged_final.tsv"
output_file = "../results/01_length_features.tsv"


df = pd.read_csv(
    input_file,
    sep="\t"
)


print("Calculating length features...")


df["Protein_Length"] = (
    df["Protein_Sequence"]
    .fillna("")
    .apply(len)
)


df["Codon_Count"] = (
    pd.to_numeric(
        df["CDS_length"],
        errors="coerce"
    )
    // 3
)


df.to_csv(
    output_file,
    sep="\t",
    index=False
)


print("Saved:", output_file)
