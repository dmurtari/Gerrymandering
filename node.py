import sys, operator, itertools

# Defines a node, that node's contents, and the neighbors to that node and the
# edge weights to access that neighbor
class Node:

    # Initialize a node, with name containing the contents of the node,
    # and neighbors being a dictionary containing the neighbor's name as the 
    # key and the weight of the edge between them as the value
    def __init__(self, name):
        self.name = name
        self.neighbors = {}
        self.visited = False
        self.sccID = None
        self.pre = None
        self.post = None
        self.dist = 0

    # Accessor for the name
    def getName(self):
        return self.name

    # Accessor for the names of the neighbors to the current node
    def getNeighbors(self):
        return self.neighbors.keys()

    # Accessor for the weights of the neighbors to the current node
    def getWeight(self, neighbor):
        return self.neighbors[neighbor]

    # Add a neighbor to the current node, with the default being no weight
    def addNeighbor(self, neighbor, weight = 0):
        self.neighbors[neighbor] = weight