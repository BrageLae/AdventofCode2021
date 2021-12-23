# Reproduce every 7 days
# Not synchronized
# 9 days for newborns

import time

with open ("input.txt") as file:
    vec = file.read().split(',')

vec = list(map(int, vec))


def partTwo(maxdays, vec):
    iter = 1
    tot_time = time.time()
    while (iter <= maxdays):
        interval_time = time.time()
        vec.extend([9] * vec.count(0))
        vec = [x-1 if x != 0 else 6 for x in vec]
        iter += 1
        print("interval {} seconds: {}".format(iter, time.time() - interval_time))
    print("total seconds: {}".format(time.time() - tot_time))
    print(len(vec))

v = [vec.count(x) for x in range(9)]
print(v)

def partTwo(maxDays, vec):
    iter = 1
    while (iter <= maxDays):
        tmp = vec[0]
        vec[0] = vec[1]
        vec[1] = vec[2]
        vec[2] = vec[3]
        vec[3] = vec[4]
        vec[4] = vec[5]
        vec[5] = vec[6]
        vec[6] = vec[7] + tmp
        vec[7] = vec[8]
        vec[8] = tmp
        iter += 1
partTwo(256, v)
print(sum(v))