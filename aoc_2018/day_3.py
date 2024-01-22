"""Day 3: No Matter How You Slice It."""


if __name__ == "__main__":

    row_length = 11
    col_height = 9
    grid = [[0 for _ in range(row_length)] for _ in range(col_height)]
    for row in range(col_height):
        for col in range(row_length):
            grid[row][col] == 0

    for row in grid:
        print(row)
