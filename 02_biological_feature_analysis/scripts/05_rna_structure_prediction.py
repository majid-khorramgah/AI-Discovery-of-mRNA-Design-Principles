import pandas as pd
import RNA


input_file="../results/04_cai_features.tsv"

output_file="../results/05_rna_structure.tsv"



df=pd.read_csv(
    input_file,
    sep="\t"
)



def fold(seq):

    structure,mfe = RNA.fold(
        str(seq)
    )

    return pd.Series({

        "RNA_Secondary_Structure":
        structure,

        "MFE":
        round(mfe,3)

    })



result = (
    df["mRNA_Sequence"]
    .apply(fold)
)



df=pd.concat(
    [df,result],
    axis=1
)


df.to_csv(
    output_file,
    sep="\t",
    index=False
)


print("RNA folding completed")
