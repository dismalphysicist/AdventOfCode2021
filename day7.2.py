pos = []
with open("input7.txt") as input:
    pos = [ int(n) for n in input.read().split(",") ]

pos.sort()
lowerb = int(pos[-1]/5)
upperb = int(4*pos[-1]/5)
print(lowerb,upperb)
median = 0
fuel = len(pos) * pos[-1]*(pos[-1]+1)/2

for m in range(lowerb,upperb):
    thisfuel = 0
    for n in pos:
        d = abs(n-m)
        thisfuel += d*(d+1)/2
    # print(thisfuel)
    if thisfuel < fuel:
        fuel = thisfuel
        median = m

print(median)
print(fuel)