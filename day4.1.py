import csv 
import itertools

drawn = []
boards = []

with open("input4.txt") as input:
    reader = csv.reader(input,delimiter=',')

    for rown, row in enumerate(reader):
        if rown == 0:
            drawn = [ int(e.strip()) for e in row ]
            break

    reader = csv.reader(input,delimiter=' ')

    board = []
    for rown, row in enumerate(reader):
        if len(board) == 25:
            boards.append(board)
            board = []
        if rown != 0 and (rown)%6!=0:
            for r in row:
                if len(r) > 0:
                    board.append(int(r.strip()))

# print(drawn)
# print(boards)

def winCondition(indices):
    indices.sort()
    for subset in itertools.combinations(indices,5):
        if sum(subset)-subset[0]*5 == 50:
            print(subset)
            return True

indices = [ [] for b in boards ]

def findWinner():
    for num in drawn:
        for i,board in enumerate(boards):
            if num in board:
                indices[i].append(board.index(num))

            if winCondition(indices[i]):
                score = 0
                for j,n in enumerate(board):
                    if j not in indices[i]:
                        score += n
                print(num)
                print(board)
                score *= num
                return i, score

print(findWinner())