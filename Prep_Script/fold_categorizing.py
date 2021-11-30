#Use the result directly from hte snpeff step. 
#you will have three output files: four-fold.txt, zero-fold.txt, and all_others.txt. 
#you can also modify the script to generate 2-fold and 3-fold snps. 

import sys

infile = sys.argv[1]
fh = open(infile,'r')

foutfile  = sys.argv[2]
fouth = open(foutfile,'w')

zoutfile  = sys.argv[3]
zouth = open(zoutfile,'w')

dumpfile=sys.argv[4]
dumph = open(dumpfile,'w')



miss_var = ['stop','start_lost', 'missense_variant']
syn_var=['synonymous']

for lines in fh:
    if not lines.startswith("#"):
        position=lines.strip().split()[0]+"_"+lines.strip().split()[1]
        pos={}
        for anns in lines.replace("ANN=","").strip().split()[7].split(","):
        #ann = anns.split(",")
            nucl = anns.split('|')[0]
            mut_type =  anns.split('|')[1]
            if nucl not in pos:
                pos[nucl]=[mut_type]
            else:
                pos[nucl].append(mut_type)

        #print(pos)
        outputline=[]
        outputline.append(position)
        for x,y in pos.items():
            miss_matching=[m for m in y if any(miss in m for miss in miss_var)]
            syn_matching=[s for s in y if any(syn in s for syn in syn_var)]
            if miss_matching!=[]:
                outputline.append("missense")
            else:
                if syn_matching!=[]:
                    outputline.append("synonymous")

                else:
                    outputline.append("others")

        if outputline.count("missense") == 3:
            zouth.write(position+"\n")
        elif outputline.count("synonymous") == 3:
            fouth.write(position+"\n")
        else:
            dumph.write('\t'.join(outputline)+"\n")


dumph.close()
fh.close()
fouth.close()
zouth.close()
