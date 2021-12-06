
with open("puzzleInput.txt") as x:
    xs = x.readline().split(',')
    ys = x.read().split()

xs = list(map(int, xs))
ys = list(map(int, ys))

size = 5



bingoBoards = [[[ys[k+j*5+i*25] for k in range(size)] for j in range(size)] for i in range(int(len(ys)/size**2))]
hitBoards = [[[False for k in range(size)]for j in range(size)]for i in range(int(len(ys)/size**2))]

def checkBingo(boards):
    for i in range(int(len(ys)/size**2)):
        if checkBoard(boards[i]):
            return i
    return -1

def checkBoard(board):
    for i in range(size):
        if all(board[i]): return True
        if all([r[i] for r in board ]): return True
    return False

def checkRem(boards, lst):
    for i in range(int(len(ys)/size**2)):
        if i in lst: continue
        if checkBoard(boards[i]):
            return i
    return -1

boardnumber = -1
it = 0

while it < len(xs): 
    indices = [i for i, x in enumerate(ys) if x == xs[it]]
    for j in range(len(indices)):
        c = indices[j] // 25
        b = indices[j] % 25 // 5
        a = indices[j] % 5
        hitBoards[c][b][a] = True
    if checkBingo(hitBoards) >= 0:
        boardnumber = checkBingo(hitBoards)
        break
    it += 1

sum = 0
for i in range(size):
    for j in range(size):
        if hitBoards[boardnumber][i][j]:
            bingoBoards[boardnumber][i][j] = 0
        sum += bingoBoards[boardnumber][i][j]

print("sum = {sum}, last number = {num}, product = {p}".format(sum = sum, num = xs[it], p = xs[it]*sum))

