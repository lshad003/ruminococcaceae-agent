#!/bin/bash
#SBATCH --job-name=download_ruminococcaceae
#SBATCH --account=stajichlab
#SBATCH --partition=batch
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=16G
#SBATCH --time=24:00:00
#SBATCH --output=download_genomes_%j.out
#SBATCH --error=download_genomes_%j.err

set -euo pipefail

# Create output directory
mkdir -p data/genomes

# Function to download genome with retry logic
download_genome() {
    local accession=$1
    local max_retries=3
    local retry_count=0
    
    # Remove prefix and extract accession parts
    clean_acc=$(echo $accession | sed 's/^[A-Z]*_//')
    acc_prefix=$(echo $clean_acc | cut -d'_' -f1)  # GCA or GCF
    acc_number=$(echo $clean_acc | cut -d'_' -f2)
    acc_version=$(echo $clean_acc | cut -d'.' -f2)
    
    # Construct FTP URL
    acc_dir="${acc_number:0:3}/${acc_number:3:3}/${acc_number:6:3}"
    base_url="https://ftp.ncbi.nlm.nih.gov/genomes/all/${acc_prefix}/${acc_dir}"
    
    # Find the correct assembly directory
    assembly_dir="${clean_acc}_*"
    
    # Get the actual directory name
    actual_dir=$(wget -qO- "${base_url}/" | grep -o "${clean_acc}_[^/]*" | head -1)
    
    if [ -z "$actual_dir" ]; then
        echo "Error: Could not find assembly directory for $accession"
        return 1
    fi
    
    # Download genomic.fna.gz file
    fna_url="${base_url}/${actual_dir}/${actual_dir}_genomic.fna.gz"
    output_file="data/genomes/${clean_acc}_genomic.fna.gz"
    
    while [ $retry_count -lt $max_retries ]; do
        if wget -q --timeout=30 --tries=3 "$fna_url" -O "$output_file"; then
            echo "Successfully downloaded: $accession"
            return 0
        else
            retry_count=$((retry_count + 1))
            echo "Retry $retry_count/$max_retries for $accession"
            sleep 5
        fi
    done
    
    echo "Failed to download after $max_retries attempts: $accession"
    return 1
}

export -f download_genome

# Read accessions and download in parallel
cat data/filtered_genomes/accession_list.txt | \
    parallel -j 8 --joblog data/download_log.txt download_genome {}

echo "Download completed. Check data/download_log.txt for details."
