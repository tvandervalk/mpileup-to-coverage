# mpileup-to-coverage
Script to calculate depth and breath of coverage for contigs in a BAMfile, using the output from samtools mpileup

Runs as follows:
'python mtDNA_coverages.py fasta_headers.txt reference.fai filename.mpile'

Required files:
fasta_header.txt: Headers of the reference fasta file. Can be obtained by running grep ">" reference.fna > fasta_header.txt
