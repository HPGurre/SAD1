import sys
from collections import deque

#Data structures
men = [1,3,5]
women = [2,4,6]
isNotWedlocked = {x: True for x in women}
menPreferenceList = {1: deque([6,4,2]), 3: deque([2,6,4]), 5: deque([6,4,2])}
#womenPreferenceList = {2: [3,5,1], 4: [5,1,3], 6: [1,5,3]}

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
    if isNotWedlocked[woman]:
        pass
#         assign m and w to be engaged
#     elif (w prefers m to her fiance m')
#         assign m and w to be engaged, and m' to be free
    else:
        men.append(man)

#Print results during or after algorithm?..