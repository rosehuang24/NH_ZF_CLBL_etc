# Get CDS sequece

bedtools getfasta -fi Gallus_gallus.GRCg6a.dna.toplevel.fa -bed cds.bed -fo chkn_cds.ffn
python3 fakemuta.py
sort -V fake_mutation.vcf | uniq > fakemuta_uniq.vcf
java -Xmx4g -jar /backup/home/zhenying_Group/huangruoshi/biosoft/snpEff/snpEff.jar -c /backup/home/zhenying_Group/huangruoshi/biosoft/snpEff/snpEff.config -v Galgal6a fakemuta_uniq.vcf > output_ann.vcf
cat output_ann.vcf | grep -v "#" | sed 's/NN=/ /' | awk '{print $1 "_" $2, $9}' | sed 's/||WARNING_TRANSCRIPT_NO_START_CODON//g' | sed 's/|||||/BBBBB/g' | sed 's/||,/ /g' | sed 's/,/ /g' > format.ann


#need to double check on the script
python3 iteration.py

