from graph import Graph

class Gerrymandering:
    
    def __init__(self, neighborhood_file = "./smallNeighborhood.txt"):
        """
        Initialize by reading in the data from a given file, and store the data
        in appropriate data structure
        """
        self.neighborhood_graph = Graph(neighborhood_file)
        neighborhood_file = open(neighborhood_file, "r")
        self.neighborhood = []
        edgecount = 0

        for line in neighborhood_file:
            self.neighborhood.append(line.strip().split(" "))
             
def main():
    gerrymandering = Gerrymandering()

if __name__ == "__main__":
    main()