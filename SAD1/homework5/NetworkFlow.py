import timeit

class Vertex:
    def __init__ (self, name):
        self.name = name

    def __str__(self):
        return "Vertex(%s)"%(self.name) 
    
class Arc:
    def __init__(self, fromVertex, toVertex, capacity): 
        self.fromVertex = fromVertex
        self.toVertex = toVertex
        self.capacity = capacity  
        
    def __str__(self):
        return "Arc(%s --> %s [%s])"%(self.fromVertex, self.toVertex, self.capacity) 

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
                b =  int(tokens[1])
                c = int(tokens[2])
                arcs.append(Arc(a, b, c))


for v in vertices:
    print(v)
for a in arcs:
    print(a)
stop = timeit.default_timer()
total = stop-start
print("Runtime(total): " + str(total))

