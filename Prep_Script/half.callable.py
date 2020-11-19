#input file from:
#bedtools intersect -a Afake.bed -b Bfake.bed -wo | awk '{print$1"\t"$2"\t"$7}'
#Afake is the 1kb.bed, B is callable.bed file for each population/individual.

import sys

infile = sys.argv[1]
inh = open(infile, 'r')

outfile = sys.argv[2]
outh = open(outfile, 'w')


dc={}
for lines in inh:
    line =lines.strip().split()

    pos = line[0]+"_"+line[1]
    dc.setdefault(pos, []).append(int(line[2]))

#print(dc)
for keys, values in dc.items():
    if sum(dc[keys]) >=500:
        key=keys.split("_")
        outh.write(key[0]+'\t'+key[1]+'\t'+str(int(key[1])+1000)+'\n')



inh.close()
outh.close()
