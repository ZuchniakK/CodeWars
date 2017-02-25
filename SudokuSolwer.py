def print_sudoku(puzzle):
    for i in puzzle:
        print(i)


def sudoku(puzzle):
    puzzle_solved = puzzle
    sudoku_size, grid_size = 9, 3
    while any(0 in row for row in puzzle_solved):
        for i in range(sudoku_size):
            for j in range(sudoku_size):
                if puzzle_solved[i][j] == 0:
                    exclusion = []
                    # elements in common sub grid
                    for m in range(i - i % grid_size, i - i % grid_size + grid_size):
                        for n in range(j - j % grid_size, j - j % grid_size + grid_size):
                            exclusion.append(puzzle_solved[m][n])
                    # elements in common row
                    exclusion.extend(puzzle_solved[i])
                    # elements in common column
                    exclusion.extend([puzzle_solved[m][j] for m in range(sudoku_size)])
                    # check what digits are posible
                    posible_elements = [k for k in range(1, 10) if k not in exclusion]
                    # if only one digit posible choose it, ale element = 0
                    puzzle_solved[i][j] = posible_elements[0] if len(posible_elements) == 1 else 0
    return puzzle_solved


if __name__ == '__main__':
    puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
              [6, 0, 0, 1, 9, 5, 0, 0, 0],
              [0, 9, 8, 0, 0, 0, 0, 6, 0],
              [8, 0, 0, 0, 6, 0, 0, 0, 3],
              [4, 0, 0, 8, 0, 3, 0, 0, 1],
              [7, 0, 0, 0, 2, 0, 0, 0, 6],
              [0, 6, 0, 0, 0, 0, 2, 8, 0],
              [0, 0, 0, 4, 1, 9, 0, 0, 5],
              [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    print_sudoku(puzzle)
    result = sudoku(puzzle)
    print(" ")
    print_sudoku(result)
