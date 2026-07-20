import pandas as pd


file = "protein_mrna_merged.tsv"


df = pd.read_csv(
    file,
    sep="\t"
)


valid_aa = set(
    "ACDEFGHIKLMNPQRSTVWY"
)


def find_error(seq):

    if pd.isna(seq):
        return ""

    errors = set(seq) - valid_aa

    return "".join(errors)



df["invalid_characters"] = (
    df["Protein_Sequence"]
    .apply(find_error)
)


errors = df[
    df["invalid_characters"] != ""
]


print(errors[
    [
        "Entry",
        "Protein_Name",
        "invalid_characters"
    ]
])


errors.to_csv(
    "../results/protein_sequence_errors.csv",
    index=False
)


print(
    "Saved error report"
)
