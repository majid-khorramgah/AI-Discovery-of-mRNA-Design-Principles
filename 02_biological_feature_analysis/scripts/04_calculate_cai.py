import pandas as pd


input_file="../results/03_codon_features.tsv"

output_file="../results/04_cai_features.tsv"


df=pd.read_csv(
    input_file,
    sep="\t"
)


# TODO:
# Human codon reference table


df["CAI"] = None



df.to_csv(
    output_file,
    sep="\t",
    index=False
)

print("CAI pipeline ready")
