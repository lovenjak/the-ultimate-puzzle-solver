from piece import *


def initialize_pieces():
    pieces = list()

    state1 = State(Part(Shape.CIRCLE, Orientation.OUT),
                   Part(Shape.CROSS, Orientation.OUT),
                   Part(Shape.CROSS, Orientation.IN),
                   Part(Shape.CIRCLE, Orientation.IN))
    pieces.append(Piece(state1))

    state2 = State(Part(Shape.ARROW_OUT, Orientation.OUT),
                   Part(Shape.ARROW_OUT, Orientation.OUT),
                   Part(Shape.CIRCLE, Orientation.IN),
                   Part(Shape.ARROW_IN, Orientation.IN))
    pieces.append(Piece(state2))

    state3 = State(Part(Shape.ARROW_IN, Orientation.OUT),
                   Part(Shape.ARROW_IN, Orientation.OUT),
                   Part(Shape.CIRCLE, Orientation.IN),
                   Part(Shape.CROSS, Orientation.IN))
    pieces.append(Piece(state3))

    state4 = State(Part(Shape.CIRCLE, Orientation.OUT),
                   Part(Shape.ARROW_IN, Orientation.OUT),
                   Part(Shape.CROSS, Orientation.IN),
                   Part(Shape.ARROW_IN, Orientation.IN))
    pieces.append(Piece(state4))

    state5 = State(Part(Shape.ARROW_IN, Orientation.OUT),
                   Part(Shape.ARROW_OUT, Orientation.OUT),
                   Part(Shape.ARROW_OUT, Orientation.IN),
                   Part(Shape.CIRCLE, Orientation.IN))
    pieces.append(Piece(state5))

    state6 = State(Part(Shape.ARROW_OUT, Orientation.OUT),
                   Part(Shape.CIRCLE, Orientation.OUT),
                   Part(Shape.CIRCLE, Orientation.IN),
                   Part(Shape.ARROW_OUT, Orientation.IN))
    pieces.append(Piece(state6))

    state7 = State(Part(Shape.CIRCLE, Orientation.OUT),
                   Part(Shape.ARROW_IN, Orientation.OUT),
                   Part(Shape.ARROW_IN, Orientation.IN),
                   Part(Shape.ARROW_OUT, Orientation.IN))
    pieces.append(Piece(state7))

    state8 = State(Part(Shape.ARROW_OUT, Orientation.OUT),
                   Part(Shape.CIRCLE, Orientation.OUT),
                   Part(Shape.CIRCLE, Orientation.IN),
                   Part(Shape.CROSS, Orientation.IN))
    pieces.append(Piece(state8))

    state9 = State(Part(Shape.ARROW_IN, Orientation.OUT),
                   Part(Shape.ARROW_IN, Orientation.OUT),
                   Part(Shape.ARROW_OUT, Orientation.IN),
                   Part(Shape.CROSS, Orientation.IN))
    pieces.append(Piece(state9))

    state10 = State(Part(Shape.CIRCLE, Orientation.OUT),
                    Part(Shape.CROSS, Orientation.OUT),
                    Part(Shape.ARROW_OUT, Orientation.IN),
                    Part(Shape.ARROW_OUT, Orientation.IN))
    pieces.append(Piece(state10))

    state11 = State(Part(Shape.CIRCLE, Orientation.OUT),
                    Part(Shape.CIRCLE, Orientation.OUT),
                    Part(Shape.CIRCLE, Orientation.IN),
                    Part(Shape.ARROW_OUT, Orientation.IN))
    pieces.append(Piece(state11))

    state12 = State(Part(Shape.CIRCLE, Orientation.OUT),
                    Part(Shape.ARROW_IN, Orientation.OUT),
                    Part(Shape.CIRCLE, Orientation.IN),
                    Part(Shape.CROSS, Orientation.IN))
    pieces.append(Piece(state12))

    state13 = State(Part(Shape.ARROW_IN, Orientation.OUT),
                    Part(Shape.CROSS, Orientation.OUT),
                    Part(Shape.ARROW_OUT, Orientation.IN),
                    Part(Shape.ARROW_IN, Orientation.IN))
    pieces.append(Piece(state13))

    state14 = State(Part(Shape.CROSS, Orientation.OUT),
                    Part(Shape.ARROW_OUT, Orientation.OUT),
                    Part(Shape.ARROW_OUT, Orientation.IN),
                    Part(Shape.CIRCLE, Orientation.IN))
    pieces.append(Piece(state14))

    state15 = State(Part(Shape.CIRCLE, Orientation.OUT),
                    Part(Shape.CROSS, Orientation.OUT),
                    Part(Shape.ARROW_IN, Orientation.IN),
                    Part(Shape.CIRCLE, Orientation.IN))
    pieces.append(Piece(state15))

    state16 = State(Part(Shape.CROSS, Orientation.OUT),
                    Part(Shape.ARROW_OUT, Orientation.OUT),
                    Part(Shape.CROSS, Orientation.IN),
                    Part(Shape.ARROW_IN, Orientation.IN))
    pieces.append(Piece(state16))

    return pieces


def initialize_mapping_matrix():
    mm = list()

    for i in range(1, 5):
        for j in range(1, 5):
            mm.append([[i], [j]])

    return mm
