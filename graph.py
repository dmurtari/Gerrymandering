from node import Node

# Defines a Graph using an adjacency list.
class Graph:

    # Initialize a graph with an empty list of nodes
    def __init__(self, graph_file):
        self.node_list = {}
        self.import_from_file(graph_file)

    # Allow iterations over nodes
    def __iter__(self):
        return iter(self.node_list.values())
    
    # Import a graph from a file. Each line should contain the two nodes that
    # an edge goes between, separated by a tab.
    def import_from_file(self, graph_file, reverse = False):
        neighborhood_file = open(graph_file, "r")
        neighborhood = []
        for line in neighborhood_file:
            neighborhood.append(line.strip().split(" "))

        for i, neighbors in enumerate(neighborhood):
            for j, house in enumerate(neighbors):
                print i, j, house
                if j != (len(neighbors) - 1):
                    print "Adding edge ", house, i, j, " and ", i, j + 1
                    self.add_edge(house, neighbors[j + 1], 0) 
                if j != 0:
                    print "Adding edge ", house, i, j, " and ", i, j - 1
                    self.add_edge(house, neighbors[j - 1], 0) 
                if i != (len(neighbors) - 1):
                    print "Adding edge ", house, i, j, " and ", i + 1, j
                    self.add_edge(house, neighborhood[i + 1][j], 0)
                if i != 0:
                    print "Adding edge ", house, i, j, " and ", i - 1, j
                    self.add_edge(house, neighborhood[i - 1][j], 0) 
                

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
        self.node_list[source].add_neighbor(self.node_list[dest], weight)

    # Get all nodes in the current graph
    def get_nodes(self):
        return self.node_list.keys()