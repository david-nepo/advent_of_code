"""Day 1: Chronal Calibration."""


def change_frequency(current_freq: int, change_in_freq: str) -> int:
    """Changes frequency after parsing number sign."""

    magnitude = int(change_in_freq[1:])
    sign = change_in_freq[0]

    return current_freq + magnitude if sign == "+" else current_freq - magnitude


def solve_part1() -> int:
    """Solves part 1."""

    with open('day_1_input.txt', 'r', encoding='utf-8') as f:
        puzzle_input = [row.strip() for row in f.readlines()]

    new_freq = 0
    for num in puzzle_input:
        new_freq = change_frequency(new_freq, num)

    return new_freq


def solve_part2() -> int:
    """Solves part 2."""

    with open('day_1_input.txt', 'r', encoding='utf-8') as f:
        puzzle_input = [row.strip() for row in f.readlines()]

    new_freq = 0
    freq_list = []

    while True:
        for num in puzzle_input:
            new_freq = change_frequency(new_freq, num)

            if new_freq in freq_list:
                return new_freq

            freq_list.append(new_freq)


def main():
    """Main script logic."""

    print(f"Part 1: {solve_part1()}")
    print(f"Part 2: {solve_part2()}")


if __name__ == "__main__":
    main()
