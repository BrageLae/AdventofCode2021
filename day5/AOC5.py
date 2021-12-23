import re
import numpy as np

with open ("input.txt") as file:
    lines = file.read().replace('\n',",")   # read file, replace newline with comma
    line = re.split(',|->', lines)          # turn string to list of chars, split at comma and arrow

size = len(line)//4                         # size of each sublist  
line = list(map(int, line))                 # cast objects in the list to int
sizemat = max(line) + 1                     # size of matrix
isPartTwo = True

vecs = []

x1s, x2s, y1s, y2s = line[::4], line[2::4], line[1::4], line[3::4] # separate list into four lists

# add vectors to vecs
for it in range(size):
    x1, x2, y1, y2 = x1s[it], x2s[it], y1s[it], y2s[it]
    # horizontal lines
    if (x1 == x2):
        diff = abs(y1-y2)
        startit = max(y1, y2)
        for i in range(diff + 1):
            vecs.append([x1, startit-i])
    # vertical lines
    if (y1s[it] == y2):
        diff = abs(x1-x2)
        startit = max(x1, x2)
        for i in range(diff + 1):
            vecs.append([startit-i, y1])
    # diagonal line: up right/down left
    if (x1+y1 == x2+y2 and isPartTwo):
        diff = abs(x1-x2)
        xmax = max(x1,x2)
        ymin = min(y1,y2)
        for i in range(diff + 1):
            vecs.append([xmax-i, ymin+i])
    # diagonal line: up left/down right
    elif (abs(x1-x2) == abs(y1-y2) and isPartTwo):
        diff = abs(x1-x2)
        xmax = max(x1,x2)
        ymax = max(y1,y2)
        for i in range(diff + 1):
            vecs.append([xmax-i, ymax-i])
        
# init matrix
matrix = np.zeros((sizemat, sizemat), int)

# update matrix
for i in vecs:
    matrix[i[1]][i[0]] += 1

# count all elements in matrix that are larger than 1
ans = np.count_nonzero(matrix > 1) 
print(ans)
