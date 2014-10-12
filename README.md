Gerrymandering
==============

Gerrymandering implemented using minimax search

Run with: `python gerrymandering.py <neighborhood file>`

Algorithm:

1. Generate a tree of possible moves. Possible moves are represented by a
   2D array of the same size as the neighborhood array. The root node is the
   state where nobody has made a move, and children are each possible move 
   by either player from the node.
2. Perform a minimax search on the tree of possible moves. The value of each
   node is given as the number of districts that the max_player has won. 