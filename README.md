# CoverageStats

Set of scripts to compute coverage stats across a set of targetted intervals

## Installation

```
git clone 

## Usage

### ./scripts/config.sh

Is just used to define all the necessary environment variables/paths
* BEDTOOLS - Path to bedtools binary
* SAMTOOLS - Path to samtools library
* TMP_PATH - Path to directory to use as temporary folder (needs to store BAMs when converting from CRAMs!)
* INTERVAL_PATH - Path to bed file containing the probe intervals

### ./scripts/compute_coverage.sh

```
./scripts/compute_coverage.sh <bam_file> <hist_output_path>
```

If the input is a CRAM file, the file is first converted into a BAM file (using the path specified in the config file to store the intermediate BAM file). 

Bedtools is used to compute the histogram file using the coverage command. The histograms are then outputted to the specified output folder.

### CoverageStats/process_hist_files.py

```
python CoverageStats/process_hist_files.py <hist_file>
```

Computes the median coverage per probe, prints the output to stdout.


## History

TODO: Write history

## Credits

Name: Alejandro Sifrim
Affiliation: Wellcome Trust Sanger Institute
E-mail: as33@sanger.ac.uk
Twitter: @asifrim

