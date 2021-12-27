
import numpy as np

with open("input.txt") as file:
    mat = [[x for x in line.strip()] for line in file]

npmat = np.array(mat, dtype = int)
npmat2 = np.copy(npmat)

def findAdjacent(m, coords):
    row, col = coords[0], coords[1]
    adjacent_coords = []
    maxrow, maxcol = m.shape

    canNorth = row > 0
    canSouth = row < (maxrow - 1)
    canWest = col > 0
    canEast = col < (maxcol - 1)

    if canNorth: 
        if canWest: adjacent_coords.append([row-1, col-1])
        if canEast: adjacent_coords.append([row-1, col+1])
        adjacent_coords.append([row-1, col])
    if canSouth: 
        if canWest: adjacent_coords.append([row+1, col-1])
        if canEast: adjacent_coords.append([row+1, col+1])
        adjacent_coords.append([row+1, col])
    if canEast: adjacent_coords.append([row, col+1])
    if canWest: adjacent_coords.append([row, col-1])

    return adjacent_coords

def step(matrix):
    matrix = matrix + 1
    matrix = flash(matrix)
    matrix[matrix > 9] = 0
    return matrix
            
def flash(m): 
    fm = np.array(m > 9)
    flashed = np.copy(fm)

    while(np.any(fm)):

        rowflash, colflash = np.where(fm)
        flashcoords = list(zip(rowflash, colflash))

        for i in range(len(flashcoords)):
            inccoords = findAdjacent(m, flashcoords[i])
            for coord in inccoords:
                m[coord[0], coord[1]] += 1
        
        for r, c in np.ndindex(fm.shape):
            fm[r, c] = (m[r, c] > 9) & (flashed[r, c] == False)
            if fm[r,c]: flashed[r,c] = True
    return m

flashes = 0
for i in range(100):
    npmat = step(npmat)
    flashes += np.count_nonzero(npmat == 0)

print(flashes)

# part 2

size = npmat2.shape[0] * npmat2.shape[1]
stepcount = 0

while(True):
    stepcount += 1
    npmat2 = step(npmat2)
    if np.count_nonzero(npmat2 == 0) == size: break
    

print(stepcount)
