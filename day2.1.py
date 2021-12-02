import csv
import numpy as np

forwards = 0
depth = 0
with open("input2.txt") as input:
    reader = csv.reader(input,delimiter=' ')
    for row in reader:
        if row[0] == 'forward':
            forwards += int(row[1])
        elif row[0] == 'up':
            depth -= int(row[1])
        elif row[0] == 'down':
            depth += int(row[1])
        else: 
            print("Error")

print(forwards)
print(depth)

print(forwards*depth)