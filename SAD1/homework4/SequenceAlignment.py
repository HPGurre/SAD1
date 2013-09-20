# import sys
# import math
import itertools
import timeit

class Entity:
    def __init__ (self, name, sequence):
        self.name = name
        self.sequence = sequence
        
    def __str__(self):
        return "Entity(%s: [%s])"%(self.name, self.sequence) 

def Alignment(X, Y):
        delta = 1;
        #initialise
        A = [[None for y in range(len(Y))] for x in range(len(X))] #A[row(x)][column(y)]
  
        for i in range(len(X)):
            A[i][0] = i*delta; 
        
        for j in range(len(Y)):
            A[0][j] = j*delta;
            
        #Recurrence

        return -1;
    
start = timeit.default_timer()
theFile = 'Toy_FASTAs.in'
#Open the file and load contents into memory
Entities = []
with open(theFile, 'r') as f:
    for line in f:
        Entities.append(Entity(line[1:-2], f.__next__()[:-1]))      

for e1, e2 in itertools.combinations(Entities, 2):
    alignment = Alignment(e1.sequence, e2.sequence)
    print('{0}---{1}: {2}'.format(e1.name, e2.name, alignment))
    

stop = timeit.default_timer()
total = stop-start
print("Runtime(total): " + str(total))