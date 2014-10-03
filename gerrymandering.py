from graph import Graph

class Gerrymandering:
    
    def __init__(self, neighborhood_file = "./smallNeighborhood.txt"):
        """
        Initialize by reading in the data from a given file, and store the data
        in appropriate data structure
        """
        self.neighborhood = Graph(neighborhood_file)

        print "Neighborhood is: " + str(self.neighborhood)
             
def main():
    gerrymandering = Gerrymandering()

if __name__ == "__main__":
    main()