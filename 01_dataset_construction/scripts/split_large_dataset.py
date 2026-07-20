import pandas as pd
import os


input_file = "ncbi_mrna.tsv"

output_dir = "data/raw"

os.makedirs(output_dir, exist_ok=True)


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
        f"ncbi_mrna_part_{i+1:02d}.tsv"
    )

    chunk.to_csv(
        output_file,
        sep="\t",
        index=False
    )

    print(
        f"Saved {output_file}: {len(chunk)} rows"
    )


print("Dataset splitting completed.")
