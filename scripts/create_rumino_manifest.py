#!/usr/bin/env python3
"""
Create a manifest of high-quality Ruminococcaceae MAGs
Does NOT copy files - just creates a reference list
"""

import pandas as pd
import glob
import os

def create_ruminococcaceae_manifest():
    """Create manifest file with bin IDs and file paths"""
    
    gtdb_base = "/bigdata/stajichlab/shared/projects/Herptile/Metagenome/Fecal/results_bins_gtkdb"
    checkm_base = "/bigdata/stajichlab/shared/projects/Herptile/Metagenome/Fecal/results_bins_checkm"
    bins_base = "/bigdata/stajichlab/shared/projects/Herptile/Metagenome/Fecal/results"
    
    manifest = []
    
    # Find all GTDB-Tk results
    gtdb_files = glob.glob(f"{gtdb_base}/**/gtdbtk.bac120.summary.tsv", recursive=True)
    
    for gtdb_file in gtdb_files:
        try:
            df = pd.read_csv(gtdb_file, sep='\t')
            
            # Filter for Ruminococcaceae
            rumino = df[df['classification'].str.contains('f__Ruminococcaceae', na=False)]
            
            for _, row in rumino.iterrows():
                bin_id = row['user_genome']
                sample_id = os.path.basename(os.path.dirname(gtdb_file))
                
                # Construct path to actual MAG file
                mag_path = f"{bins_base}/{sample_id}/bins/{bin_id}.fa"
                
                manifest.append({
                    'bin_id': bin_id,
                    'sample_id': sample_id,
                    'classification': row['classification'],
                    'mag_path': mag_path,
                    'gtdb_file': gtdb_file
                })
                
        except Exception as e:
            print(f"Error: {e}")
    
    # Convert to DataFrame
    manifest_df = pd.DataFrame(manifest)
    
    # Add CheckM quality metrics
    quality_data = []
    for sample_dir in glob.glob(f"{checkm_base}/*"):
        sample_id = os.path.basename(sample_dir)
        summary_file = f"{sample_dir}/summary_table.tsv"
        
        if os.path.exists(summary_file):
            try:
                qc = pd.read_csv(summary_file, sep='\t')
                qc['sample_id'] = sample_id
                quality_data.append(qc)
            except:
                pass
    
    if quality_data:
        quality_df = pd.concat(quality_data, ignore_index=True)
        
        # Merge with manifest
        manifest_df = pd.merge(
            manifest_df,
            quality_df[['Bin Id', 'Completeness', 'Contamination', 'sample_id']],
            left_on=['bin_id', 'sample_id'],
            right_on=['Bin Id', 'sample_id'],
            how='left'
        )
    
    # Filter for high quality (>90% complete, <5% contamination)
    high_quality = manifest_df[
        (manifest_df['Completeness'] >= 90.0) &
        (manifest_df['Contamination'] <= 5.0)
    ].copy()
    
    # Calculate quality score
    high_quality['quality_score'] = high_quality['Completeness'] - (5 * high_quality['Contamination'])
    high_quality = high_quality.sort_values('quality_score', ascending=False)
    
    # Save manifest files
    os.makedirs('data', exist_ok=True)
    
    # All Ruminococcaceae (no quality filter)
    manifest_df.to_csv('data/ruminococcaceae_all_manifest.tsv', sep='\t', index=False)
    
    # High quality only
    high_quality.to_csv('data/ruminococcaceae_HQ_manifest.tsv', sep='\t', index=False)
    
    # Simple list for downstream tools
    with open('data/ruminococcaceae_HQ_bins.txt', 'w') as f:
        for path in high_quality['mag_path']:
            f.write(path + '\n')
    
    print(f"\n{'='*60}")
    print(f"MANIFEST CREATED")
    print(f"{'='*60}")
    print(f"Total Ruminococcaceae MAGs: {len(manifest_df)}")
    print(f"High-quality MAGs (>90% complete, <5% contam): {len(high_quality)}")
    print(f"\nFiles saved:")
    print(f"  - data/ruminococcaceae_all_manifest.tsv (all MAGs)")
    print(f"  - data/ruminococcaceae_HQ_manifest.tsv (high quality)")
    print(f"  - data/ruminococcaceae_HQ_bins.txt (file paths only)")
    print(f"\n💾 Total size: ~{(len(manifest_df) + len(high_quality)) * 0.001:.2f} KB")
    print(f"{'='*60}\n")
    
    return high_quality

if __name__ == "__main__":
    hq_mags = create_ruminococcaceae_manifest()
    
    # Show sample of results
    print("\nSample of high-quality MAGs:")
    print(hq_mags[['bin_id', 'sample_id', 'Completeness', 'Contamination', 'quality_score']].head(10))
