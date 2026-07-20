import pandas as pd
import json


input_file = "../results/02_gc_features.tsv"

output_file = "../results/03_codon_features.tsv"



df = pd.read_csv(
    input_file,
    sep="\t"
)



def codon_profile(seq):

    seq=str(seq)

    codons={}


    for i in range(0,len(seq)-2,3):

        codon=seq[i:i+3]

        codons[codon]=codons.get(codon,0)+1


    return json.dumps(codons)



df["Codon_Usage_Profile"] = (
    df["mRNA_Sequence"]
    .apply(codon_profile)
)



df.to_csv(
    output_file,
    sep="\t",
    index=False
)


print("Codon usage completed")
