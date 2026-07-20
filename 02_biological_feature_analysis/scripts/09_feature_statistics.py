import pandas as pd
import os


# ==========================
# Paths
# ==========================

input_file = "../results/07_complexity_features.tsv"

output_file = "../results/feature_statistics.csv"



# ==========================
# Load dataset
# ==========================

print("Loading dataset...")


df = pd.read_csv(
    input_file,
    sep="\t"
)


print("Rows:", len(df))
print("Columns:", len(df.columns))



# ==========================
# Select numeric features
# ==========================

numeric_df = df.select_dtypes(
    include=["int64","float64"]
)



print(
    "Numeric features:",
    len(numeric_df.columns)
)



# ==========================
# Statistics
# ==========================

stats = pd.DataFrame({

    "Mean": numeric_df.mean(),

    "Median": numeric_df.median(),

    "Std": numeric_df.std(),

    "Min": numeric_df.min(),

    "Max": numeric_df.max(),

    "Missing": numeric_df.isna().sum()

})


# transpose

stats = stats.T



# save

os.makedirs(
    "../results",
    exist_ok=True
)


stats.to_csv(
    output_file
)



print("====================")
print("Statistics finished")
print("====================")


print(
    stats
)


print(
    "Saved:",
    output_file
)
