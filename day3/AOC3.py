## Part 1 ##

with open("puzzleInput.txt") as x:
    xs = x.read().split()

gamma, epsilon = [], []

# keep most common bit for each position
for i in range(len(xs[0])):
    if ([int(x[i]) for x in xs].count(0) > len(xs)/2): 
        gamma.append('0'); epsilon.append('1')
    else: 
        gamma.append('1'); epsilon.append('0') 

# convert list to string, then cast binary string to decimal int
gamma = int(''.join(gamma),2)
epsilon = int(''.join(epsilon),2)

print("gamma: {g}, epsilon: {e}, product: {p}".format(g= gamma, e= epsilon, p= gamma*epsilon))

## Part 2 ##

o, co2 = xs.copy(), xs.copy()

i = 0
while (len(o) > 1):
    if ([int(x[i]) for x in o].count(0) > len(o)/2):
        dropInds = [o.index(x) for x in o if x[i] == '1']
    else:
        dropInds = [o.index(x) for x in o if x[i] == '0']
    for index in sorted(dropInds, reverse=True):
        del o[index]
    i += 1

i = 0
while (len(co2) > 1):
    if ([int(x[i]) for x in co2].count(0) > len(co2)/2):
        dropInds = [co2.index(x) for x in co2 if x[i] == '0']
    else:
        dropInds = [co2.index(x) for x in co2 if x[i] == '1']
    for index in sorted(dropInds, reverse=True):
        del co2[index]
    i += 1

o = int(o[0],2)
co2 = int(co2[0],2)

print("oxygen: {o}, co2: {co2}, life support rating: {p}".format(o= o, co2= co2, p= o*co2))
