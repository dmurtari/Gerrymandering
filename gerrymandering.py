
class Gerrymandering:
    
    def __init__(self, neighborhood_file = "./smallNeighborhood.txt"):
        """
        Initialize by reading in the data from a given file, and store the data
        in appropriate data structure
        """
        neighborhood_file = open(neighborhood_file, "r")
        self.neighborhood = []

        for line in neighborhood_file:
            self.neighborhood.append([line.strip().split(" "), 0])

        self.region_size = len(self.neighborhood)
        self.vertical = []
        self.horizontal = []
        self.square = []

        for i in range(self.region_size):
            self.vertical.append([0, i])
            self.horizontal.append([i, 0])

        for i in range(self.region_size/2):
            for j in range(self.region_size/2):
                self.square.append([i, j])

    # def generate_moves():

             
def main():
    gerrymandering = Gerrymandering("./largeNeighborhood.txt")

if __name__ == "__main__":
    main()