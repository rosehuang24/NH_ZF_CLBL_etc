# Workflow for generating Zero-fold/Four-fold Raio

## Get CDS sequece

```
grep "^>" Gallus_gallus.GRCg6a.cds.all.fa | awk -F ":" '{print$3"\t"$4"\t"$5}' | sort -k1,1 -k2,2n| bedtools merge > CDS.from.ensembl.bed

bedtools getfasta -fi Gallus_gallus.GRCg6a.dna.toplevel.fa -bed CDS.from.ensembl.bed -fo CDS.from.ensembl.ffn
```
## Create fake mutations for each site

```
python3 fakemuta.py
sort -V fake_mutation.vcf | uniq > fakemuta_uniq.vcf
```

## Annotate for effect

```
java -Xmx4g -jar /backup/home/zhenying_Group/huangruoshi/biosoft/snpEff/snpEff.jar -c /backup/home/zhenying_Group/huangruoshi/biosoft/snpEff/snpEff.config -v Galgal6a fakemuta_uniq.vcf > output_ann.vcf
cat output_ann.vcf | grep -v "#" | sed 's/NN=/ /' | awk '{print $1 "_" $2, $9}' | sed 's/||WARNING_TRANSCRIPT_NO_START_CODON//g' | sed 's/|||||/BBBBB/g' | sed 's/||,/ /g' | sed 's/,/ /g' > format.ann
```

## Four-fold/Zero-fold categorization
#need to double check on the script
python3 iteration.py

