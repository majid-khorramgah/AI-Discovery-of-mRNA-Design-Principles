import os


# ============================================
# Project:
# AI Discovery of mRNA Design Principles
# ============================================


folders = [

    # Documentation
    "docs",

    # Data
    "data/raw",
    "data/processed",
    "data/external",

    # ========================================
    # Phase 01
    # Dataset Construction
    # ========================================
    "01_dataset_construction/scripts",
    "01_dataset_construction/notebooks",
    "01_dataset_construction/statistics",
    "01_dataset_construction/results",


    # ========================================
    # Phase 02
    # Biological Feature Analysis
    # ========================================
    "02_biological_feature_analysis/notebooks",
    "02_biological_feature_analysis/scripts",
    "02_biological_feature_analysis/figures",
    "02_biological_feature_analysis/results",


    # ========================================
    # Phase 03
    # Biological Rule Discovery
    # ========================================
    "03_biological_rule_discovery/models",
    "03_biological_rule_discovery/embeddings",
    "03_biological_rule_discovery/analysis",
    "03_biological_rule_discovery/results",


    # ========================================
    # Phase 04
    # Protein Representation Learning
    # ========================================
    "04_protein_representation_learning/models",
    "04_protein_representation_learning/preprocessing",
    "04_protein_representation_learning/training",
    "04_protein_representation_learning/results",


    # ========================================
    # Phase 05
    # Protein to mRNA Prediction
    # ========================================
    "05_protein_to_mrna_prediction/models",
    "05_protein_to_mrna_prediction/losses",
    "05_protein_to_mrna_prediction/configs",
    "05_protein_to_mrna_prediction/experiments",
    "05_protein_to_mrna_prediction/results",


    # ========================================
    # Phase 06
    # Explainable AI
    # ========================================
    "06_explainable_ai/shap",
    "06_explainable_ai/attention_analysis",
    "06_explainable_ai/integrated_gradients",
    "06_explainable_ai/figures",
    "06_explainable_ai/results",


    # ========================================
    # Phase 07
    # mRNA Generation
    # ========================================
    "07_mrna_generation/tokenizer",
    "07_mrna_generation/models",
    "07_mrna_generation/training",
    "07_mrna_generation/checkpoints",
    "07_mrna_generation/results",


    # ========================================
    # Phase 08
    # Multi Objective Optimization
    # ========================================
    "08_multi_objective_optimization/objectives",
    "08_multi_objective_optimization/fitness_functions",
    "08_multi_objective_optimization/optimizers",
    "08_multi_objective_optimization/results",


    # ========================================
    # Phase 09
    # Reinforcement Learning
    # ========================================
    "09_reinforcement_learning/environment",
    "09_reinforcement_learning/agents",
    "09_reinforcement_learning/rewards",
    "09_reinforcement_learning/configs",
    "09_reinforcement_learning/experiments",
    "09_reinforcement_learning/results",


    # ========================================
    # Phase 10
    # Benchmark Comparison
    # ========================================
    "10_baseline_comparison/linear_design",
    "10_baseline_comparison/codon_optimization",
    "10_baseline_comparison/ours",
    "10_baseline_comparison/tables",
    "10_baseline_comparison/figures",


    # ========================================
    # Phase 11
    # Experimental Validation
    # ========================================
    "11_experimental_validation/protocols",
    "11_experimental_validation/results",


    # ========================================
    # General
    # ========================================
    "src",
    "scripts",
    "configs",
    "results/figures",
    "results/tables"

]


files = [

    # Main documents

    "README.md",

    "docs/research_question.md",
    "docs/hypothesis.md",
    "docs/methodology.md",
    "docs/related_work.md",
    "docs/roadmap.md",
    "docs/paper_draft.md",



    # Dataset phase

    "01_dataset_construction/README.md",
    "01_dataset_construction/scripts/merge_uniprot_ncbi.py",
    "01_dataset_construction/scripts/verify_dataset.py",


    # Feature analysis

    "02_biological_feature_analysis/README.md",
    "02_biological_feature_analysis/scripts/feature_engineering.py",



    # Biological discovery

    "03_biological_rule_discovery/README.md",



    # Representation learning

    "04_protein_representation_learning/README.md",
    "04_protein_representation_learning/models/protein_encoder.py",



    # Prediction model

    "05_protein_to_mrna_prediction/README.md",
    "05_protein_to_mrna_prediction/train.py",
    "05_protein_to_mrna_prediction/evaluate.py",



    # Explainability

    "06_explainable_ai/README.md",
    "06_explainable_ai/explain.py",



    # Generation

    "07_mrna_generation/README.md",
    "07_mrna_generation/train.py",
    "07_mrna_generation/generate.py",



    # Optimization

    "08_multi_objective_optimization/README.md",
    "08_multi_objective_optimization/fitness_function.py",



    # RL

    "09_reinforcement_learning/README.md",
    "09_reinforcement_learning/train_rl.py",



    # Comparison

    "10_baseline_comparison/README.md",
    "10_baseline_comparison/run_comparison.py",



    # Validation

    "11_experimental_validation/README.md",



    # Environment

    "requirements.txt",
    "environment.yml",
    ".gitignore"

]


for folder in folders:
    os.makedirs(folder, exist_ok=True)


for file in files:
    with open(file, "w", encoding="utf-8") as f:
        f.write("")


print("\n====================================")
print("mRNA Research Project Structure Created")
print("AI Discovery of mRNA Design Principles")
print("====================================")