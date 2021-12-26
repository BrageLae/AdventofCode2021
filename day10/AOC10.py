
import statistics

with open("input.txt") as file:
    lines = [x.strip() for x in file.readlines()]

errors = []
syntaxErrorScore = 0
incompleteList = []
completionScores = []

def findCorrupted(line):
    stack = []

    for i, x in enumerate(line):

        if isOpener(x):
            stack.append(x)

        if isCloser(x):
            if len(stack) == 0: 
                errors.append(x)
                return "Closed unopened chunk"
            if stack[-1] != getOpen(x): 
                errors.append(x)
                return ("Expected: {}. Found: {}. Index: {}".format(getClose(stack[-1]), x, i))
            if stack[-1] == getOpen(x):
                stack.pop()
    if len(stack) == 0:
        return 'OK'
    incompleteList.append(''.join(stack))
    return ("Incomplete, opened: {} without closing".format(''.join(stack)))

def isOpener(char):
    return '(' == char or '<' == char or '[' == char or '{' == char

def isCloser(char):
    return ')' == char or '>' == char or ']' == char or '}' == char

def getOpen(close):
    if close == ')': return '('
    if close == '>': return '<'
    if close == ']': return '['
    if close == '}': return '{' 

def getClose(open):
    if open == '(': return ')'
    if open == '<': return '>'
    if open == '[': return ']'
    if open == '{': return '}'

for i, line in enumerate(lines):
    print('line ', i, ': ', findCorrupted(line))

for i in errors:
    if i == ')': syntaxErrorScore += 3
    elif i == ']': syntaxErrorScore += 57
    elif i == '}': syntaxErrorScore += 1197
    elif i == '>': syntaxErrorScore += 25137
    else: print("Error, error {} is incorrect error.".format(i))

print("Syntax error score = {}".format(syntaxErrorScore))

# part 2

scores = {')': 1,
          ']': 2,
          '}': 3,
          '>': 4}

def autoComplete(str):
    tot_score = 0
    for char in reversed(str):
        closer = getClose(char)
        score = scores[closer]
        tot_score *= 5
        tot_score += score
    return tot_score

for str in incompleteList:
    completionScores.append(autoComplete(str))

print('median score = {}'.format(statistics.median(completionScores)))


