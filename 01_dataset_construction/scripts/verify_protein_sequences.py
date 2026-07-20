import pandas as pd
import os


# ===============================
# Input dataset
# ===============================

input_file = "protein_mrna_merged_final.tsv"


# Output directory

output_dir = "../results"

os.makedirs(
    output_dir,
    exist_ok=True
)


output_file = os.path.join(
    output_dir,
    "protein_sequence_errors.csv"
)



# ===============================
# Load dataset
# ===============================

print("Loading dataset...")

df = pd.read_csv(
    input_file,
    sep="\t"
)


print(f"Total sequences checked: {len(df)}")



# ===============================
# Valid amino acids
# ===============================

# Standard amino acids + Selenocysteine (U)

valid_aa = set(
    "ACDEFGHIKLMNPQRSTVWYU"
)



# ===============================
# Sequence validation
# ===============================

def find_error(seq):

    if pd.isna(seq):
        return "Missing"

    invalid = set(seq) - valid_aa

    return "".join(sorted(invalid))



df["invalid_characters"] = (
    df["Protein_Sequence"]
    .apply(find_error)
)



# ===============================
# Extract invalid sequences
# ===============================

errors = df[
    df["invalid_characters"] != ""
]



# ===============================
# Report
# ===============================

print("\n================================")
print("Protein Sequence Validation")
print("================================")


print(
    f"Invalid sequences: {len(errors)}"
)



if len(errors) > 0:

    print("\nInvalid examples:")

    print(
        errors[
            [
                "Entry",
                "Protein_Name",
                "invalid_characters"
            ]
        ].head(20)
    )


    errors[
        [
            "Entry",
            "Protein_Name",
            "Protein_Sequence",
            "invalid_characters"
        ]
    ].to_csv(
        output_file,
        index=False
    )


    print(
        f"\nError report saved:"
        f" {output_file}"
    )


else:

    print(
        "All protein sequences passed validation."
    )


print("\nQC completed successfully.")
