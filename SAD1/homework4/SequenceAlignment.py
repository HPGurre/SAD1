import re
import itertools
import timeit

class Entity:
    def __init__ (self, name, sequence):
        self.name = name
        self.sequence = sequence
        
    def __str__(self):
        return "Entity(%s: [%s])"%(self.name, self.sequence) 

def Alignment(X, Y):
        delta = -4; # take this from the file.
        
        #initialise
        A = [[None for y in range(len(Y))] for x in range(len(X))] #A[row(x)][column(y)]
        
        for i in range(len(X)):
            A[i][0] = i*delta 
        
        for j in range(len(Y)):
            A[0][j] = j*delta
        
        return AlignmentRec(X,Y,A)      
    
def AlignmentRec(X, Y, A):
    #base
    if not X:
        return len(Y)*-4
#         return A[0][len(Y)-1] FIXME
    if not Y:
        return len(X)*-4
        #return A[len(X)-1][0] FIXME
    i   = scores[X[0]][Y[0]]+ AlignmentRec(X[1:], Y[1:], A)
    ii  = scores['*'][Y[0]] + AlignmentRec(X,Y[1:], A)
    iii = scores[X[0]]['*'] + AlignmentRec(X[1:], Y, A)
        
    return max(i, ii , iii )

file = 'BLOSUM62.txt'
scores = {};
with open(file, 'r') as f: 
    letters = [] 
    for line in f:
        if line.startswith("#"):
            continue;
        if line.startswith(" "):
            letters = line.split()
            scores = {key: {key1 :None} for key in letters for key1 in letters}
            continue
        else:
            tokens = line.split();
            letter = tokens[0]
            theScores = line.split()[1:]
            for i in range(len(letters)):
                scores[letter][letters[i]] = int(theScores[i])
            
start = timeit.default_timer()

file = 'Toy_FASTAs.in'
Entities = []
with open(file, 'r') as f:
    for line in f:
        Entities.append(Entity(line[1:-2], f.__next__()[:-1]))      

for e1, e2 in itertools.combinations(Entities, 2):
    alignment = Alignment(e1.sequence, e2.sequence)
    print('{0}---{1}: {2}'.format(e1.name, e2.name, alignment))
    print('{0}'.format("("+e1.name+') Alignment [TODO]'))
    print('{0}'.format("("+e2.name+') Alignment [TODO]'))
    

stop = timeit.default_timer()
total = stop-start
print("Runtime(total): " + str(total))