import time

with open('input.txt') as file:
    template = file.readline().strip()
    codes = [x.strip().split(' -> ') for x in file if len(x.strip()) > 0]

RULES = {}

for [pair, insert] in codes:
    RULES[pair] = insert 
    
def step(pairs):

    # insert item between all pairs according to RULES dictionary
    newpairs = []
    for pair in pairs:
        insert = RULES.get(pair)
        newpairs.append(pair[0] + insert)
        newpairs.append(insert + pair[1])
    return newpairs

def getPairs(temp):
    """return pairs of characters from string"""
    return [''.join(pair) for pair in zip(temp[:-1], temp[1:])]

def fromPairs(pairs):
    """return string from character pairs"""
    string = ''
    for pair in pairs[:-1]:
        string += pair[0]
    return string + pairs[-1]

def countChar(string):
    return [string.count(char) for char in set(string)]

# Part 1

pairs = getPairs(template)

for i in range(10):
    pairs = step(pairs)

counts = countChar(fromPairs(pairs))
print("Most common: {} Least common: {}, subbed: {}".format(max(counts), min(counts), max(counts)-min(counts)))

# Part 2

pairs = getPairs(template)
pairCounts = dict.fromkeys(RULES, 0)
for pair in pairs:
    pairCounts[pair] += 1

countDict = {}

for [_, insert] in codes:
    if insert in countDict: continue
    else: countDict[insert] = 0
for char in template:
    countDict[char] += 1

def step2(pairCounts):
    ret = pairCounts.copy()
    for key, value in pairCounts.items():
        if value == 0: continue
        newChar = RULES.get(key)
        new1 = key[0] + newChar
        new2 = newChar + key[1] 
        countDict[newChar] += value
        ret[key] -= value
        ret[new1] += value
        ret[new2] += value
    return ret

    
for i in range(40):
    pairCounts = step2(pairCounts)

print(countDict)
print("Most common: {} Least common: {}, subbed: {}".format(max(countDict.values()),
                                                            min(countDict.values()), 
                                                            max(countDict.values())-min(countDict.values())))