#!/usr/bin/python
from __future__ import division
from sys import argv
import operator
import math
import gzip



"""
author: Tom van der Valk
"""

mtdna_dict = {}
with open(argv[1]) as f1:
    for line in f1:
          line = line.replace(" mitochondrion, complete genome","")
          line = line.replace(", whole genome shotgun sequence","")
          splitted = line.strip().split(" ")
          contig_id = splitted[0][1:]
          species = " ".join(splitted[1:])
          mtdna_dict[contig_id] = [species,0,0,0]

with open(argv[2]) as f2:
    for line in f2:
        splitted = line.strip().split("\t")
        contig_id,length = splitted[0],int(splitted[1])
        mtdna_dict[contig_id][1] = length

with open(argv[3]) as f3:
    for line in f3:
        splitted = line.strip().split("\t")
        contig,coverage = splitted[0],int(splitted[3])
        mtdna_dict[contig][2] += 1
        mtdna_dict[contig][3] += coverage

print("contigID","species","mtDNA length","covered bases","percentage of mtDNA covered","coverage of covered bases","genome-wide coverage",sep="\t")
for key,value in mtdna_dict.items():
     contigID = key
     species = value[0]
     length = value[1]
     if length > 14000 and length < 20000:
        if value[2] > 0:
            bases = value[2]
            percentage_covered = round(value[2]/value[1],3)
            coverage = round(value[3]/value[2],3)
            all_coverage = round(value[3]/value[1],3)
            
            print(contigID,species,length,bases,percentage_covered,coverage,all_coverage,sep="\t")
