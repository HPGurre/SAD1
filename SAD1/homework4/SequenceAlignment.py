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
        A = [[None for y in range(len(Y)+1)] for x in range(len(X)+1)] #A[row(x)][column(y)]
        
        for i in range(len(X)+1):
            A[i][0] = i*delta
        for j in range(len(Y)+1):
            A[0][j] = j*delta
        
        cost = AlignmentRec(X,Y,A)  
        
        return (cost, '[TODO]AlignmentX', '[TODO]AlignmentY')    
    
def AlignmentRec(X, Y, A):
    #base
    if not X:
        return A[0][len(Y)] #assumes all deltas are equal
    if not Y:
        return A[len(X)][0] #assumes all deltas are equal

#     if A[len(X)][len(Y)] == None:
#         i = scores[X[0]][Y[0]]+ AlignmentRec(X[1:], Y[1:], A)  
#         A[len(X)][len(Y)] = i
#     else:
#         i = A[len(X)][len(Y)]
#     
#     if A[len(X)][len(Y)-1] == None:
#         ii = scores['*'][Y[0]] + AlignmentRec(X,Y[1:], A)  
#         A[len(X)][len(Y)-1] = ii
#     else:
#         ii = A[len(X)][len(Y)-1] 
#         
#     if A[len(X)-1][len(Y)] == None:
#         iii = scores[X[0]]['*'] + AlignmentRec(X[1:], Y, A)
#         A[len(X)-1][len(Y)] = iii
#     else:
#         iii = A[len(X)-1][len(Y)]
        
    i =  A[len(X)][len(Y)] if A[len(X)][len(Y)] != None else scores[X[0]][Y[0]]+ AlignmentRec(X[1:], Y[1:], A)  
    ii =  A[len(X)][len(Y)-1] if A[len(X)][len(Y)-1] != None else scores['*'][Y[0]] + AlignmentRec(X,Y[1:], A) 
    iii =  A[len(X)-1][len(Y)] if A[len(X)-1][len(Y)] != None else scores[X[0]]['*'] + AlignmentRec(X[1:], Y, A)
    
    A[len(X)][len(Y)] = i 
    A[len(X)][len(Y)-1] =  ii 
    A[len(X)-1][len(Y)] = iii    
    
    return max(i, ii , iii)

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
    print('{0}---{1}: {2}'.format(e1.name, e2.name, alignment[0]))
    print('{0}'.format(alignment[1]))
    print('{0}'.format(alignment[2]))
    

stop = timeit.default_timer()
total = stop-start
print("Runtime(total): " + str(total))