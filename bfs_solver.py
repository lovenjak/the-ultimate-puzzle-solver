from initialize import *
from svg_generator import *
from puzzle import *
from copy import deepcopy


class BFSSolver:
    def __init__(self, pieces):
        self.possible_solutions = list()

        puzzle = Puzzle(pieces)
        self.possible_solutions.append(puzzle)

        self.mm = initialize_mapping_matrix()

    def solve(self):
        new_candidates = list()

        for solution in self.possible_solutions:
            n_available_pieces = len(solution.available_pieces)
            for piece_index in range(n_available_pieces):
                for rotation in [Rotation.NONE, Rotation.DEG90, Rotation.DEG180, Rotation.DEG270]:
                    x = self.mm[solution.next_piece_index][0][0]
                    y = self.mm[solution.next_piece_index][1][0]
                    piece = solution.available_pieces[piece_index]
                    piece.rotate(rotation)
                    state = piece.current_state

                    if solution.check_state(state, x, y):
                        solution_candidate = deepcopy(solution)
                        solution_candidate.place_piece(solution_candidate.available_pieces[piece_index], x, y)
                        new_candidates.append(solution_candidate)

        print(len(new_candidates))
        self.possible_solutions = new_candidates


if __name__ == "__main__":
    pieces = initialize_pieces()
    solver = BFSSolver(pieces)

    for i in range(16):
        solver.solve()

    print("**********")
    generate_svg_solution(solver.possible_solutions[0], 'solution')
