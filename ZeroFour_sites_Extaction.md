# Workflow for generating Zero-fold/Four-fold Raio

## Get CDS sequece

```
grep "^>" Gallus_gallus.GRCg6a.cds.all.fa | awk -F ":" '{print$3"\t"$4"\t"$5}' | sort -k1,1 -k2,2n| bedtools merge > CDS.from.ensembl.bed

bedtools getfasta -fi Gallus_gallus.GRCg6a.dna.toplevel.fa -bed CDS.from.ensembl.bed -fo CDS.from.ensembl.ffn
```
## Create fake mutations for each site

```
python3 fakemuta.py ../chicken_ref/CDS.from.ensembl.ffn fake_mutation.vcf
sort -V fake_mutation.vcf | uniq > fakemuta_uniq.vcf
```

## Annotate for effect

from 2020 there is a Ggallus 6a database in the program *yay!*

```
#go to snpeff folder
java -jar snpEff.jar download -v GRCg6a.99
```


```

java -Xmx4g -jar $snpeff/snpEff.jar -c $snpeff/snpEff.config -v Galgal6a fakemuta_uniq.vcf > output_ann.vcf

```

## Four-fold/Zero-fold categorization


All possible snpEff annotations are:

```
intragenic_variant
missense_variant
missense_variant&splice_region_variant
splice_acceptor_variant&intron_variant
splice_acceptor_variant&splice_donor_variant&intron_variant
splice_acceptor_variant&splice_region_variant&intron_variant
splice_donor_variant&intron_variant
splice_donor_variant&splice_region_variant&intron_variant
splice_region_variant
splice_region_variant&intron_variant
splice_region_variant&non_coding_transcript_exon_variant
splice_region_variant&synonymous_variant
start_lost
start_lost&splice_region_variant
stop_gained
stop_gained&splice_region_variant
stop_lost
stop_lost&splice_region_variant
synonymous_variant

```

Marsden 2016 stated:
Sites were classed as zero-fold degenerate when the four different bases resulted in four different amino acids, and four-fold degenerate when no changes in amino acids were observed.


However, in our study, based on the SNPEff annotation, we set any stop related, start-los and missense as "amino acid changing" snp (need to be paraphrased in paper)
In another word, we are only interested in:

```
missense_variant
missense_variant&splice_region_variant
splice_region_variant&synonymous_variant
start_lost
start_lost&splice_region_variant
stop_gained
stop_gained&splice_region_variant
stop_lost
stop_lost&splice_region_variant
synonymous_variant
```




The script is below. 
Sure it can be improved (such as using parser and gzip reading etc.)

```
python3 fold_categorizing.py output_ann.vcf four-fold.coords zero-fold.coords all_others-folds.coords
```

Update 2021/12/02:
The results are deposited here. Named 0-fold.coord.gz and 4-fold.coord.gz (gzip)
