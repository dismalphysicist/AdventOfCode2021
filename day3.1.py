def splitString(s):
    return [ int(c) for c in s ]

diagnostics = []
with open('input3.txt') as input:
    diagnostics = [ splitString(line.strip()) for line in input.readlines()]

gamma = ''
epsilon = ''
for i in range(len(diagnostics[0])):
    sum_ = 0 
    for j in range(len(diagnostics)):
        sum_ += diagnostics[j][i]

    if sum_ < len(diagnostics)/2.:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

print("gamma = {}".format(gamma))
gamint = int(gamma,2)
print("epsilon = {}".format(epsilon))
epsint = int(epsilon,2)
print("Power consumption = gamma x epsilon = {}".format(gamint*epsint))