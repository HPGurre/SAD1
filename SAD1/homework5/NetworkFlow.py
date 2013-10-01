import timeit
from homework5.Graph import Graph, Vertex
from homework5.BreadthFirstSearch import BreadthFirst

def augment(maxFlow, P):
    bottleneck = min(P, key= lambda x :x.capacity-x.flow).capacity
    for arc in P:
        #verify the that these are correct
        if arc.isForward:
            arc.flow += bottleneck
            #arc.reverseEdge.flow += bottleneck
        elif not arc.isForward:  
            arc.flow -= bottleneck
           # arc.reverseEdge.flow -= bottleneck

    return maxFlow + bottleneck
    
def maxflow():
    maxFlow = 0
    bfs = BreadthFirst(G, G.source)
    while bfs.hasPathTo(G.sink):
        P = bfs.pathTo(G.sink)
        maxFlow =  augment(maxFlow, P)
        bfs = BreadthFirst(G , G.source)
        
        #remove these print out when done...
        print("maxflow is currently: {0}".format(maxFlow))
        for e in G.arcs:
            print(e)
            
    return maxFlow
            
start = timeit.default_timer()

G = Graph();
with open('rail.txt', 'r') as f:
    for line in f:    
        if line.startswith('55'): #Quick fix
            for vertex in range(int(line[:-1])):
                line = f.__next__()
                G.addVertex(Vertex(line[:-1]))
                                 
        if line.startswith('119'): #Quick fix
            m = int(line[:-1])
            for arc in range(int(line[:-1])):
                line = f.__next__()
                tokens = line.split() 
                a = int(tokens[0])
                b =  int(tokens[1])
                c = int(tokens[2]) if int(tokens[2]) > 0 else float('inf') 
                G.addArc(a, b, c)
       
print('MaxFlow: {0}'.format(maxflow()))

stop = timeit.default_timer()
total = stop-start
print("Runtime(total): " + str(total))

