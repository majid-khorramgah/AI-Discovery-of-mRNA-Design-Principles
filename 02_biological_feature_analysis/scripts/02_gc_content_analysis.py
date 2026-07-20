import pandas as pd


input_file = "../results/01_length_features.tsv"

output_file = "../results/02_gc_features.tsv"



df = pd.read_csv(
    input_file,
    sep="\t"
)



def nucleotide_features(seq):

    seq = str(seq).upper()

    length = len(seq)

    return pd.Series({

        "GC_Content":
        round(
            (seq.count("G")+seq.count("C"))
            /length*100,
            3
        ),

        "A_Content":
        round(seq.count("A")/length*100,3),

        "U_Content":
        round(seq.count("U")/length*100,3),

        "G_Content":
        round(seq.count("G")/length*100,3),

        "C_Content":
        round(seq.count("C")/length*100,3)

    })



features = (
    df["mRNA_Sequence"]
    .apply(nucleotide_features)
)



df = pd.concat(
    [df,features],
    axis=1
)


df.to_csv(
    output_file,
    sep="\t",
    index=False
)


print("GC features completed")
