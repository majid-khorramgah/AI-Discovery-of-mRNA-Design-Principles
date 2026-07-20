import pandas as pd
import math
import os
from collections import defaultdict


# ==============================
# Paths
# ==============================

input_file = "../results/03_codon_features.tsv"

codon_reference = "../references/human_codon_usage.tsv"

output_file = "../results/04_cai_features.tsv"


# ==============================
# Genetic code
# ==============================

codon_table = {

'UUU':'F','UUC':'F','UUA':'L','UUG':'L',
'UCU':'S','UCC':'S','UCA':'S','UCG':'S',
'UAU':'Y','UAC':'Y','UAA':'*','UAG':'*',
'UGU':'C','UGC':'C','UGA':'*','UGG':'W',

'CUU':'L','CUC':'L','CUA':'L','CUG':'L',
'CCU':'P','CCC':'P','CCA':'P','CCG':'P',
'CAU':'H','CAC':'H','CAA':'Q','CAG':'Q',
'CGU':'R','CGC':'R','CGA':'R','CGG':'R',

'AUU':'I','AUC':'I','AUA':'I','AUG':'M',
'ACU':'T','ACC':'T','ACA':'T','ACG':'T',
'AAU':'N','AAC':'N','AAA':'K','AAG':'K',
'AGU':'S','AGC':'S','AGA':'R','AGG':'R',

'GUU':'V','GUC':'V','GUA':'V','GUG':'V',
'GCU':'A','GCC':'A','GCA':'A','GCG':'A',
'GAU':'D','GAC':'D','GAA':'E','GAG':'E',
'GGU':'G','GGC':'G','GGA':'G','GGG':'G'

}


# ==============================
# Load codon usage
# ==============================

print("Loading codon reference...")


codon_usage = pd.read_csv(
    codon_reference,
    sep="\t"
)


# make dictionary

freq = dict(
    zip(
        codon_usage["Codon"],
        codon_usage["Frequency"]
    )
)



# ==============================
# Calculate Relative Adaptiveness
# ==============================


aa_codons = defaultdict(list)


for codon, aa in codon_table.items():

    if aa != "*":
        aa_codons[aa].append(codon)



weights = {}


for aa,codons in aa_codons.items():

    max_freq = max(
        freq.get(c,0)
        for c in codons
    )

    for c in codons:

        if max_freq == 0:
            weights[c]=0

        else:
            weights[c] = (
                freq.get(c,0)
                /
                max_freq
            )



# ==============================
# CAI Function
# ==============================


def calculate_cai(sequence):

    if pd.isna(sequence):
        return None


    sequence = sequence.upper()


    codons=[]


    for i in range(0,len(sequence)-2,3):

        codons.append(
            sequence[i:i+3]
        )


    logs=[]


    for c in codons:

        if c in weights:

            w=weights[c]


            if w>0:

                logs.append(
                    math.log(w)
                )


    if len(logs)==0:
        return 0


    cai = math.exp(
        sum(logs)
        /
        len(logs)
    )


    return round(cai,4)



# ==============================
# Load Dataset
# ==============================


print("Loading dataset...")


df=pd.read_csv(
    input_file,
    sep="\t"
)


print(
    "Rows:",
    len(df)
)



# ==============================
# Calculate
# ==============================


print("Calculating CAI...")


df["CAI"] = (
    df["mRNA_Sequence"]
    .apply(calculate_cai)
)



# ==============================
# Save
# ==============================


os.makedirs(
    "../results",
    exist_ok=True
)


df.to_csv(
    output_file,
    sep="\t",
    index=False
)



print("==========================")
print("Finished")
print("==========================")

print(
    df["CAI"].describe()
)


print(
    "Saved:",
    output_file
)
