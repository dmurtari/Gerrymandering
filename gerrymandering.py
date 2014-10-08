from sys import argv
from tree import Node
from Queue import Queue
from copy import deepcopy, copy

fitting = 0

class Gerrymandering:

    def __init__(self, neighborhood_file = "smallNeighborhood.txt"):
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
        self.queue = Queue()
        self.max_player = "D"
        self.min_player = "R"

    def generate_moves(self, depth, selected_regions):
        """
        Generate a tree of available moves. Iterate through the array of 
        available regions, generating a tree where each node represents a 
        possible configuration of regions. Root node is the state where nothing
        has been selected, root's children are where one move has been made, 
        children's children are where two moves have been made, etc.
        """

        current_player = 0
        root_move = Node(selected_regions, current_player)
        self.queue = Queue()

        self.queue.put(root_move)
        while not self.queue.empty():
            selected_parent = self.queue.get()
            current_player = selected_parent.get_player()
            print "self.queuesize", self.queue.qsize()
            if current_player > depth:
                print "broke"
                break
            for k, shape in enumerate(self.shapes):
                if k == 0:
                    self.fit_vertical(selected_parent.get_value(), current_player, selected_parent)
                elif k == 1:
                    self.fit_horizontal(selected_parent.get_value(), current_player, selected_parent)
                else:
                    self.fit_square(selected_parent.get_value(), current_player, selected_parent)

                """
                for i in range(self.region_size):
                    for j in range(self.region_size):
                        if selected_parent.get_value()[i][j] == 0:
                            selected_child = self.fit_shape(shape, \
                                selected_parent.get_value(), (i, j), \
                                current_player + 1)
                            if selected_child:
                                child_node = Node(selected_child, \
                                                  current_player + 1)
                                queue.put(child_node)
                                selected_parent.add_child(child_node)
                                """
        return root_move
        

    def fit_horizontal(self, selected_regions, current_player, selected_parent):
        for i in range(self.region_size):
            if selected_regions[i][0] == 0:
                current_child = self.select_child(self.shapes[0], selected_regions, \
                    current_player, (i, 0))
                if current_child:
                    self.queue.put(current_child)
                    selected_parent.add_child(current_child)

    def fit_vertical(self, selected_regions, current_player, selected_parent):
        for i in range(self.region_size):
            if selected_regions[0][i] == 0:
                current_child = self.select_child(self.shapes[1], selected_regions, \
                    current_player, (0, i))
                if current_child:
                    self.queue.put(current_child)
                    selected_parent.add_child(current_child)

    def fit_square(self, selected_regions, current_player, selected_parent):
        for i in range(self.region_size/2 + 1):
            for j in range(self.region_size/2 + 1):
                if selected_regions[i][j] :
                    current_child = self.select_child(self.shapes[2], selected_regions, \
                        current_player, (i, j))                    
                    if current_child:
                        self.queue.put(current_child)
                        selected_parent.add_child(current_child)

    def select_child(self, shape, selected_regions, current_player, coords):
        i, j = coords
        selected_child = self.fit_shape(shape, \
                                selected_regions, (i, j), \
                                current_player + 1)
        if selected_child:
            return Node(selected_child, current_player + 1)
        else:
            return None


    def fit_shape(self, shape, selected_regions, starting_coords, player):
        """
        See if a given shape will fit in the available space, where the shape 
        will start at a given set of starting coordinates. If the shape fits, 
        then designate the region that that shape covers as being a district 
        that the current player owns (even for MAX, odd for MIN), and return 
        the updated configuration to the caller
        """
        global fitting
        fitting = fitting + 1
        print fitting

        selected_region = deepcopy(selected_regions)
        x, y = starting_coords
        for i in range(len(shape)):
            dx = x + shape[i][0]
            dy = y + shape[i][1]

            if dx >= self.region_size or dy >= self.region_size or \
                not selected_region[dx][dy] == 0:
                return None
            selected_region[dx][dy] = player

        return selected_region

    def evaluate_board(self, game_state, should_print = False):
        """
        Evaluates the board state for the max_player, and returns the number
        of districts that the max_player has won
        """
        districts_won = 0

        # Region dict holds the number of max_player's elements present in each
        # district. E.g. if a district is designated by a 1, and there are 3
        # D's in 1 (where D is the max_player), then region_dict = {1: 3}
        region_dict = {}
        for row in game_state:
            for elt in row:
                region_dict[elt] = 0

        for i, row in enumerate(self.neighborhood):
            for j, elt in enumerate(row):
                if elt == self.min_player and game_state[i][j] % 2 == 0 and \
                    not game_state[i][j] == 0:
                    region_dict[game_state[i][j]] += 1

        for player, count in region_dict.iteritems():
            if count > self.region_size/2:
                districts_won += 1
                if should_print:
                    print "District", str(player) + ":", self.min_player
            elif count == self.region_size/2 and should_print:
                print "District", str(player) + ": Tied"
            elif count < self.region_size/2 and should_print:
                print "District", str(player) + ":", self.max_player

        if should_print:
            if districts_won > self.region_size/2:
                print "Election outcome:", self.min_player, "wins"
            elif districts_won == self.region_size/2:
                print "Election outcome: Tie"
            else:
                print "Election outcome:", self.max_player, "wins"     


        return districts_won

    def minimax(self, node, depth, player):
        """
        Perform a minimax search from a given node, to a given depth, from the
        perspective of a given player. 
        """
        if depth == 0 or len(node.get_children()) == 0:
            for row in node.get_value():
                if 0 in row:
                    print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
                    node = self.generate_moves(depth, node.get_value())
                    print node.get_children()
                    if len(node.get_children()) == 0:
                        return (self.evaluate_board(node.get_value()), node.get_value())
                    self.minimax(node, depth - 1, player)
            return (self.evaluate_board(node.get_value()), node.get_value())
                    
        elif player == self.min_player:
            best_value = -float("inf")
            for child in node.get_children():
                value, board = self.minimax(child, depth - 1, self.max_player)
                if value > best_value:
                    best_value = value
                    best_board = board
            return (best_value, best_board)
        else:
            best_value = float("inf")
            for child in node.get_children():
                value, board = self.minimax(child, depth - 1, self.min_player)
                if value < best_value:
                    best_value = value
                    best_board = board
            return (best_value, board)

    def generate_output(self, board):
        """
        Outputs required information for grading for a given board.
        """
        districts = {}

        print "MAX =", self.max_player
        print "MIN =", self.min_player
        print ""

        print "Board is:"
        for row in board:
            print row
            for elt in row:
                districts[elt] = []
        print ""

        for i, row in enumerate(board):
            for j, elt in enumerate(row):
                districts[elt] += [(i, j)]

        districts = iter(sorted(districts.items()))

        for owner, coords in districts:
            print "District", str(owner) + ":", coords
        print ""

        self.evaluate_board(board, should_print=True)

def main():
    gerrymandering = Gerrymandering(argv[1])
    node = gerrymandering.generate_moves(2, gerrymandering.selected_regions)
    value, board = gerrymandering.minimax(node, 2, "R")
    gerrymandering.generate_output(board)

if __name__ == "__main__":
    main()
