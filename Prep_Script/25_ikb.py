#this works on the bed that is already 1kb from neutral regions and 50%callable

import sys
infile = sys.argv[1]
inh = open(infile, 'r')

outfile = sys.argv[2]
outh = open(outfile, 'w')

c = 0
for lines in inh:
    line=lines.strip().split()
    if int(line[1]) > c:
        if int(line[1])-c>=26000:
            c=int(line[1])
            outh.write(lines)
    else:
        c=int(line[1])
        outh.write(lines)


inh.close()
outh.close()
