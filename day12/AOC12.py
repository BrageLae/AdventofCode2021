with open("input.txt") as file:
    connections = [line.strip().split("-") for line in file]

# dictionary of all connected caves
PATH = {}

# Represent undirected graph in dict
for [one, two] in connections:
    if one in PATH:
        PATH[one].append(two)
    else:
        PATH[one] = [two]
    if two in PATH:
        PATH[two].append(one)
    else:
        PATH[two] = [one]


def findPath(fromCave, paths, available, visitedSmalls = [], visitMax = 1):
    """from cave, paths taken thus far, available small caves, can visit twice"""
    # create copies of lists for recursion steps
    p = paths.copy()
    a_s = available.copy()
    vs = visitedSmalls.copy()
    vm = visitMax

    if fromCave in a_s: 
        vs.append(fromCave)

    if vs.count(fromCave) == vm:
        a_s.remove(fromCave)
        vm = 1
    
    p.append(fromCave)  # append cave to paths
    next = PATH.get(fromCave)  # get possible next caves from graph

    for x in next:
        if x in a_s and vs.count(x) < vm:
            findPath(x, p, a_s, vs, visitMax=vm)
        elif x.isupper():
            findPath(x, p, a_s, vs, visitMax=vm)
        elif x == "end":
            all_paths.append(p + ["end"])
    return


all_paths = []
smallcaves = [
    key for key in PATH.keys() if key.islower() and key != "end" and key != "start"
]

findPath("start", [], smallcaves)
print("{} paths: \n".format(len(all_paths)))

all_paths = []


findPath("start", [], smallcaves, visitMax=2)
print("{} paths: \n".format(len(all_paths)))


debug = False
if debug:
    for path in all_paths:
        print(path)

