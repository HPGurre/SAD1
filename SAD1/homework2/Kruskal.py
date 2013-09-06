import sys
import re

# class Vertex:
#     def __init__(self, name):
#         self.name = name
        
class Edge:
    def __init__(self, fromVertex, toVertex, weight): 
        self.fromVertex = fromVertex
        self.toVertex = toVertex
        self.weight = weight    
        
class UnionFind:
    components = []
    parent = {}
    size = {}
    def __init__(self):
        pass
    def makeUnionFind(self, vertices):
        """Creates the Union-find data structure with n singleton sets, 
        where n is the number of vertices
        """
        for vertex in vertices:
            self.components.append({vertex})
            self.parent[vertex] = vertex
            self.size[vertex] = 1

    def find(self, vertex):
        """Returns the name of the set that this vertex currently belongs to
        """
        while vertex != self.parent[vertex]: 
            vertex = self.parent[vertex]
        return vertex

    def union(self, vertex, anotherVertex):
        """Weighted Quick-union 
        """
        if self.size[vertex] < self.size[anotherVertex]:
            self.parent[vertex] = anotherVertex
            self.size[anotherVertex] += self.size[vertex]
        else:
            self.parent[anotherVertex] = vertex
            self.size[vertex] += self.size[anotherVertex]
    
    def connected(self, vertex, anotherVertex):
        """Are they connected?
        """
        return self.find(vertex) == self.find(anotherVertex)
    
#Data structures
vertices=[]
edges=[]

#REGEX for matching the lines in the file
cityPattern = re.compile('^["]?\D*["]?$')
cityDistancePattern = re.compile('^.*[[]\d*[]]')

#Open the file and load contents into memory
with open(sys.argv[1], 'r') as f:
    for line in f:  
        
        if cityPattern.match(line):
            vertices.append(line.rstrip('\n').strip(' " '))
            
        elif cityDistancePattern.match(line):
            # TODO: Optimize the extraction of the edges. It feels like too much work is being done.
            fromVertex = line.split('--')[0].strip(' "')
            toVertex =  line.split('--')[1].split('[')[0].strip(' "')
            weight = int(line.split('--')[1].split("[")[1][0:-2])
            edges.append(Edge(fromVertex, toVertex, weight))
 
for edge in edges:
    print(edge.fromVertex)
    print(edge.toVertex)
    print(edge.weight)
print(vertices)            

def Kruskal(vertices, edges):
    #Sort edges weights so that c1 <= c2 =< ... <=cm
    edges.sort(key=lambda edge: edge.weight)
    # TODO: Look up running time of this. It need to be at least n LogN. 

    # T is initially empty, where T is the subset of edges.
    T = set()

    #for (u belonging V) make a set containing singleton u
    unionFind = UnionFind()
    unionFind.makeUnionFind(vertices)
    
    #  for i = 1 to m
    for edge in edges: 
        # (u, v) = ei
          
        if (not unionFind.connected(edge.toVertex, edge.fromVertex)):
            #T = T UNION ei
            T.add(edge)
            
            #merge the sets containing u and v
            unionFind.union(edge.toVertex, edge.fromVertex)

    return sum(edge.weight for edge in T)

totalWeight = Kruskal(vertices, edges)
print("Totalweight is: "+ str(totalWeight))
#totalWeight = 16598 

#assert totalWeight == 16394, "Your error is probably in the parsing stage, not in the algorithm." 
#assert totalWeight != 16598, "Your answer is wrong - no suggestions are available." 




