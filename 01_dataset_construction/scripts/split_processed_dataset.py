import pandas as pd
import os


# Input merged dataset
input_file = "protein_mrna_merged.tsv"


# Output directory
output_dir = "../data/processed"

os.makedirs(output_dir, exist_ok=True)


# Number of rows per file
chunksize = 7000


for i, chunk in enumerate(
        pd.read_csv(
            input_file,
            sep="\t",
            chunksize=chunksize
        )
):

    output_file = os.path.join(
        output_dir,
        f"protein_mrna_merged_part_{i+1:02d}.tsv"
    )


    chunk.to_csv(
        output_file,
        sep="\t",
        index=False
    )


    print(
        f"Saved {output_file}: {len(chunk)} rows"
    )


print("\nProcessed dataset splitting completed!")
