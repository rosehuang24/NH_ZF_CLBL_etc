import sys

infile = sys.argv[1]
inh = open(infile, 'r')

outfile = sys.argv[2]
outh = open(outfile, 'w')




for lines in inh:
    if not lines.startswith('#'):
        #info = lines.strip().split()[8]
        #print(info)
        for line in lines.strip().split()[9:]:
            gt=line.split(":")
            #print(gt[0])
            if gt[0] == "0/1":
                outh.write(lines)
            elif gt[0] == "0|1":
                outh.write(lines)



outh.close()
inh.close()
