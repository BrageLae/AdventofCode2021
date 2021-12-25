
with open('input.txt') as file:
    mat = [[int(x[i]) for i in range(len(x))] for x in file.read().split('\n')]

def findAdj(m, row, col, partTwo = False):
    """return all values of neighbouring points"""
    vertical_size = len(m) - 1
    horizontal_size = len(m[0]) - 1
    adj = []

    if row < vertical_size:
        if partTwo:
            adj.append([m[row+1][col], row+1, col])
        else:
            adj.append(m[row+1][col])
    if row != 0:
        if partTwo:
            adj.append([m[row-1][col], row-1, col])
        else:
            adj.append(m[row-1][col])

    if col < horizontal_size:
        if partTwo:
            adj.append([m[row][col+1], row, col+1])
        else:
            adj.append(m[row][col+1])
    if col != 0:
        if partTwo:
            adj.append([m[row][col-1], row, col-1])
        else:
            adj.append(m[row][col-1])
    return adj

def isAllHigher(n, list):
    """check if n is lower than all elements in list"""
    lt = [True if x > n else False for x in list ]
    return all(lt)

def findLowPoints(m, partTwo = False):
    lowPoints = []
    for row in range(len(m)):
        for col, x in enumerate(m[row]):
            if isAllHigher(x, findAdj(m, row, col)):
                if partTwo:
                    lowPoints.append([x, row, col])
                else:
                    lowPoints.append(x)
    return lowPoints

print('risk level = {}'.format(sum([x+1 for x in findLowPoints(mat)])))

added_points = []

def findBasin(m, x, row, col):
    size = 1
    adjs = findAdj(m, row, col, partTwo=True) # [[value, row, col], [], ...]
    for i in range(len(adjs)):
        value_adjacent = adjs[i][0]
        adj_row = adjs[i][1]
        adj_col = adjs[i][2]
        if value_adjacent > x and value_adjacent != 9:
            if((adj_row, adj_col) not in added_points):
                added_points.append((adj_row, adj_col))
                size += findBasin(m, value_adjacent, adj_row, adj_col)            
    return size

basinSizes = []
for lowpoint in findLowPoints(mat, partTwo=True):
    val, row, col = lowpoint[0], lowpoint[1], lowpoint[2]
    basinSizes.append(findBasin(mat, val, row, col))

answer = 1
for i in range(3):
    ans = max(basinSizes)
    basinSizes.remove(ans)
    answer *= ans

print(answer)

    
