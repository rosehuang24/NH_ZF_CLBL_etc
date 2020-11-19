#cut out the 1kb regions from the semi-neutral region ikb.py:no 25kb interval. They are 1kb side by side.

import sys

infile = sys.argv[1]
inh = open(infile, 'r')

outfile = sys.argv[2]
outh = open(outfile, 'w')


for lines in inh:
    line =lines.strip().split()
    rg = int(line[2])-int(line[1])
    c = 0
    count = []
    if rg >= 1000:
        mul = (rg//1000)
        while c < mul:
            c+=1
            count.append(c)
        #print(count)
        #print(mul)
        for i in count:
            start = str(int(line[1])+1000*(i-1))
            end = str(int(start)+1000)
            outh.write(line[0]+'\t'+start+'\t'+end+'\n')



inh.close()
outh.close() 
