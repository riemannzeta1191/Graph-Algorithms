#Graph Implementation

class Graph(object):
    "Undirected Graph container"
    def __init__(self):
        self.nodes=list()
        self.edge=dict()
        
        self.color=dict()
        self.par=dict()
        self.time=0
        self.d=dict()
        self.f=dict()

        self.dfsl=list()
        self.bfsl=list()
        
    def insert(self,a,b):
        "Insert edges into graph"
        if not (a in self.nodes):
            self.nodes.append(a)
            self.edge[a]=list()
        if not (b in self.nodes):
            self.nodes.append(b)
            self.edge[b]=list()
        self.edge[a].append(b)
        self.edge[b].append(a)
        
    def succ(self,a):
        """Returns list of succesoors of cuurent node if present in graph
            else returns None"""
        try:
            return self.edge[a]
        except:
            return None

    def getnodes(self):
        "Returns list of nodes in graph"
        return self.nodes

    def dfs(self):
        "Depth first search algorithm"
        
        if not self.dfsl==[]:
            return
        
        for u in self.nodes:
            self.color[u]="white"
            self.par[u]=None
        self.time=0
        for u in self.nodes:
            if self.color[u]=="white":
                self.dfs_visit(u)
    def dfs_visit(self,u):
        self.time+=1
        
        self.dfsl.append(u)## node Discovered
        
        self.dist=self.time
        self.color[u]="grey"
        for v in self.succ(u):
            if self.color[v]=="white":
                self.par[v]=u
                self.dfs_visit(v)
        self.color[u]="black"
        self.time+=1
        self.f[u]=self.time

    def bfs(self,s):
        q=list()
        for u in self.nodes:
            self.color[u]="white"
            self.par[u]=None
        self.color[s]="grey"
        self.d[s]=0
        q.append(s)
        while q!=[]:
            u=q.pop(0)
            for v in self.succ(u):
                if self.color[v]=="white":
                    self.color[v]="grey"
                    self.d[v]=self.d[u]+1
                    self.par[v]=u
                    q.append(v)
            self.color[u]="black"
            self.bfsl.append(u)
        
class UWGraph(Graph):
    "Undirected Unweighted Graph container"
    

## Driver code
if __name__=='__main__':
    n=input("""Enter Choice:\n1. Undirected Unweighted Graph\n2. Undirected Weighted Graph
3. Directed Unweighted Graph\n4. Directed Weighted Graph\n\n$Graph\_ """)
    if n==1:
        graph=Graph()
        print "Enter edges of graph [Enter 0 0 to end]"
        while True:
            a,b=raw_input().split()
            if a=='0' or b =='0' :
                break
            graph.insert(a,b)
    ##    print graph.getnodes()
    ##    print [graph.succ(x) for x in graph.nodes]
        m=input("Enter Choice:\n1. Depth First Search\n2. Breadth First Search\n\n$Graph\_ ")
        if m==1:
            graph.dfs()
            print "Depth First Search:",graph.dfsl
        elif m==2:
            graph.bfs(graph.nodes[0])
            print "Breadth First Search:",graph.bfsl
