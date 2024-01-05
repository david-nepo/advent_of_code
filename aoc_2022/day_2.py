"""Day 2: Rock Paper Scissors."""


def read_input(filename: str) -> list[str]:
    """Reads in puzzle input as list of strings."""

    with open(filename, 'r', encoding='utf-8') as f:
        return [row.strip() for row in f.readlines()]


def get_opponent_shape(game: str) -> str:
    """Gets the shape opponent plays."""

    return game[0]


def get_your_shape(game: str) -> str:
    """Gets your shape."""

    return game[-1]


def get_result_points(game: str) -> int:
    """Gets points from result."""

    opp = get_opponent_shape(game)
    you = get_your_shape(game)
    play = opp + you

    win = ['CX', 'AY', 'BZ']
    draw = ['AX', 'BY', 'CZ']

    if play in win:
        return 6

    if play in draw:
        return 3

    return 0


def get_shape_points(your_shape: str) -> int:
    """Get points from shape selection."""

    shape_points = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    return shape_points.get(your_shape)


def solve_part1(filename: str) -> int:
    """Solves Part 1."""

    strategy_guide = read_input(filename)

    points = 0
    for game_play in strategy_guide:
        your_shape = get_your_shape(game_play)
        points += get_result_points(game_play) + get_shape_points(your_shape)

    return points


def get_result_points_2(game: str) -> int:
    """Get result points according to Part 2."""

    result = game[-1]

    result_points = {
        'X': 0,
        'Y': 3,
        'Z': 6
    }

    return result_points.get(result)


def determine_your_shape(game: str) -> str:
    """Determines your shape."""

    you = get_your_shape(game)
    opp = get_opponent_shape(game)

    shape_finder_dict = {
        'X': ['BX', 'CY', 'AZ'],
        'Y': ['AX', 'BY', 'CZ'],
        'Z': ['CX', 'AY', 'BZ']
    }

    potential_outcomes = shape_finder_dict.get(you)

    return [outcome[1] for outcome in potential_outcomes if outcome.startswith(opp)][0]


def solve_part2(filename: str) -> int:
    """Solves part 2."""

    strategy_guide = read_input(filename)

    points = 0
    for game_play in strategy_guide:
        your_shape = determine_your_shape(game_play)
        points += get_result_points_2(game_play) + get_shape_points(your_shape)

    return points


def main():
    """Main script logic."""

    filename = 'input_day_2.txt'

    print(f"Part 1: {solve_part1(filename)}")
    print(f"Part 2: {solve_part2(filename)}")


if __name__ == "__main__":
    main()
