#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Authors: Bhavna Hurgobin
#Date:    09/08/2016
#Institution: The University of Western Australia
#Usage: for i in 2_genomes/*.txt; do python extract_core.py $i 2 >> 2.genomes.core; done
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import sys

f1=open(sys.argv[1],'r')
genomes=int(sys.argv[2])

core=0
pan=0

#f1.readline() #skip header
for line in f1:
    l=line.rstrip().split(",")
    if l[0:].count('1') == genomes:
       core+=1
    if l[0:].count('0') == genomes:
       continue

print str(core)
