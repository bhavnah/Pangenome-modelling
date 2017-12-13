#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Authors: Bhavna Hurgobin
#Date:    09/08/2016
#Institution: The University of Western Australia
#Usage: python add_index.py 1.genomes.core 1.genomes.pan 1 >> matrix.txt
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import sys
import itertools

f1=open(sys.argv[1],'r') #1.genomes.core
f2=open(sys.argv[2],'r') #1.genomes.pan
index=int(sys.argv[3])

for a,b in itertools.izip(f1,f2):
    la=a.rstrip()
    lb=b.rstrip()
    print str(index)+','+a.replace('\n','')+','+b.replace('\n','')
