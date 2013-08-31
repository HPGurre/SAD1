import sys
from collections import deque

#Data structures
men = [1,3,5]
women = [2,4,6]
current = {x: None for x in women}
menPreferenceList = {1: deque([6,4,2]), 3: deque([2,6,4]), 5: deque([6,4,2])}
ranking = {2: {3:0,5:1,1:2}, 4: {5:0,1:1,3:2}, 6: {1:0,5:1,3:2}}
    
#Open the file and load contents into memory
with open(sys.argv[1], 'r') as f:
    for line in f:
        if line.startswith('#'):
            pass
        elif line.startswith('n'):
            n = line[2]
#         elif 1+1:
#             print(line, end='')

#Gale-Shapley Algorithm
while men:
    man = men.pop()
    woman = menPreferenceList[man].popleft()
    if current[woman] == None:
        current[woman] = man
    elif ranking[woman][man] < ranking[woman][current[woman]]:
        discardedMan = current[woman]
        men.append(discardedMan)
        current[woman] = man
    else:
        men.append(man)

#Print results during or after algorithm?..
print(current)