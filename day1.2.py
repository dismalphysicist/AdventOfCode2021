import numpy as np

input = np.loadtxt("input.txt",dtype=int)

gap = 3
lastsumdepths = 0
increase = 0

for i,depth in enumerate(input):
    if i > len(input) - gap:
        break
    sumdepths = sum(input[i:i+gap]) # deal with wraparound indices

    if lastsumdepths != 0 and sumdepths > lastsumdepths:
        increase += 1

    lastsumdepths = sumdepths

print(increase)