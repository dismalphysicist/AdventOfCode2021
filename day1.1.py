import csv

increase = 0

with open("input.txt") as input:
    reader = csv.reader(input,delimiter=' ')
    lastdepth = 0
    starti = 0
    gap = 3
    for line in reader:
        depth = int(line[0].strip())
        if (lastdepth != 0 and depth > lastdepth):
            increase += 1
        lastdepth = depth 
    
    print("Total rows = {}".format(reader.line_num))

print("Increased depths = {}".format(increase))