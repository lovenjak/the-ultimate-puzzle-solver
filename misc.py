def print_solution(solution):
    for i in range(1, 5):
        for j in range(1, 5):
            print("(x, y): ({}, {})", i, j)
            print("UP: {}, {}".format(solution.grid[i][j].current_state.up.shape,
                  solution.grid[i][j].current_state.up.orientation))
            print("RIGHT: {}, {}".format(solution.grid[i][j].current_state.right.shape,
                  solution.grid[i][j].current_state.right.orientation))
            print("DOWN: {}, {}".format(solution.grid[i][j].current_state.down.shape,
                  solution.grid[i][j].current_state.down.orientation))
            print("LEFT: {}, {}".format(solution.grid[i][j].current_state.left.shape,
                  solution.grid[i][j].current_state.left.orientation))
            print("**********")
