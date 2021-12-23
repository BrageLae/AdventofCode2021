
import numpy as np
with open("input.txt") as file:
    input = file.read().split(',')


input = list(map(int, input))
max = max(input)

# part 1
best = np.inf
position = -1

for i in range(max):
    tmp = sum([abs(x-i) for x in input])
    if tmp < best: best = tmp; position = i

print("Position = {}, Fuel consumption = {}".format(position, best))

# part 2
best = np.inf
position = -1

def sumFun(n):
    return n*(n+1)//2

for i in range(max):
    tmp = sum([sumFun(abs(x-i)) for x in input])
    if tmp < best: best = tmp; position = i



print("Position = {}, Fuel consumption = {}".format(position, best))