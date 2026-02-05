#!/usr/bin/env python3
"""
Evaluate the scientific merit of the Ruminococcaceae MAG project
"""

from ruminococcaceae_analysis import RuminococcaceaeAnalyzer
import os

analyzer = RuminococcaceaeAnalyzer()

print("\n" + "="*70)
print("CRITICAL EVALUATION: Ruminococcaceae MAG Study from Herptile Metagenomes")
print("="*70)

# Question 1: Scientific merit and novelty
print("\n[PART 1: Scientific Merit & Publication Potential]")
print("-"*70)
lit_response = analyzer.literature_review("""
I have 157 assembled herptile (reptile/amphibian) gut metagenome samples with:
- GTDB-Tk taxonomic classifications 
- CheckM quality assessments
- Binned MAGs from MetaBAT2

Research plan: Identify and characterize high-quality Ruminococcaceae MAGs 
from these herptile gut samples.

Critical evaluation needed:
1. Is this publishable? What's the novelty?
2. Ruminococcaceae is well-studied in mammals - what's unique about herptile hosts?
3. What would make this study impactful vs. just another MAG catalog?
4. What comparisons/analyses are essential?
5. Should I compare to my existing Lachnospiraceae work from the same samples?
6. What are the gaps in current Ruminococcaceae knowledge that this could fill?
""")

print(lit_response)

# Save results
os.makedirs('results', exist_ok=True)
with open('results/project_evaluation.txt', 'w') as f:
    f.write("="*70 + "\n")
    f.write("SCIENTIFIC EVALUATION\n")
    f.write("="*70 + "\n\n")
    f.write(lit_response)
    f.write("\n\n")

print("\n" + "="*70)
print("✓ Evaluation complete!")
print("📄 Full report saved to: results/project_evaluation.txt")
print("="*70)
