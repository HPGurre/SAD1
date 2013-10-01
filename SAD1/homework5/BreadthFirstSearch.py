from collections import deque

class BreadthFirst:
    
    def __init__(self, G, s):
        self.marked = {k:False for k in G.vertices}
        self.edgeTo = {}
        self.queue = deque([s])
        self.s = s
        
        #finds paths through the graph from s.
        while self.queue:
            v = self.queue.popleft()
            for w in G.adj[v]:
                if not self.marked[w.toVertex] and (w.capacity - w.flow - w.reverseEdge.flow) > 0:
                    self.edgeTo[w.toVertex] = w
                    self.marked[w.toVertex] = True
                    self.queue.append(w.toVertex);   
            
    def hasPathTo(self, v):
        return self.marked[v]

    def pathTo(self, v):
        if not self.hasPathTo(v):
            return None
        path = []
        e = self.edgeTo[v]
        while e.fromVertex.name != 'ORIGINS':
            path.append(e)
            e = self.edgeTo[e.fromVertex]  
        return path;
