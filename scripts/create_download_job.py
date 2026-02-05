#!/usr/bin/env python3
"""
Ask AI to create download job script that actually works
"""

from ruminococcaceae_analysis import RuminococcaceaeAnalyzer
import re
import os
import subprocess

analyzer = RuminococcaceaeAnalyzer()

print("🤖 Asking AI to create working download script...")

solution = analyzer.agent.analyze_ruminococcaceae(
    'bioinformatics',
    """I have 300 Ruminococcaceae genome accessions in: data/filtered_genomes/accession_list.txt
    
    Example accessions:
    GB_GCA_018379485.1
    GB_GCA_017517145.1
    RS_GCF_010509575.1
    
    Create a SLURM job script that:
    1. Downloads genomes from NCBI FTP
    2. Handles both GCA and GCF accessions
    3. Handles GB_ and RS_ prefixes
    4. Uses wget with retry logic
    5. Downloads in parallel (8 jobs)
    6. Resource requirements: 16GB RAM, 8 CPUs, 24 hours
    7. Account: stajichlab
    8. Partition: batch
    
    Output only the SLURM script in this format:
```bash
    #!/bin/bash
    #SBATCH ...
    [script here]
```
    """
)

print(solution)

# Extract script
match = re.search(r'```bash\n(.*?)```', solution, re.DOTALL)
if match:
    script = match.group(1)
    
    with open('jobs/03_download_final.sh', 'w') as f:
        f.write(script)
    
    os.chmod('jobs/03_download_final.sh', 0o755)
    
    print("\n✅ Created: jobs/03_download_final.sh")
    print("\n🚀 Ready to submit: sbatch jobs/03_download_final.sh")
else:
    print("⚠️  Could not extract script")
