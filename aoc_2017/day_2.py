"""Day 2: Corruption Checksum."""


def convert_str_to_int(input_row: str) -> list[int]:
    """Converts input row from string to list of integers."""

    input_int = input_row.split()

    return [int(num) for num in input_int]


def get_difference(input_row: list[int]) -> int:
    """For each row, gets the difference between largest and smallest value."""

    return max(input_row) - min(input_row)


def get_checksum(differences: list[int]) -> int:
    """Sums all the differences from each row."""

    return sum(differences)


def solve_part1() -> int:
    """Solves part 1."""

    with open('day_2.txt', 'r', encoding='utf-8') as f:
        data = list(f.readlines())

    data = [convert_str_to_int(row) for row in data]
    differences = [get_difference(row) for row in data]

    return get_checksum(differences)


def get_evenly_divisible_values(input_row: list[int]) -> int:
    """Gets result of dividing evenly divisible values."""

    for i in input_row:
        for j in input_row:
            if not i % j and i // j != 1:
                return i // j
    return 0


def solve_part2() -> int:
    """Solves part 2."""

    with open('day_2.txt', 'r', encoding='utf-8') as f:
        data = list(f.readlines())

    data = [convert_str_to_int(row) for row in data]
    results = [get_evenly_divisible_values(row) for row in data]

    return get_checksum(results)


def main():
    """Main script logic."""

    print(f"Part 1: {solve_part1()}")
    print(f"Part 2: {solve_part2()}")


if __name__ == "__main__":
    main()
