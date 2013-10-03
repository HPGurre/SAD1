class Vertex:
    def __init__ (self, name):
        self.name = name
 
    def __str__(self):
        return "Vertex(%s)"%( self.name) 
    
class Arc:
    def __init__(self, fromVertex, toVertex, capacity, isForward=True): 
        self.fromVertex = fromVertex
        self.toVertex = toVertex
        self.capacity = capacity
        self.isForward = isForward
        self.flow = 0
        
    def __str__(self):
        direction = 'forward' if self.isForward else 'backward'
        return "%s > %s [%s/%s](%s)"%(self.fromVertex, self.toVertex, self.flow, self.capacity, direction ) 

class Graph:
    def __init__(self): 
        self.vertices = []
        self.arcs = []
        self.adj = {}
        self.flow = {}
        self.sink = None
        self.source = None
    
    def addVertex(self, vertex):
        if vertex.name == 'ORIGINS':
            self.source = vertex
        if vertex.name == 'DESTINATIONS':
            self.sink = vertex
        self.adj[vertex] = []
        self.vertices.append(vertex)
    
    def addArc(self, a, b, c):
        fromVertex = self.vertices[a]
        toVertex = self.vertices[b]
        edge = Arc(fromVertex,toVertex, c) 
        reverseEdge = Arc(toVertex,fromVertex, c, False)
        reverseEdge.isForward = False 
        self.adj[fromVertex].append(edge)
        self.adj[toVertex].append(reverseEdge)
        self.arcs.append(edge)
        self.arcs.append(reverseEdge)
