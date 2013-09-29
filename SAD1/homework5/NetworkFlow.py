import timeit
from collections import deque

class Vertex:
    def __init__ (self, name):
        self.name = name

    def __str__(self):
        return "Vertex(%s)"%(self.name) 
    
class Arc:
    def __init__(self, fromVertex, toVertex, capacity, isForward=True): 
        self.fromVertex = fromVertex
        self.toVertex = toVertex
        self.capacity = capacity
        self.isForward = isForward  
        
    def __str__(self):
        direction = 'forward' if self.isForward else 'backward'
        return "Arc(%s > %s) [%s][%s]"%(self.fromVertex, self.toVertex, self.capacity,direction ) 
    
    
def augment(f, P):
    b = max(P, key= lambda x :x.capacity) #fixme insert correct key
#     for arc in P:
#         if arc.isForward:
#             pass # increase f(e) in G by b
#         else:
#             pass
    
    return f
    
def maxflow():
    pass


def bfs(G, s):  
    queue = deque([s])
    
    while len(queue) == 0 :
        queue.popleft()
    
    
start = timeit.default_timer()

file = 'rail.txt'
vertices = []
arcs = []
with open(file, 'r') as f:
    for line in f:
        if line.startswith('55'): #Quick fix
            n = int(line[:-1])
            for vertex in range(n):
                line = f.__next__()
                vertices.append(Vertex(line[:-1]))     
                                
        if line.startswith('119'): #Quick fix
            m = int(line[:-1])
            for arc in range(m):
                line = f.__next__()
                tokens = line.split() 
                a = tokens[0]
                b =  tokens[1]
                c = int(tokens[2])
                arcs.append(Arc(a, b, c))

for v in vertices:
    print(v)
for a in arcs:
    print(a)
P = []
P.append(Arc("a", "b", 10))
P.append(Arc("a", "b", 1))
P.append(Arc("a", "b", 2))

augment("s", P)
stop = timeit.default_timer()
total = stop-start
print("Runtime(total): " + str(total))

