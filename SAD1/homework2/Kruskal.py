import sys
import re
  
class Edge:
    def __init__(self, fromVertex, toVertex, weight): 
        self.fromVertex = fromVertex
        self.toVertex = toVertex
        self.weight = weight    
        
class UnionFind:
    parents = {}    #Holds the parent of a vertex
    size = {}       #Holds the sizes of the components/sets
    def makeUnionFind(self, vertices):
        """Creates the Union-find data structure with n singleton sets, 
        where n is the number of vertices
        """
        for vertex in vertices:
            self.parents[vertex] = vertex
            self.size[vertex] = 1
        
    def find(self, vertex):
        """Returns the name of the set that this vertex currently belongs to
        """
        if vertex == self.parents[vertex]: 
            return vertex
        return self.find(self.parents[vertex])

    def union(self, vertex, anotherVertex):
        """Weighted Quick-union 
        """
        if self.size[vertex] < self.size[anotherVertex]:
            self.parents[self.find(vertex)] = self.find(anotherVertex)
            self.size[anotherVertex] += self.size[vertex]
        else:
            self.parents[self.find(anotherVertex)] = self.find(vertex)
            self.size[vertex] += self.size[anotherVertex]
    
    def connected(self, vertex, anotherVertex):
        """Are they connected?
        """
        return self.find(vertex) == self.find(anotherVertex)
    
#REGEX for matching the lines in the file
cityPattern = re.compile('^["]?\D*["]?$')
cityDistancePattern = re.compile('^.*[[]\d*[]]')

#Open the file and load contents into memory
with open(sys.argv[1], 'r') as f:
    vertices=[]
    edges=[]
    for line in f:  
        
        if cityPattern.match(line):
            vertices.append(line.rstrip('\n').strip(' " '))
            
        elif cityDistancePattern.match(line):
            # TODO: Optimize the extraction of the edges. It feels like too much work is being done.
            fromVertex = line.split('--')[0].strip(' "')
            toVertex =  line.split('--')[1].split('[')[0].strip(' "')
            weight = int(line.split('--')[1].split("[")[1][0:-2])
            edges.append(Edge(fromVertex, toVertex, weight))
        
def Kruskal(vertices, edges):
    edges.sort(key=lambda edge: edge.weight)
    # TODO: Look up running time of this. It need to be at least n*LogN. Alternative use a PQ.

    T = set()
    unionFind = UnionFind()
    unionFind.makeUnionFind(vertices)
    
    for edge in edges: 
        if (not unionFind.connected(edge.fromVertex, edge.toVertex)):
            T.add(edge)
            unionFind.union(edge.fromVertex, edge.toVertex)
        
    return sum(edge.weight for edge in T)

print("Total weight is: "+ str(Kruskal(vertices, edges)))
#assert totalWeight != 16598, "Your answer is wrong (if the result is 16394 your error is probably in the parsing stage, not in the algorithm.)" 




