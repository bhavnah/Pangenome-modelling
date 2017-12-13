# Pangenome-modelling
Steps to model pangenome expansion and core genome reduction.

# Prerequisites
1. Gene presence/absence variation (PAV) table: This can be obtained by running SGSGeneLoss () and should be formatted to look like this:
```
1,1,1,0,1,0,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1
0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,1,0,0,0,1,0,1,0,0
0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,1,0,0,0,1,0,1,0,0
0,0,0,0,0,0,0,1,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,1,0,1,0,1,1,1,1,0,0
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,1,1,0,1,0,0,0,1,1,1,0,0,0
0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,1,1,1,1,0,1,1,0,1,0,1,1,1,0,0,0
0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,1,0
0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,1,0
```
'1' means present and '0' means lost. Each row represents the status of a gene (present or absent) and each column represent the status of a gene in a particular individual/cultivar

2. R (latest version; minpack.lm required)

# Methodology

1. Create folders for each genome:

```
seq 1 50 | while read line; do mkdir $line"_"genomes; done
```

2. Print cut command to extract tables with all possible combinations of genomes:

```
seq 1 50 | while read line; do echo python print.py $line ">>" $line"_"genomes/extract"_"$line"_"genomes.sh; done
```

3. Extract tables. The table extraction will produce a lot of files depending on the number of genomes being sampled. Here we are only using 100,000 random combinations of 50 genomes only. The assumption is that within these 100,000 combinations we would have captured enough information to do the modelling. The more combinations, the longer the run time. One flaw of this method is that when generating the combinations, the same combination may be generated several times. To account for this, we can do more combinations. But testing has shown that combinations of 10,000 and 100,000 produce similar results provided enough genomes have been sampled.

```
seq 1 50 | while read line; do bash $line_genomes/extract_$line_genomes.sh; done
```

4. Get number of core genes and pangenome genes for each possible combination (e.g. shown here for 2 genomes; repeat for all genomes).

```
for i in 2_genomes/*.txt; do python extract_core.py $i 2 >> 2.genomes.core; done
for i in 2_genomes/*.txt; do python extract_pan.py $i 2 >> 2.genomes.pan; done
```

6. Merge the results for all 50 genomes into a single file:

```
python add_index.py 1.genomes.core 1.genomes.pan 1 >> matrix.txt
python add_index.py 2.genomes.core 2.genomes.pan 2 >> matrix.txt
python add_index.py 3.genomes.core 3.genomes.pan 3 >> matrix.txt
etc...
```

7. Model in R
```
Rscript 6.model_all.R
```
