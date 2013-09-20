# import sys
# import re
# import math
import itertools
# import glob
import timeit
from xml.dom.minidom import Entity

class Entity:
    def __init__ (self, name, sequence):
        self.name = name
        self.sequence = sequence
        
    def __str__(self):
        return "Entity(%s: [%s])"%(self.name, self.sequence) 

def Alignment(X, Y):
        pass
    
start = timeit.default_timer()
theFile = 'Toy_FASTAs.in'
#Open the file and load contents into memory
Entities = []
with open(theFile, 'r') as f:
    for line in f:
        Entities.append(Entity(line[1:-2], f.__next__()[:-1]))      

for e in Entities:
    print(e)

for e1, e2 in itertools.combinations(Entities, 2):
    print('{0}---{1}'.format(e1.name, e2.name))
    Alignment(e1.sequence, e2.sequence)
        

theClosestPair = Alignment(1, 2)
    
stop = timeit.default_timer()
total = stop-start
print("Runtime(total): " + str(total))