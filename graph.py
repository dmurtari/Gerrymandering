from node import Node

# Defines a Graph using an adjacency list.
class Graph:

    # Initialize a graph with an empty list of nodes
    def __init__(self, graph_file):
        self.node_list = {}
        import_from_file(graph_file)

    # Allow iterations over nodes
    def __iter__(self):
        return iter(self.node_list.values())
    
    # Import a graph from a file. Each line should contain the two nodes that
    # an edge goes between, separated by a tab.
    # ONLY WORKS FOR UNWEIGHTED GRAPHS (Could easily work for weighted)
    def import_from_file(self, graph_file, reverse = False):
        fopen = open(graph_file, "r")
        graphList = fopen.read().splitlines()
        
        for pair in graphList:
            pair = pair.split("\t")
            if reverse:
                self.add_edge(pair[1], pair[0])
            else:
                self.add_edge(pair[0],pair[1])

    # Add a node of a given name, and increment the amount of nodes
    def add_node(self, name):
        self.node_list[name] = Node(name)

    # Add an edge from source to dest, creating source and dest if they do not 
    # exist
    def add_edge(self, source, dest, weight = 0):
        if source not in self.node_list:
            self.add_node(source)
        if dest not in self.node_list:
            self.add_node(dest)
        self.node_list[source].addNeighbor(self.node_list[dest], weight)

    # Get all nodes in the current graph
    def get_nodes(self):
        return self.node_list.keys()