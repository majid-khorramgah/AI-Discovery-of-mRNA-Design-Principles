import os


scripts=[
"01_sequence_length_features.py",
"02_gc_content_analysis.py",
"03_codon_usage_analysis.py",
"04_calculate_cai.py",
"05_rna_structure_prediction.py"
]


for s in scripts:

    print("Running:",s)

    os.system(
        f"python {s}"
    )


print("Feature extraction pipeline completed")
