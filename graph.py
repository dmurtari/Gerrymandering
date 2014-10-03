from node import Node

# Defines a Graph using an adjacency list.
class Graph:

    # Initialize a graph with an empty list of nodes
    def __init__(self):
        self.nodeList = {}
        self.clock = 0
        self.sccCount = 0
        self.sccSum = []
        self.sccSumMembers = []
        self.sccEdges = 0
        self.diameter = 0

    # Allow iterations over nodes
    def __iter__(self):
        return iter(self.nodeList.values())
    
    # Import a graph from a file. Each line should contain the two nodes that
    # an edge goes between, separated by a tab.
    # ONLY WORKS FOR UNWEIGHTED GRAPHS (Could easily work for weighted)
    def importFromFile(self, graph, reverse = False):
        fopen = open(graph, "r")
        graphList = fopen.read().splitlines()
        
        for pair in graphList:
            pair = pair.split("\t")
            if reverse:
                self.addEdge(pair[1], pair[0])
            else:
                self.addEdge(pair[0],pair[1])

    # Add a node of a given name, and increment the amount of nodes
    def addNode(self, name):
        self.nodeList[name] = Node(name)

    # Add an edge from source to dest, creating source and dest if they do not 
    # exist
    def addEdge(self, source, dest, weight = 0):
        if source not in self.nodeList:
            self.addNode(source)
        if dest not in self.nodeList:
            self.addNode(dest)
        self.nodeList[source].addNeighbor(self.nodeList[dest], weight)

    # Get all nodes in the current graph
    def getNodes(self):
        return self.nodeList.keys()