pos = []
with open("input7.txt") as input:
    pos = [ int(n) for n in input.read().split(",") ]

pos.sort()
median = pos[int(len(pos)/2)]
print(median)

fuel = 0
for n in pos:
    fuel += abs(n-median)

print(fuel)