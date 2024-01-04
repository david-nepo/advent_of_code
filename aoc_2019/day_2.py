"""Day 2: 1202 Program Alarm."""


def get_input_data(filename: str) -> list[int]:
    """Reads in input data."""

    with open(filename, 'r', encoding='utf-8') as f:
        return [int(char) for char in f.readline().split(',')]


def solve_part1() -> int:
    """Solves part 1."""

    puzzle_input = get_input_data('inputs_day_2.txt')
    puzzle_input[1] = 12
    puzzle_input[2] = 2

    for i in range(0, len(puzzle_input)-4, 4):
        subset = puzzle_input[i:i+4]

        if subset[0] == 1:
            puzzle_input[subset[3]] = (
                puzzle_input[subset[1]] + puzzle_input[subset[2]])

        if subset[0] == 2:
            puzzle_input[subset[3]] = (
                puzzle_input[subset[1]] * puzzle_input[subset[2]])

        if subset[0] == 99:
            break

    return puzzle_input[0]


def calculate_program_output(original_input: list[int], noun_val: int, verb_val: int) -> int:
    """Calculates program output."""

    original_input[1] = noun_val
    original_input[2] = verb_val

    for i in range(0, len(original_input)-4, 4):
        subset = original_input[i:i+4]

        if subset[0] == 1:
            original_input[subset[3]] = (
                original_input[subset[1]] + original_input[subset[2]])

        elif subset[0] == 2:
            original_input[subset[3]] = (
                original_input[subset[1]] * original_input[subset[2]])

        elif subset[0] == 99:
            break

    return original_input[0]


def solve_part2() -> int:
    """Solves part 2."""

    puzzle_input = get_input_data('inputs_day_2.txt')

    noun_vals = list(range(100))
    verb_vals = list(range(100))

    combos = [(a, b) for a in noun_vals for b in verb_vals]

    for combo in combos:
        noun = combo[0]
        verb = combo[1]

        result = calculate_program_output(puzzle_input.copy(), noun, verb)

        if result == 19690720:
            return 100 * noun + verb


def main():
    """Main script logic."""

    print(f"Part 1: {solve_part1()}")
    print(f"Part 2: {solve_part2()}")


if __name__ == "__main__":
    main()
