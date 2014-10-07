from tree import Node
from Queue import Queue
from copy import deepcopy, copy

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

        self.selected_regions = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
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
            for i in range(self.region_size):
                for j in range(self.region_size):
                    if selected_parent.get_value()[i][j] == 0:
                        for shape in self.shapes:
                            selected_child = self.fit_shape(shape, selected_parent.get_value(), (i, j), 2)
                            if selected_child:
                                child_node = Node(selected_child)
                                queue.put(child_node)
                                selected_parent.add_child(child_node)

    def fit_shape(self, shape, selected_regions, starting_coords, player):
        selected_region=deepcopy(selected_regions)
        x, y = starting_coords
        for i in range(len(shape)):
            dx = x + shape[i][0]
            dy = y + shape[i][1]

            if dx >= self.region_size or dy >= self.region_size or not selected_region[dx][dy] == 0:
                return None
            selected_region[dx][dy] = player
        return selected_region

def main():
    gerrymandering = Gerrymandering("./smallNeighborhood.txt")

if __name__ == "__main__":
    main()
