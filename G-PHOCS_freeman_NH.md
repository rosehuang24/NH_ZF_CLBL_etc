# Workflow

wd: /storage/zhenyingLab/huangruoshi/neutral_region

## Phastcons scores:

Sites are considered consseved if pc score is larger than 0.5

100 basepair flanking regions were added (as freeman did in their paper for g-phocs neutral loci criteria)

```
grep '^chr' scores.bed | sed 's/M/MT/g' | awk '$4 >= 0.5 {print$1"\t"$2"\t"$3}' > PC_larger_than_0.5.bed

bedtools merge -i PC_larger_than_0.5.bed | awk '$3-$2>3 {print$1"\t"$2-100"\t"$3+100}' > PC_larger_than_0.5_length3_100b_flanking.bed

grep -v 'A' PC_larger_than_0.5_length3_100b_flanking.bed | grep -v 'K' | grep -v 'Z' | grep -v 'W' | grep -v 'M' |sed 's/chr//g' | sort -k1,1n -k2,2n -k3,3n | awk 'BEGIN {OFS="\t" }; { if($2 < 0) print $1"\t0\t"$3; else print $0}' | bedtools merge | sort -k 1.1n -k 2,2n > PC_larger_than_0.5_length3_100b_flanking.merged.bed
```
