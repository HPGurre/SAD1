import sys
import re

class Vertex:
    def __init__(self, name):
        self.name = name
        
class Edge:
    def __init__(self, fromVertex, toVertex, weight): 
        self.fromVertex = fromVertex
        self.toVertex = toVertex
        self.weight = weight
    
class Record:
    def __init__(self, vertex, pointer): 
        self.vertex = vertex
        self.pointer = pointer
        # FIXME: Implement this( see page 154)
        
class UnionFind:
    def __init__(self):
        pass
    def makeUnionFind(self, vertices):
        """Creates the Union-find data structure with n sets, where n is the no. of vertices
        """
        pass
        # FIXME: Implement this (see page 154)   
    def find(self, vertex):
        """Returns the name of the set that this vertex currently belongs to
        """
        pass
        # FIXME: Implement this( see page 154) 
    def union(self, component1, compoment2):
        """Unions the two sets that the vertices belong to
        """
        pass
        # FIXME: Implement this (see page 154) 

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
            vertices.append(Vertex(line))
        elif cityDistancePattern.match(line):
            # TODO: Optimize the extraction of the edges. It feels like too much work is being done.
            fromVertex = line.split('--')[0];
            toVertex =  line.split('--')[1].split("[")[0][0:-1]
            weight = int(line.split('--')[1].split("[")[1][0:-2])
            edges.append(Edge(fromVertex, toVertex, weight))
            

def Kruskal(vertices, edges):
    #Sort edges weights so that c1 <= c2 =< ... <=cm
    edges.sort(key=lambda edge: edge.weight)
    # TODO: Look p running time of this. It need to be at least n LogN. 

    # T is initially empty, where T is the subset of edges.
    T = []

    #for (u belonging V) make a set containing singleton u
    unionFind = UnionFind.makeUnionFind(UnionFind, vertices)
    
    #  for i = 1 to m
    for edge in edges: 
        # (u, v) = ei
          
        if (edge.fromVertex != edge.toVertex):
            #T = T UNION ei
            T.append(edge)
            
            #merge the sets containing u and v
            # unionFind.union(set1, set2)

    return sum(x.weight for x in T)

totalWeight = Kruskal(vertices, edges)
#totalWeight = 16598 

#assert totalWeight == 16394, "Your error is probably in the parsing stage, not in the algorithm." 
#assert totalWeight != 16598, "Your answer is wrong - no suggestions are available." 




