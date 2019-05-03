import pickle
import svgwrite
from copy import deepcopy
from initialize import *
from piece import *
from misc import *
from bfs_solver import *


class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


class PartGeometryFactory:
    def __init__(self):
        self.base_geometry = dict()
        self.base_geometry[Shape.ARROW_IN] = [(0, 2), (1, 1), (1, 2), (1.5, 2),
                                              (1.5, 3), (1, 3), (1, 4), (0, 3)]
        self.base_geometry[Shape.ARROW_OUT] = [(0, 2), (0.5, 2), (0.5, 1),
                                               (2, 2.5), (0.5, 4), (0.5, 3),
                                               (0, 3)]
        self.base_geometry[Shape.CIRCLE] = [(0, 2), (0.5, 1.5), (1, 1.5), (1.5, 2),
                                            (1.5, 3), (1, 3.5), (0.5, 3.5),
                                            (0, 3)]
        self.base_geometry[Shape.CROSS] = [(0, 2), (0.5, 2), (0.5, 1.5), (1, 1.5),
                                           (1, 2), (1.5, 2), (1.5, 3), (1, 3),
                                           (1, 3.5), (0.5, 3.5), (0.5, 3), (0, 3)]

    @staticmethod
    def switch_xy(geometry):
        switched_geometry = list()
        for (x, y) in geometry:
            switched_geometry.append((y, x))

        return switched_geometry

    @staticmethod
    def mirror_y(geometry):
        mirrored_geometry = list()
        for (x, y) in geometry:
            mirrored_geometry.append((-x, y))

        return mirrored_geometry

    @staticmethod
    def mirror_x(geometry):
        mirrored_geometry = list()
        for (x, y) in geometry:
            mirrored_geometry.append((x, -y))

        return mirrored_geometry

    @staticmethod
    def translate(geometry, translation):
        translated_geometry = list()
        (x_t, y_t) = translation
        for (x, y) in geometry:
            translated_geometry.append((x + x_t, y + y_t))

        return translated_geometry

    def __call__(self, shape: Shape, direction: Direction, orientation: Orientation):
        geometry = deepcopy(self.base_geometry[shape])

        if direction == Direction.LEFT:
            if orientation == Orientation.IN:
                return geometry
            elif orientation == Orientation.OUT:
                return self.mirror_y(geometry)

        if direction == Direction.RIGHT:
            if orientation == Orientation.OUT:
                return self.translate(geometry, (5, 0))
            elif orientation == Orientation.IN:
                return self.translate(self.mirror_y(geometry), (5, 0))

        switched_geometry = self.switch_xy(geometry)

        if direction == Direction.UP:
            if orientation == Orientation.IN:
                return switched_geometry
            elif orientation == Orientation.OUT:
                return self.mirror_x(switched_geometry)

        elif direction == Direction.DOWN:
            if orientation == Orientation.OUT:
                return self.translate(switched_geometry, (0, 5))
            elif orientation == Orientation.IN:
                return self.translate(self.mirror_x(switched_geometry), (0, 5))


class PieceGeometryFactory:
    def __init__(self, scale=1):
        self.scale = 1/5 * scale

    def scale_geometry(self, geometry):
        scaled_geometry = list()
        for (x, y) in geometry:
            scaled_geometry.append((x * self.scale, y * self.scale))

        return scaled_geometry

    @staticmethod
    def reverse_geometry(geometry):
        reversed_geometry = list()
        for point in geometry:
            reversed_geometry.insert(0, point)

        return reversed_geometry

    def __call__(self, piece):
        pgf = PartGeometryFactory()
        piece_geometry = list()

        piece_geometry.append((0, 0))
        left_part = piece.current_state.left
        piece_geometry += pgf(left_part.shape, Direction.LEFT, left_part.orientation)

        piece_geometry.append((0, 5))
        down_part = piece.current_state.down
        piece_geometry += pgf(down_part.shape, Direction.DOWN, down_part.orientation)

        piece_geometry.append((5, 5))
        right_part = piece.current_state.right
        piece_geometry += self.reverse_geometry(pgf(right_part.shape, Direction.RIGHT, right_part.orientation))

        piece_geometry.append((5, 0))
        up_part = piece.current_state.up
        piece_geometry += self.reverse_geometry(pgf(up_part.shape, Direction.UP, up_part.orientation))

        return self.scale_geometry(piece_geometry)


def translate_piece_geometry(geometry, translation):
    translated_geometry = list()
    (x_t, y_t) = translation

    for (x, y) in geometry:
        translated_geometry.append((x + x_t, y + y_t))

    return translated_geometry


def create_svg_solution(solution, filename, scale=100):
    piece_geometry_factory = PieceGeometryFactory(scale)
    mm = initialize_mapping_matrix()

    dwg = svgwrite.Drawing(filename, (scale * 6, scale * 6), debug=True)
    pieces_svg = dwg.add(dwg.g(id='original-pieces', stroke='black', fill='gray'), )

    for i in range(16):
        x = mm[i][0][0]
        y = mm[i][1][0]
        piece = solution.grid[x][y]
        piece_geometry = piece_geometry_factory(piece)

        translated_pg = translate_piece_geometry(piece_geometry, (x * scale, y * scale))
        pieces_svg.add(dwg.polygon(translated_pg))

    dwg.save()


if __name__ == "__main__":
    solver_pickle = open('solver.obj', 'rb')
    solver = pickle.load(solver_pickle)

    print_solution(solver.possible_solutions[0])


    create_svg_solution(solver.possible_solutions[0], "solution2")

    scale = 100
