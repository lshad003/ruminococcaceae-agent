#!/usr/bin/env python3
"""
SMART AI Agent: Inspects data first, then solves problems
"""

from ruminococcaceae_analysis import RuminococcaceaeAnalyzer
import pandas as pd
import subprocess
import os

analyzer = RuminococcaceaeAnalyzer()

print("\n" + "="*70)
print("🧠 SMART AI AGENT: Autonomous problem solving")
print("="*70 + "\n")

# STEP 1: Inspect the data first
print("[Step 1] Inspecting GTDB metadata structure...")
df = pd.read_csv('reference_genomes/ruminococcaceae_metadata.tsv', sep='\t', nrows=3)

data_info = f"""
GTDB Metadata Structure:
- Total columns: {len(df.columns)}
- Sample columns: {list(df.columns[:20])}
- First few rows:
{df.head(3).to_string()}
"""

print(data_info)

# STEP 2: Ask AI to write code that works with THIS data
print("\n[Step 2] Asking AI to write solution for THIS EXACT data structure...")

solution = analyzer.agent.analyze_ruminococcaceae(
    'bioinformatics',
    f"""I have GTDB metadata with the following structure:
    
{data_info}

The file is at: reference_genomes/ruminococcaceae_metadata.tsv

Task: Write Python code that:
1. Reads this EXACT metadata file
2. Identifies which columns contain completeness and contamination data
3. Filters for genomes with >90% completeness, <5% contamination
4. Selects top 300 by completeness
5. Saves filtered list to: data/filtered_genomes/high_quality_genomes.tsv
6. Saves accession list to: data/filtered_genomes/accession_list.txt

IMPORTANT: 
- Use the ACTUAL column names from the data shown above
- The file has NO HEADER - use column positions
- Column 3 appears to be completeness
- Column 4 appears to be contamination
- Column 1 appears to be accession

Write ONLY executable Python code, no explanations.
Use this format:
```python
[your code here]
```
"""
)

print(solution)

# STEP 3: Extract and run the Python code
print("\n[Step 3] Extracting and executing solution...")

import re
code_match = re.search(r'```python\n(.*?)```', solution, re.DOTALL)

if code_match:
    code = code_match.group(1)
    
    # Save code
    with open('scripts/filter_genomes_auto.py', 'w') as f:
        f.write(code)
    
    print("✓ Code extracted and saved")
    
    # Execute code
    print("\n[Step 4] Running the code...")
    try:
        exec(code)
        print("✅ Code executed successfully!")
        
        # Verify results
        if os.path.exists('data/filtered_genomes/accession_list.txt'):
            count = len(open('data/filtered_genomes/accession_list.txt').readlines())
            print(f"\n✅ SUCCESS! Filtered {count} genomes")
            print(f"   Files created:")
            print(f"   - data/filtered_genomes/high_quality_genomes.tsv")
            print(f"   - data/filtered_genomes/accession_list.txt")
            
            if count > 0:
                print(f"\n🚀 Ready to download!")
                print(f"   Next: sbatch jobs/02_download_ncbi.sh")
            else:
                print(f"\n⚠️  No genomes passed filter - asking AI to debug...")
        else:
            print("⚠️  Output files not created - something went wrong")
            
    except Exception as e:
        print(f"❌ Error executing code: {e}")
        print("\n🔄 Let me ask AI to fix this...")
else:
    print("⚠️  No Python code found in AI response")
    print("Saving response for review...")
    with open('results/ai_response.txt', 'w') as f:
        f.write(solution)

print("\n" + "="*70)
print("🎉 Smart agent completed!")
print("="*70)
