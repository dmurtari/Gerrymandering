from tree import Node
from Queue import Queue

class Gerrymandering:

    def __init__(self, neighborhood_file = "./smallNeighborhood.txt"):
        """
        Initialize by reading in the data from a given file, and store the data
        in appropriate data structure
        """
        neighborhood_file = open(neighborhood_file, "r")
        self.neighborhood = []

        for line in neighborhood_file:
            self.neighborhood.append(line.strip().split(" "))

        self.region_size = len(self.neighborhood)

        self.selected_regions = [[0]*self.region_size]*self.region_size
        vertical = []
        horizontal = []
        square = []

        for i in range(self.region_size):
            vertical.append([0, i])
            horizontal.append([i, 0])

        for i in range(self.region_size/2):
            for j in range(self.region_size/2):
                square.append([i, j])

        self.shapes = [vertical, horizontal, square]
        self.generate_moves()

    def generate_moves(self):
        root_move = Node(self.selected_regions)
        queue = Queue()
        queue.put(root_move)
        while not queue.empty():
            selected_parent = queue.get()
            print selected_parent
            for i in range(self.region_size):
                for j in range(self.region_size):
                    for shape in self.shapes:
                        selected_child = self.fit_shape(shape, selected_parent.get_value(), (i, j), 2)
                        if selected_child:
                            child_node = Node(selected_child)
                            queue.put(child_node)
                            selected_parent.add_child(child_node)

    def fit_shape(self, shape, selected_regions, starting_coords, player):
        x, y = starting_coords
        # print len(shape)
        for i in range(len(shape)):
            dx = x + shape[i][0]
            dy = y + shape[i][1]
            # if len(shape) == 16:
            #     print "HEYY " + str(dx)
            #     print shape
            if dx >= self.region_size or dy >= self.region_size or not selected_regions[dx][dy] == 0:
                return None
            # print selected_regions
            selected_regions[dx][dy] = player
        return selected_regions

def main():
    gerrymandering = Gerrymandering("./largeNeighborhood.txt")

if __name__ == "__main__":
    main()
