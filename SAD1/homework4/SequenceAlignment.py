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
        if i > 0 and j > 0 and A[i-1][j-1] == max(A[i-1][j-1], A[i-1][j], A[i][j-1]):
            AlignmentA = X[i-1] +AlignmentA 
            AlignmentB = Y[j-1] + AlignmentB
            i = i-1
            j = j-1
        elif i > 0 and A[i-1][j] == max(A[i-1][j], A[i][j-1]):
            AlignmentA = X[i-1] + AlignmentA 
            AlignmentB = "-" + AlignmentB
            i -= 1
        else:
            AlignmentA = "-" + AlignmentA
            AlignmentB = Y[j-1] + AlignmentB
            j -= 1

    return AlignmentA, AlignmentB
    
def Alignment(X, Y):
        delta = -4; # take this from the file.
        
        #initialise
        A = [[None for y in range(len(Y)+1)] for x in range(len(X)+1)] #A[row(x)][column(y)]
        
        for i in range(len(X)+1):
            A[i][0] = i*delta
        for j in range(len(Y)+1):
            A[0][j] = j*delta

        AL = []
        cost = AlignmentRec1(X,Y,A,AL)[0] 
        a1, a2 = findAlignment(A, X, Y)
        return cost, a1, a2

def AlignmentRec1(X, Y, A, AL):
    #Base
    if not X:
        return (A[0][len(Y)], AL) #assumes all deltas are equal
    if not Y:
        return (A[len(X)][0], AL) #assumes all deltas are equal
    
    #Parameters
    alpha = scores[X[0]][Y[0]]
    deltaii = scores['*'][Y[0]]
    deltaiii = scores[X[0]]['*']
    
    #Recursion
    if A[len(X)][len(Y)] == None:
        A[len(X)][len(Y)] =  AlignmentRec1(X[1:], Y[1:], A, AL)[0] + alpha
        
    if A[len(X)][len(Y)-1] == None:
        A[len(X)][len(Y)-1] = AlignmentRec1(X,Y[1:], A, AL)[0] + deltaii
    
    if A[len(X)-1][len(Y)] == None:
        A[len(X)-1][len(Y)] = AlignmentRec1(X[1:], Y, A, AL)[0] + deltaiii
    
    i = A[len(X)][len(Y)]       
    ii  = A[len(X)][len(Y)-1] 
    iii = A[len(X)-1][len(Y)] 
    
    if max(i, ii, iii) == i:
        AL.append(Y[0])
        return i, AL
    elif max(ii, iii) == ii:
        return ii, AL
    else:
        return iii, AL
        
    
# def AlignmentRec(X, Y, A, AL):
#     #Base
#     if not X:
#         return (A[0][len(Y)], '') #assumes all deltas are equal
#     if not Y:
#         return (A[len(X)][0], '') #assumes all deltas are equal
# 
#     #Recursion
#     
#     if A[len(X)][len(Y)] == None:
#         rec = AlignmentRec(X[1:], Y[1:], A, AL)
#         i = rec[0]+ scores[X[0]][Y[0]]
#         A[len(X)][len(Y)] = rec[0] 
# #         AL = rec[1]
#     else:
#         i = A[len(X)][len(Y)]
#      
#     if A[len(X)][len(Y)-1] == None:
#         rec = AlignmentRec(X,Y[1:], A, AL)
#         ii =  rec[0]+scores['*'][Y[0]]
#         A[len(X)][len(Y)-1] = ii
# #         AL = rec[1]
#     else:
#         ii = A[len(X)][len(Y)-1] 
#          
#     if A[len(X)-1][len(Y)] == None:
#         rec = AlignmentRec(X[1:], Y, A, AL)
#         iii = rec[0]+scores[X[0]]['*']
#         A[len(X)-1][len(Y)] = iii
# #         AL = rec[1]
#     else:
#         iii = A[len(X)-1][len(Y)]
#     
# #     if max(i, ii, iii) == i:
# #         AL += Y[0]
# #     elif max(ii, iii) == ii:
# #         AL += '_'
# #     else:
# #         AL += '_' 
#     return max(i,ii,iii), AL

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
       # print('{0}'.format(e1.sequence)) 
    else:
        alignment = Alignment(e2.sequence, e1.sequence) 
        print('{0}---{1}: {2}'.format(e1.name, e2.name, alignment[0]))
        #print('{0}'.format(e2.sequence))

    print('{0}'.format(alignment[1]))
    print('{0}'.format(alignment[2]))
    
stop = timeit.default_timer()
total = stop-start
print("Runtime(total): " + str(total))