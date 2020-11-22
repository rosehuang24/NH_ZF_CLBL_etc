import sys

infile = sys.argv[1]
inh = open(infile, 'r')

outfile = sys.argv[2]
outh = open(outfile, 'w')




for lines in inh:
    if not lines.startswith('#'):
        #info = lines.strip().split()[8]
        #print(info)
        coord=lines.strip().split()
        for line in lines.strip().split()[9:]:
            gt=line.split(":")
            #print(gt[0])
            if gt[0] == "0/1":
                outh.write(coord[0]+"\t"+str(int(coord[1])-1)+"\t"+coord[1]+"\n")
            elif gt[0] == "0|1":
                outh.write(coord[0]+"\t"+str(int(coord[1])-1)+"\t"+coord[1]+"\n")



outh.close()
inh.close()
