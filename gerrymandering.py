from tree import Node
from Queue import Queue
from copy import deepcopy, copy

class Gerrymandering:

    def __init__(self, neighborhood_file = "./smallNeighborhood.txt"):
        """
        Initialize by reading in the data from a given file, and store the data
        in a 2D array. Also create a corrosponding array to hold region 
        information, where MAX is represented by an even number, MIN is 
        represented by an odd number, and if a region has not been selected by
        either it is represented by 0
        """

        # Store neighborhood information in a 2D array
        neighborhood_file = open(neighborhood_file, "r")
        self.neighborhood = []
        for line in neighborhood_file:
            self.neighborhood.append(line.strip().split(" "))

        # Region size is equal to the length of one of the sides of the 
        # neighborhood, since neighboorhoods are square
        self.region_size = len(self.neighborhood)

        # Represent the regions selected by MAX and MIN. Initially filled with
        # all 0's since neither has picked a region yet
        self.selected_regions = [[0]*self.region_size \
                                 for i in range(self.region_size)]
       
        # Generate the shapes that regions can be defined as, where n is the 
        # length of the sides of the neighborhood.
        vertical = []   # Vertical line of length n 
        horizontal = [] # Horizontal line of length n
        square = []     # Square of dimensions n/2 x n/2

        for i in range(self.region_size):
            vertical.append([0, i])
            horizontal.append([i, 0])

        for i in range(self.region_size/2):
            for j in range(self.region_size/2):
                square.append([i, j])

        self.shapes = [vertical, horizontal, square]
        self.generate_moves()

    def generate_moves(self):
        """
        Generate a tree of available moves. Iterate through the array of 
        available regions, generating a tree where each node represents a 
        possible configuration of regions. Root node is the state where nothing
        has been selected, root's children are where one move has been made, 
        children's children are where two moves have been made, etc.
        """

        current_player = 0
        root_move = Node(self.selected_regions, current_player)
        queue = Queue()
        queue.put(root_move)

        while not queue.empty():
            print queue.qsize()
            selected_parent = queue.get()
            current_player = selected_parent.get_player()
            for i in range(self.region_size):
                for j in range(self.region_size):
                    if selected_parent.get_value()[i][j] == 0:
                        for shape in self.shapes:
                            selected_child = self.fit_shape(shape, \
                                selected_parent.get_value(), (i, j), \
                                current_player + 1)
                            if selected_child:
                                child_node = Node(selected_child, \
                                                  current_player + 1)
                                queue.put(child_node)
                                selected_parent.add_child(child_node)

    def fit_shape(self, shape, selected_regions, starting_coords, player):
        """
        See if a given shape will fit in the available space, where the shape 
        will start at a given set of starting coordinates. If the shape fits, 
        then designate the region that that shape covers as being a district 
        that the current player owns (even for MAX, odd for MIN), and return 
        the updated configuration to the caller
        """

        selected_region=deepcopy(selected_regions)
        x, y = starting_coords
        for i in range(len(shape)):
            dx = x + shape[i][0]
            dy = y + shape[i][1]

            if dx >= self.region_size or dy >= self.region_size or \
                not selected_region[dx][dy] == 0:
                return None
            selected_region[dx][dy] = player
        return selected_region

    def evaluate(self, region):
        """
        Evaluates a given region according to the current player. Uses
        the function suggested on the worksheet, giving greater weight to 
        configurations that group the opposing player and give the current 
        player a majority
        """

        # Sum of even (MAX) and off (MIN) elements. Don't currently do anything
        # with the sum of even elements, but calculate anyways
        even_sum = 0
        odd_sum = 0 

        for element in region:
            if element == 0:
                return -1
            elif element % 2 == 0:
                even_sum += 1
            else:
                odd_sum += 1

        # Score is good if MINs are grouped together, not as good if a lot of
        # MAXs are grouped together
        return odd_sum + 1


def main():
    gerrymandering = Gerrymandering("./smallNeighborhood.txt")

if __name__ == "__main__":
    main()
