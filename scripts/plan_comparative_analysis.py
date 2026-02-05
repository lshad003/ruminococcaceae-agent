#!/usr/bin/env python3
"""
Plan comparative genomics strategy for Ruminococcaceae with resource requirements
"""

from ruminococcaceae_analysis import RuminococcaceaeAnalyzer
import os

analyzer = RuminococcaceaeAnalyzer()

print("\n" + "="*70)
print("COMPARATIVE GENOMICS STRATEGY: Ruminococcaceae Reference Genomes")
print("="*70)

# Question 1: Download strategy with computational requirements
print("\n[PART 1: Reference Genome Selection & Download Strategy]")
print("-"*70)

strategy = analyzer.agent.analyze_ruminococcaceae(
    'bioinformatics',
    """I have 284 high-quality Ruminococcaceae MAGs from herptile gut metagenomes (836 MB total).
    I'm working on HPCC cluster with SLURM job scheduler.
    
    I want to download reference Ruminococcaceae genomes from NCBI for comparative analysis.
    Similar to my previous Lachnospiraceae work.
    
    Provide detailed information including:
    
    DOWNLOAD STRATEGY:
    1. How many reference genomes should I download? (mammals, birds, environment)
    2. What host diversity should I target? (human, mouse, cow, chicken, etc.)
    3. Should I use NCBI datasets, GTDB, or both?
    4. What metadata is essential to collect (host, diet, body site, completeness)?
    5. Specific commands for downloading from NCBI using ncbi-datasets-cli
    
    COMPUTATIONAL REQUIREMENTS FOR EACH STEP:
    - Memory (GB RAM) needed
    - Number of CPU cores
    - Expected runtime
    - Disk space requirements
    
    Format key steps as:
    STEP | TOOL | MEMORY | CPUS | RUNTIME | DISK SPACE
    """
)

print(strategy)

# Question 2: Comparative analysis with resource requirements
print("\n\n[PART 2: Comparative Analysis Pipeline & Resource Requirements]")
print("-"*70)

analysis_plan = analyzer.agent.analyze_ruminococcaceae(
    'bioinformatics',
    """I'll compare 284 herptile Ruminococcaceae MAGs (836 MB) against reference genomes 
    from mammals, birds, and possibly environment.
    
    For EACH major analysis step, I need exact resource requirements for SLURM:
    
    ANALYSES NEEDED:
    1. Phylogenomic tree construction (concatenated marker genes? FastTree? IQ-TREE?)
    2. Functional annotation (Prokka? eggNOG-mapper? DRAM?)
    3. CAZyme profiling with dbCAN
    4. Metabolic pathway reconstruction (KEGG mapper? MetaCyc?)
    5. Pan-genome analysis (Roary? PIRATE? Panaroo?)
    6. Average Nucleotide Identity calculations (FastANI? pyani?)
    7. Comparative genomics (OrthoFinder? ProteinOrtho?)
    
    CRITICAL: For ~400-500 total genomes (284 herptile + 200 reference), provide:
    
    For EACH step format as:
    ## Step X: [Analysis Name]
    Tool: [name and version]
    Memory: X GB RAM
    CPUs: X cores  
    Runtime: X hours (for ~400-500 genomes)
    Disk: X GB output
    SLURM example:
```bash
    #SBATCH --mem=XG
    #SBATCH --cpus-per-task=X
    #SBATCH --time=X:00:00
    [command]
```
    """
)

print(analysis_plan)

# Question 3: Statistical analysis requirements
print("\n\n[PART 3: Statistical Analysis & Visualization Resources]")
print("-"*70)

stats_plan = analyzer.agent.analyze_ruminococcaceae(
    'analysis',
    """After phylogenomics and functional comparisons of ~400-500 genomes, 
    I need statistical analysis to identify herptile-specific adaptations.
    
    For each analysis, provide computational requirements:
    
    1. Gene enrichment analysis (host-specific genes, CAZyme differences)
       - Which test? (Fisher's exact? DESeq2? ANCOM-BC?)
       - Memory and runtime?
    
    2. Multivariate analysis (PCA, PERMANOVA on functional profiles)
       - R packages? vegan? ape? phytools?
       - Can this run on login node or needs compute?
    
    3. Phylogenetic comparative methods
       - Test for phylogenetic signal in traits?
       - Host-microbe coevolution tests?
    
    4. Visualization (phylogenetic trees, heatmaps, PCA plots)
       - Tools: ggtree? phytools? iTOL?
       - Memory requirements?
    
    For each, specify:
    - R/Python packages and versions
    - Memory requirements (GB)
    - Login node OK or compute node needed?
    - Expected runtime
    """
)

print(stats_plan)

# Save everything
os.makedirs('results', exist_ok=True)
with open('results/comparative_genomics_plan.txt', 'w') as f:
    f.write("="*70 + "\n")
    f.write("COMPARATIVE GENOMICS STRATEGY WITH RESOURCE REQUIREMENTS\n")
    f.write("="*70 + "\n\n")
    f.write("Dataset: 284 high-quality herptile Ruminococcaceae MAGs (836 MB)\n")
    f.write("Target: ~400-500 total genomes (284 herptile + 200 reference)\n")
    f.write("="*70 + "\n\n")
    f.write("[PART 1: Download Strategy & Requirements]\n")
    f.write("-"*70 + "\n")
    f.write(strategy)
    f.write("\n\n")
    f.write("[PART 2: Comparative Analysis Pipeline & Resources]\n")
    f.write("-"*70 + "\n")
    f.write(analysis_plan)
    f.write("\n\n")
    f.write("[PART 3: Statistical Analysis & Visualization Resources]\n")
    f.write("-"*70 + "\n")
    f.write(stats_plan)

# Create resource summary
print("\n\n" + "="*70)
print("✓ Complete strategy with resource requirements generated!")
print("📄 Full plan saved to: results/comparative_genomics_plan.txt")
print("\n💡 Next steps:")
print("  1. Review resource requirements")
print("  2. Create SLURM job scripts")
print("  3. Download reference genomes")
print("  4. Run comparative analysis pipeline")
print("="*70)
