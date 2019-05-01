from enum import Enum


class Shape(Enum):
    CIRCLE = 1
    CROSS = 2
    ARROW_OUT = 3
    ARROW_IN = 4


class Orientation(Enum):
    IN = 1
    OUT = 2


class Part:
    def __init__(self, shape: Shape, orientation: Orientation):
        self.shape = shape
        self.orientation = orientation


class Rotation(Enum):
    NONE = 0
    DEG90 = 1
    DEG180 = 2
    DEG270 = 3


class State:
    def __init__(self, part_left: Part, part_up: Part, part_right: Part, part_down: Part):
        self.left = part_left
        self.up = part_up
        self.right = part_right
        self.down = part_down


class Piece:
    def __init__(self, state: State):
        self.default_state = state
        self.current_state = state

    def rotate(self, rotation: Rotation):  # Clockwise rotation.
        if rotation == Rotation.NONE:
            self.current_state = self.default_state

        elif rotation == Rotation.DEG90:
            self.current_state = State(self.default_state.down, self.default_state.left, self.default_state.up,
                                       self.default_state.right)

        elif rotation == Rotation.DEG180:
            self.current_state = State(self.default_state.right, self.default_state.down, self.default_state.left,
                                       self.default_state.up)

        elif rotation == Rotation.DEG270:
            self.current_state = State(self.default_state.up, self.default_state.right, self.default_state.down,
                                       self.default_state.left)

    def flip(self):  # Flips piece on the other side - the result is mirrored state.
        pass

