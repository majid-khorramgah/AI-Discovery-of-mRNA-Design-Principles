import pandas as pd
import os


# ==========================
# Paths
# ==========================

input_file = "../results/07_complexity_features.tsv"

output_file = "../results/feature_correlation.csv"



# ==========================
# Load dataset
# ==========================


print("Loading dataset...")


df = pd.read_csv(
    input_file,
    sep="\t"
)



# ==========================
# Numeric features
# ==========================


numeric_df = df.select_dtypes(
    include=["int64","float64"]
)



# ==========================
# Correlation
# ==========================


correlation = numeric_df.corr(
    method="pearson"
)



# ==========================
# Save
# ==========================


correlation.to_csv(
    output_file
)



print("====================")
print("Correlation finished")
print("====================")


print(
    correlation
)


print(
    "Saved:",
    output_file
)
