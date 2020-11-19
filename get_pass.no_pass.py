import sys

infile = sys.argv[1]
inh = open(infile, 'r')

outfile = sys.argv[2]
outh = open(outfile, 'w')

nopassfile=sys.argv[3]
nopass=open(nopassfile,'w')


for lines in inh:
    if not lines.startswith('#'):
        line = lines.strip().split()
        if line[6] == "PASS":
            outh.write(line[0]+"\t"+str(int(line[1])-1)+"\t"+line[1]+"\n")
        else:
            nopass.write(line[0]+"\t"+str(int(line[1])-1)+"\t"+line[1]+"\n")
    else:
        outh.write(lines)

outh.close()
inh.close()
nopass.close()
