import itertools
import timeit

class Entity:
    def __init__ (self, name, sequence):
        self.name = name
        self.sequence = sequence
        
    def __str__(self):
        return "Entity(%s: [%s])"%(self.name, self.sequence) 
    
def findAlignment(A, X, Y):
    AlignmentA = ""
    AlignmentB = ""
    i = len(X)
    j = len(Y)
    
    while i or j :
        if i > 0 and j > 0 and A[i][j] == A[i-1][j-1]+scores[X[i-1]][Y[j-1]]:
            AlignmentA = X[i-1] + AlignmentA 
            AlignmentB = Y[j-1] + AlignmentB 
            i = i-1
            j = j-1
        elif i > 0 and A[i][j] == A[i-1][j] -4:
            AlignmentA = X[i-1] + AlignmentA 
            AlignmentB = "-" + AlignmentB 
            i = i-1
        elif i > 0 and A[i][j] == A[i][j-1] -4:
            AlignmentA = "-" + AlignmentA
            AlignmentB = Y[j-1] + AlignmentB
            j = j - 1
        else:
            print("error")

    return AlignmentA, AlignmentB

def Alignment(X, Y):
        delta = -4; # take this from the file.
        
        #initialise
        A = [[None for y in range(len(Y)+1)] for x in range(len(X)+1)] #A[row(x)][column(y)]
        
        for i in range(len(X)+1):
            A[i][0] = i*delta
        for j in range(len(Y)+1):
            A[0][j] = j*delta
            
        for i in range(1,len(X)+1):
            for j in range(1, len(Y)+1):
            
                #Parameter
                alpha = scores[X[i-1]][Y[j-1]]
                deltaii = scores['*'][Y[j-1]]
                deltaiii = scores[X[i-1]]['*']
                
                resi = A[i-1][j-1]
                resii = A[i-1][j]
                resiii = A[i][j-1]
                
                A[i][j] = max( resi + alpha, resii  + deltaii, resiii + deltaiii)    
            
        a1, a2 = findAlignment(A, X, Y)
        return A[len(X)][len(Y)], a1, a2

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
    if len(e1.sequence) > len(e2.sequence):
        alignment = Alignment(e1.sequence, e2.sequence)
        print('{0}---{1}: {2}'.format(e1.name, e2.name, alignment[0]))
    else:
        alignment = Alignment(e2.sequence, e1.sequence) 
        print('{0}---{1}: {2}'.format(e1.name, e2.name, alignment[0]))

    print('{0}'.format(alignment[1]))
    print('{0}'.format(alignment[2]))   
    
stop = timeit.default_timer()
total = stop-start
print("Runtime(total): " + str(total))