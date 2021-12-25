# signals mixed up
# wires connected to displays randomly
# wire/segment connections are mixed up separately for each display, same within four-digit display

# 2 = 1
# 3 = 7
# 4 = 4
# 5 = 2, 3, 5
# 6 = 0, 6, 9
# 7 = 8

unique = [2,3,4,7]
isPartOne = False

with open ("input.txt") as file:
    vals = [line.strip().split(" | ") for line in file] # split at '|' in each line, strip removes \n
    inputs, outputs = zip(*vals)                        # zip(*list) unzips list

inputs = [x.split(' ') for x in inputs]
outputs = [x.split(' ') for x in outputs]

# part 1

def getLengths(list):
    lengths =  [[len(word) for word in sub] for sub in list]
    if isPartOne:
        flattened_lengths = [word for sub in lengths for word in sub]
        count = len([x for x in flattened_lengths if unique.count(x)])
        print(count)
    return lengths

# part 2


def intersect(str1, str2):
    """return all elements occuring in both lists"""
    if len(str1) > len(str2):
        return "".join([x for x in str1 if x in str2])
    return "".join([x for x in str2 if x in str1])

def without(str1, str2):
    """return list1 without elements in list2 (list1 - list2)"""
    ret = str1
    for x in str2: ret = ret.replace(x,'')
    return ret

def equal(str1, str2):
    """Check if two strings contain the same characters"""
    return (len(str1) == len(str2) and sorted(str1) == sorted(str2))

def decode(chars):
    lengths = getLengths(chars)
    nums = []

    for i in range(len(chars)):
        bo = False
        if i == 0: bo = True
        one = chars[i][lengths[i].index(2)]
        seven = chars[i][lengths[i].index(3)]
        four = chars[i][lengths[i].index(4)]
        eight = chars[i][lengths[i].index(7)]
        a = without(seven, one) # cfa - cf = a
        bd = without(chars[i][lengths[i].index(4)], one)  # bcdf - cf = bd
        for x in [i for i,y in enumerate(lengths[i]) if y == 5]:
            if equal(intersect(chars[i][x], seven), seven): # number 3 if contains cfa
                three = chars[i][x]
                dg = without(three, seven) # acdfg - cfa = dg
                d = intersect(bd, dg)
                b = without(bd, d)
                g = without(dg, d)
        for x in [i for i, y in enumerate(lengths[i]) if y == 5]:
            if equal(intersect(chars[i][x], b), b): # number 5 if contains b
                five = chars[i][x]
                f = without(chars[i][x], a + b + d + g)
                c = without(one, f)
        e = without(chars[i][lengths[i].index(7)], a + b + c + d + f + g)
        zero = a+b+c+e+f+g
        two = a+c+d+e+g
        six = a+b+d+e+f+g
        nine = a+b+c+d+f+g
        nums.append([zero, one, two, three, four, five, six, seven, eight, nine] )
    return nums
    

codes = decode(inputs)
answers = []
for i in range(len(outputs)):
    ret = ''
    for x in outputs[i]:
        for j in range(10): 
            if equal(x, codes[i][j]): ret += (str(j))
    answers.append(int(ret))
    
print(sum(answers))


# size 2: find c, f
# size 3: find a -> 7 - 1
# save 7.
# size 4: find b, d -> 4 - 1
# size 5: only (3 intersect 7) == 7 -> find g and b by (remove)
# Find b -> bd - dg, Find d -> (bd intersect dg), Find g -> dg - bd
# size 6: only 6 has not both c, f, -> 6 has f, find c
# size 5: 5 has f -> 5 has b -> find b
# size 5: 2 has c -> 2 has e -> find e
# size 6: 0 has e
# size 6: 9 has d -> find d
# size 7: is 8, no info
# Use input to find code (decoder)
# use decoder to find numbers in output
# DO THIS BY RUNNING INTERSECT ITERATIVELY ON DIC
