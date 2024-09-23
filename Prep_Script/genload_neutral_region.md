```
#CDS from gff3 (release110)

ref=/storage/zhenyingLab/huangruoshi/chicken_ref
grep -v "#" $ref/Gallus_gallus_gca000002315v5.GRCg6a.110.gff3  |  awk '($3=="CDS") && ($1<29) {print$1"\t"$4"\t"$5}'  | sort -k 1,1n -k 2,2n | awk '{print$1"\t"$2-50000"\t"$3+50000}' > gff3.release110.CDS.50kbflanking.bed

parallel --colsep '\t' -q awk '($1=="{1}") { if($3 > {2}) print $1"\t"$2"\t{2}"; else print $0}'  gff3.release110.CDS.50kbflanking.bed  :::: /storage/zhenyingLab/huangruoshi/20211122_nh/genome.from.dna_rm | awk '{ if ($2 < 0) print$1"\t0\t"$3; else print$0}' | sort -k 1,1n -k 2,2n | bedtools merge -i - > gff3.release110.CDS.50kbflanking.inrange.bed

cat $ref/repetitive_auto.bed /storage/zhenyingLab/huangruoshi/20211122_nh/PC_larger_than_0.5_length3_100b_flanking.merged.tailed.bed gff3.release110.CDS.50kbflanking.inrange.bed | sort -k 1,1n -k 2,2n | bedtools merge -i - | awk '($1<29) {print$0}' >  dispose.PC_rep_cds_50kbflanking.bed

bedtools complement -i dispose.PC_rep_cds_50kbflanking.bed -g /storage/zhenyingLab/huangruoshi/20211122_nh/genome.from.dna_rm | awk '($1<29) {print$0}' > neutral.bed
```
