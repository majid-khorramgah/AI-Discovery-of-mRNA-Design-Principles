import pandas as pd
import math
from collections import Counter


input_file = "../results/06_translation_features.tsv"

output_file = "../results/protein_mrna_features_final.tsv"



df=pd.read_csv(
    input_file,
    sep="\t"
)



# -----------------------------
# Shannon entropy
# -----------------------------

def shannon_entropy(seq):

    seq=str(seq)

    counts=Counter(seq)

    total=len(seq)


    entropy=0


    for c in counts.values():

        p=c/total

        entropy -= p*math.log2(p)


    return round(entropy,4)



# -----------------------------
# GC3 content
# -----------------------------

def gc3_content(seq):

    codons=[
        seq[i:i+3]
        for i in range(0,len(seq)-2,3)
    ]


    third=[
        c[2]
        for c in codons
    ]


    if len(third)==0:
        return 0


    return round(
        (
        third.count("G")
        +
        third.count("C")
        )
        /
        len(third)
        *100,
        3
    )



# -----------------------------
# CpG frequency
# -----------------------------

def cpg_frequency(seq):

    seq=str(seq)

    return round(
        seq.count("CG")/
        len(seq),
        5
    )



# -----------------------------
# Dinucleotide profile
# -----------------------------

def dinucleotide_profile(seq):

    seq=str(seq)


    pairs=[
        seq[i:i+2]
        for i in range(len(seq)-1)
    ]


    return str(
        Counter(pairs)
    )



print("Calculating sequence complexity...")


df["Shannon_Entropy"] = (
    df["mRNA_Sequence"]
    .apply(shannon_entropy)
)


df["GC3_Content"] = (
    df["mRNA_Sequence"]
    .apply(gc3_content)
)


df["CpG_Frequency"] = (
    df["mRNA_Sequence"]
    .apply(cpg_frequency)
)


df["Dinucleotide_Profile"] = (
    df["mRNA_Sequence"]
    .apply(dinucleotide_profile)
)



df.to_csv(
    output_file,
    sep="\t",
    index=False
)


print("Final feature dataset saved")
