import sys
from collections import deque
import re

#Data structures
men = []
women = []
menPreferenceList = {'Ross': deque(['Rachel','Phoebe','Monica']), 'Chandler': deque(['Monica','Rachel','Phoebe']), 'Joey': deque(['Rachel','Phoebe','Monica'])}
ranking = {'Monica': {'Chandler':0,'Joey':1,'Ross':2}, 'Phoebe': {'Joey':0,'Ross':1,'Chandler':2}, 'Rachel': {'Ross':0,'Joey':1,'Chandler':2}}
    
#REGEX for matching the lines in the file
manPattern = re.compile("\s*\d*[13579][ ]")
womanPattern = re.compile("\s*\d*[02468][ ]")
manPrefPattern = re.compile("\s*\d*[13579][:]")
womanPrefPattern = re.compile("\s*\d*[02468][:]")

#Open the file and load contents into memory
with open(sys.argv[1], 'r') as f:
    for line in f:
#         elif line.startswith('n'):
#             n = line[2]
#             continue
        if manPattern.match(line):
            men.append(line.split()[1])
            continue
        elif womanPattern.match(line):
            women.append(line.split()[1])
            continue
        elif manPrefPattern.match(line):
            print("FIXME: MAN PREFERENCES MATCH")
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