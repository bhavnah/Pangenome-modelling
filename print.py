#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Authors: Bhavna Hurgobin
#Date:    09/08/2016
#Institution: The University of Western Australia
#Usage: python print.py 1 >> 1_genomes/extract_1_genomes.sh
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import random
import sys

genomes=int(sys.argv[1])
def random_combination(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(random.sample(xrange(n), r))
    return tuple(pool[i] for i in indices)

for i in range(1,100001): #100,001 is the number of combinations; change this if desired
    subset=(random_combination(range(1,51),genomes))
    if len(subset)==1:
       print "cut -d',' -f"+str(subset).replace('(','').replace(')','').replace(',','') + ' PAV_matrix.txt > '+str(subset).replace('(','').replace(')','').replace(',','')+'.txt'
    else:
         print "cut -d',' -f"+str(subset).replace('(','').replace(')','').replace(' ','') + ' PAV_matrix.txt > '+str(subset).replace('(','').replace(')','').replace(', ','_').replace(' ','')+'.txt'
