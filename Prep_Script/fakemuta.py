#wd:/storage/zhenyingLab/huangruoshi/zf_20211129

import sys

infile = sys.argv[1]
inh = open(infile, 'r')

outfile = sys.argv[2]
outh = open(outfile, 'w')

outh.write("##fileformat=VCFv4.2\n")
outh.write('#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\n')

from Bio import SeqIO
from Bio.Seq import Seq

for lines in SeqIO.parse(inh, 'fasta'):
    chrm = lines.id.replace(":","-").split("-")[0]
    start= lines.id.replace(":","-").split("-")[1]
    sequence = lines.seq
    my_seq = Seq(str(sequence))

    for i, letter in enumerate(my_seq):
        pos = str(int(i)+int(start)) #if the input is not a real bed (e.g. if you awked the cds region from esembl cds.fa) it is already 1-based closing.)
        if letter == 'A':
            outh.write(chrm + '\t' + pos + '\t.\t' + letter +'\tC,T,G' + '\t.'*3 +'\n')
        if letter == 'T':
            outh.write(chrm  + '\t' + pos + '\t.\t' + letter +'\tC,A,G' + '\t.'*3 +'\n')
        if letter == 'G':
            outh.write(chrm + '\t' + pos + '\t.\t' + letter +'\tC,T,A' + '\t.'*3 +'\n')
        if letter == 'C':
            outh.write(chrm + '\t' + pos + '\t.\t' + letter +'\tA,T,G' + '\t.'*3 +'\n')

inh.close()
outh.close()
