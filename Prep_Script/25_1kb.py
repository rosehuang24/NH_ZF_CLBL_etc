#Input is the 1 kb set .bed side by side

#chromosome splitting is needed

#the purpose of this script is to identify the loci that are truly 25kb apart from each other.

#there are a few places that can be improved (such as whether adding the last line)
#but tbh I really don't care now. It's working, and let it just stay this way.

import sys


infile = sys.argv[1]
inh = open(infile, 'r')
outfile = sys.argv[2]
outh = open(outfile, 'w')

index = sum(1 for line in open(infile))-1

lines = inh.readlines()

if index>1:
    i=0
    while i < index:
        start=lines[i].strip().split()[1]
        outh.write(lines[i])
        for c in range(1,index+1):
            next_start=lines[i+c].strip().split()[1]
            if int(next_start)-int(start)<25000 and int(i)+int(c)<index:
                continue
            i+=c
            break


    outh_last_start=lines[i-c].strip().split()[1]
    inh_last_start=lines[index].strip().split()[1]
    if int(inh_last_start)-int(outh_last_start)>24999:
        outh.write(lines[index])

elif index==1:
    outh.write(lines[0])
    outh_last_start=lines[0].strip().split()[1]
    inh_last_start=lines[1].strip().split()[1]
    if int(inh_last_start)-int(outh_last_start)>24999:
        outh.write(lines[index])
else:
    outh.write(lines[0])

inh.close()
outh.close()
