"""Day 1: Inverse Captcha."""


def append_first_digit(input_seq: str) -> str:
    """Takes first digit and adds it to the end of the sequence."""

    return input_seq + input_seq[0]


def get_matching_digits(appended_input: str) -> list[int]:
    """Gets the matching digits that need to be summmed."""

    matching_digits = []
    for i in range(len(appended_input) - 1):
        if appended_input[i] == appended_input[i+1]:
            matching_digits.append(int(appended_input[i]))

    return matching_digits


def sum_matching_digits(matching_digits: list[str]) -> int:
    """Sums matching digits."""

    return sum(matching_digits)


def solve_part1(input_seq: str = None) -> int:
    """Solves Part 1."""

    if input_seq is None:
        with open('day_1_input.txt', 'r') as f:
            input_seq = f.readline()

    return sum_matching_digits(get_matching_digits(append_first_digit(input_seq)))


def solve_part2(input_seq: str = None) -> int:
    """Solves Part 2."""

    if input_seq is None:
        with open('day_1_input.txt', 'r') as f:
            input_seq = f.readline()

    comparison_gap = len(input_seq) // 2

    matching_digits = []
    for i in range(len(input_seq)):
        linked_list = input_seq[i:] + input_seq[:i]
        if linked_list[0] == linked_list[comparison_gap]:
            matching_digits.append(int(linked_list[0]))

    return sum(matching_digits)


if __name__ == "__main__":

    print(f"Part 1: {solve_part1()}")
    print(f"Part 2: {solve_part2()}")
