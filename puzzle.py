from piece import *
import numpy


# Matching with None always succeeds.

class Puzzle:
    def __init__(self, pieces):
        self.grid = [[None for i in range(6)] for j in range(6)]
        #  Grid is actually 4x4, additional 2 rows and columns represent the borders.
        #  The solution stores in fields self.grid[1:4][1:4]
        self.available_pieces = pieces
        self.next_piece_index = 0

    def check_state(self, state, x, y):

        # Check piece below:
        piece_down = self.grid[x][y-1]
        if piece_down is None:
            pass
        else:
            shapes_match = piece_down.current_state.up.shape == state.down.shape
            orientations_match = piece_down.current_state.up.orientation != state.down.orientation

            if shapes_match and orientations_match:
                pass
            else:
                return False

        # Check piece left:
        piece_left = self.grid[x-1][y]
        if piece_left is None:
            pass
        else:
            shapes_match = piece_left.current_state.right.shape == state.left.shape
            orientations_match = piece_left.current_state.right.orientation != state.left.orientation

            if shapes_match and orientations_match:
                pass
            else:
                return False

        # Check piece above:
        piece_up = self.grid[x][y+1]
        if piece_up is None:
            pass
        else:
            shapes_match = piece_up.current_state.down.shape == state.up.shape
            orientations_match = piece_up.current_state.down.orientation != state.up.orientation

            if shapes_match and orientations_match:
                pass
            else:
                return False

        # Check piece right:
        piece_right = self.grid[x+1][y]
        if piece_right is None:
            pass
        else:
            shapes_match = piece_right.current_state.left.shape == state.right.shape
            orientations_match = piece_right.current_state.right.orientation != state.right.orientation

            if shapes_match and orientations_match:
                pass
            else:
                return False

        return True

    def place_piece(self, piece, x, y):
        self.grid[x][y] = piece
        self.available_pieces.remove(piece)
        self.next_piece_index += 1




