class Gerrymandering:
    
    def __init__(self, neighborhood_file = "./smallNeighborhood.txt"):
        """
        Initialize by reading in the data from a given file, and store the data
        in appropriate data structure
        """
        self.neighborhood_file = open(neighborhood_file, "r")
        self.neighborhood = []
        for line in self.neighborhood_file:
            self.neighborhood.append(line.strip())

        print("Neighborhood is: ", self.neighborhood)
             
def main():
    gerrymandering = Gerrymandering()

if __name__ == "__main__":
    main()
