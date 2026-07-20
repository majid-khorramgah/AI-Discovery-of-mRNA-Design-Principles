import pandas as pd
import json
from collections import Counter


input_file = "../results/05_rna_structure.tsv"

output_file = "../results/06_translation_features.tsv"



df = pd.read_csv(
    input_file,
    sep="\t"
)



# ---------------------------------
# Codon extraction
# ---------------------------------

def get_codons(seq):

    seq=str(seq)

    return [
        seq[i:i+3]
        for i in range(0,len(seq)-2,3)
    ]



# ---------------------------------
# Codon pair frequency
# ---------------------------------

def codon_pair_profile(seq):

    codons=get_codons(seq)

    pairs=[
        codons[i]+"-"+codons[i+1]
        for i in range(len(codons)-1)
    ]

    return json.dumps(
        dict(
            Counter(pairs)
        )
    )



# ---------------------------------
# Rare codon frequency
# ---------------------------------

def rare_codon_frequency(seq):

    codons=get_codons(seq)

    counts=Counter(codons)


    total=len(codons)


    if total==0:
        return 0


    # lower 10% frequency codons
    threshold=sorted(
        counts.values()
    )[max(0,int(len(counts)*0.1)-1)]


    rare=sum(
        c for c in counts.values()
        if c<=threshold
    )


    return round(
        rare/total,
        4
    )



print("Calculating translation features...")


df["Codon_Pair_Profile"] = (
    df["mRNA_Sequence"]
    .apply(codon_pair_profile)
)


df["Rare_Codon_Frequency"] = (
    df["mRNA_Sequence"]
    .apply(rare_codon_frequency)
)



df.to_csv(
    output_file,
    sep="\t",
    index=False
)


print("Translation features completed")
