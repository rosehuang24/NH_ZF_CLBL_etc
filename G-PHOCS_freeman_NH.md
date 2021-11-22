# Workflow

wd: /storage/zhenyingLab/huangruoshi/neutral_region

## Phastcons scores:

Sites are considered consseved if pc score is larger than 0.5

100 basepairs flanking regions were added (as freeman did in their paper for g-phocs neutral loci criteria)

```
grep '^chr' scores.bed | sed 's/M/MT/g' | awk '$4 >= 0.5 {print$1"\t"$2"\t"$3}' > PC_larger_than_0.5.bed

bedtools merge -i PC_larger_than_0.5.bed | awk '$3-$2>3 {print$1"\t"$2-100"\t"$3+100}' > PC_larger_than_0.5_length3_100b_flanking.bed

grep -v 'A' PC_larger_than_0.5_length3_100b_flanking.bed | grep -v 'K' | grep -v 'Z' | grep -v 'W' | grep -v 'M' |sed 's/chr//g' | sort -k1,1n -k2,2n -k3,3n | awk 'BEGIN {OFS="\t" }; { if($2 < 0) print $1"\t0\t"$3; else print $0}' | bedtools merge | sort -k 1.1n -k 2,2n > PC_larger_than_0.5_length3_100b_flanking.merged.bed
```

this is to get genome coordinates/end pos. Will also be used in later steps

```
grep '^>' ../chicken_ref/Gallus_gallus.GRCg6a.dna_rm.toplevel.fa  | awk -F ":" '{print$4"\t"$6}' > genome.from.dna_rm.txt
```

To prevent bed region going out of chromosome:

```
parallel --colsep '\t' -q awk '($1=="{1}") { if($3 > {2}) print $1"\t"$2"\t{2}"; else print $0}' PC_larger_than_0.5_length3_100b_flanking.merged.bed :::: genome.from.dna_rm > PC_larger_than_0.5_length3_100b_flanking.merged.tailed.bed
```


## CDS 50kb flanking

It is different from previous vesions because I used ensembl CDS.fa instead of extracting from gff

```
grep "^>" Gallus_gallus.GRCg6a.cds.all.fa | awk -F ":" '{print$3"\t"$4-50000"\t"$5+50000}'  | awk 'BEGIN {OFS="\t" }; { if($2 < 0) print $1"\t0\t"$3; else print $0}'| sort -k1,1 -k2,2n| bedtools merge > CDS.50kb_flanking.midstep.bed

```

To prevent bed region going out of chromosome:

```
parallel --colsep '\t' -q awk '($1=="{1}") { if($3 > {2}) print $1"\t"$2"\t{2}"; else print $0}' CDS.50kb_flanking.midstep.bed :::: genome.from.dna_rm >  CDS.50kb_flanking.bed
```


## repeatitive regions

To combine all the disposable regions:

```
cat PC_larger_than_0.5_length3_100b_flanking.merged.tailed.bed CDS.50kb_flanking.bed | sort -k 1,1 -k 2,2n | bedtools merge > dispose_PC0.5_CDS_both.flanking.bed
bedtools complement -i dispose_flanking_PC_CDS.repetitive.bed -g genome.from.dna_rm > neutral.region.flanking_PC_CDS.repetitive.bed
```

