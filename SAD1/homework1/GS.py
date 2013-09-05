import sys
from collections import deque
import re
import timeit
import pprint

#Data structures
men = []
women = []
menPreferenceList = {}
womenRanking = {}
menNames = {} # used for printing
womenNames = {} # used for printing

#Start calculating the time spent in execution algorithm
start = timeit.default_timer() 
    
#REGEX for matching the lines in the file
nPattern = re.compile('^[n]')
manPattern = re.compile('^\d*[13579][\s]')
womanPattern = re.compile('^\d*[02468][\s]')
manPrefPattern = re.compile('^\d*[13579][:]')
womanPrefPattern = re.compile('^\d*[02468][:]')

#Open the file and load contents into memory
with open(sys.argv[1], 'r') as f:
    for line in f:  
        if nPattern.match(line):
            n = int(line[2:])
            
        elif manPattern.match(line):
            tokens = line.split()
            men.append(tokens[0])
            menNames[tokens[0]] = tokens[1]   
                   
        elif womanPattern.match(line):
            tokens = line.split()
            women.append(tokens[0])
            womenNames[tokens[0]] = tokens[1]
            
        elif manPrefPattern.match(line):
            tokens = line.split()
            menPreferenceList[tokens[0][:-1]] = deque(tokens[1:])
            
        elif womanPrefPattern.match(line):
            tokens = line.split()
            womenRanking[tokens[0][:-1]] = {k: v for k,v in zip((tokens[1:]),range(n)) }
            #I am unsure on this above line. That is, how to initialize the map correctly.
            #It seems to do it correctly, but in the wrong order.

#Gale-Shapley Algorithm            
current = {x: None for x in women}        

while men:
    man = men.pop()
    woman = menPreferenceList[man].popleft()
    
    
    if current[woman] == None:
        current[woman] = man
        
    elif womenRanking[woman][man] < womenRanking[woman][current[woman]]:
        discardedMan = current[woman]
        men.append(discardedMan)
        current[woman] = man
        
    else:
        men.append(man)

#Calculate the running time      
stop = timeit.default_timer()
duration = stop-start

#Print results
print('Result:')
print(pprint.pformat(current, width=20))

print("Runtime")
print (duration)