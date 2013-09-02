import sys
from collections import deque
import re

#Data structures
men = []
women = []
#menPreferenceList = {'Ross': deque(['Rachel','Phoebe','Monica']), 'Chandler': deque(['Monica','Rachel','Phoebe']), 'Joey': deque(['Rachel','Phoebe','Monica'])}
menPreferenceList = {}
ranking = {'2': {'3':0,'5':1,'1':2}, '4': {'5':0,'1':1,'3':2}, '6': {'1':0,'5':1,'3':2}}
    
#REGEX for matching the lines in the file
manPattern = re.compile("^\d*[13579][ ]")
womanPattern = re.compile("^\d*[02468][ ]")
manPrefPattern = re.compile("^\d*[13579][:]")
womanPrefPattern = re.compile("^\d*[02468][:]")

#Open the file and load contents into memory
with open(sys.argv[1], 'r') as f:
    for line in f:
#         elif line.startswith('n'):
#             n = line[2]
#             continue
        if manPattern.match(line):
            men.append(line.split()[0])
            continue
        elif womanPattern.match(line):
            women.append(line.split()[0])
            continue
        elif manPrefPattern.match(line):
            menPreferenceList[line[0]] = deque(line.split()[1:])
            continue
        elif womanPrefPattern.match(line):
            print("FIXME: WOMAN PREFERENCES MATCH")
            continue
        
#Gale-Shapley Algorithm
current = {x: None for x in women}

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
print('Result:')
print(current)