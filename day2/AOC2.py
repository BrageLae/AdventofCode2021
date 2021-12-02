##############################
########### PART 1 ###########
##############################

with open("puzzleInput.txt") as x:
    xs = x.readlines()

horizontalPos, depth = (0,0)

for i in range(len(xs)):
    index = xs[i].find(' ') + 1
    match xs[i][0]:
        case 'f': horizontalPos += int(xs[i][index])
        case 'd': depth += int(xs[i][index])
        case 'u': depth -= int(xs[i][index])
        

print(horizontalPos*depth)


##############################
########### PART 2 ###########
##############################

horizontalPos, depth, aim = (0,0,0)

for i in range(len(xs)):
    index = xs[i].find(' ') + 1
    match xs[i][0]:
        case 'f': 
            horizontalPos += int(xs[i][index])
            depth += aim*int(xs[i][index])
        case 'd': aim += int(xs[i][index])
        case 'u': aim -= int(xs[i][index])

print(horizontalPos*depth)
