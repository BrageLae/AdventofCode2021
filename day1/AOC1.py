import os

##############################
########### PART 1 ###########
##############################

# Count the number of times a depth measurement increases from the previos measurement

testList = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263] # part1 = 7, part2 = 5
testList2 = [x for x in range(0,100)] # part1 = 99, part2 = 99?

# depthList has the content of the text file, convert type to int
with open("puzzleInput.txt", 'r') as file:
    depthList = file.readlines()
    depthList = [int(line) for line in depthList]

def checkIncList(lst):
    return sum([1 for x in range(1,len(lst)) if lst[x] > lst[x-1]])

print("test1: {ans}".format(ans = checkIncList(testList)))
print("test2: {ans}".format(ans = checkIncList(testList2)))
print("answer: {ans} \n\n".format(ans = checkIncList(depthList)))

##############################
########### PART 2 ###########
##############################

# Count the number of times the sum of measurements in this sliding window increases
# Sliding window size = 3

def checkWindowList(lst):
    return sum([1 for x in range(1,len(lst)-2) if sum(lst[x:x+3]) > sum(lst[x-1:x+2])])

print("test1: {ans}".format(ans = checkWindowList(testList)))
print("test2: {ans}".format(ans = checkWindowList(testList2)))
print("answer: {ans}".format(ans = checkWindowList(depthList)))