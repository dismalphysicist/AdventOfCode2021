import re 

drawn = []
boards = []

with open('input4.txt') as input:
    drawn = [ int(e.strip()) for e in input.readline().split(',') ]

    for i in range(75):
        input.readline()
        tmp = input.read(10)
        print(tmp)

print(drawn)
# print(boards)
