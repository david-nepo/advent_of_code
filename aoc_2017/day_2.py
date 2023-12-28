"""Day 2: Corruption Checksum."""


def convert_str_to_int(input_row: str) -> list[int]:
    """Converts input row from string to list of integers."""

    input = input_row.split()

    return [int(num) for num in input]


def get_difference(input_row: list[int]) -> int:
    """For each row, gets the difference between largest and smallest value."""

    return max(input_row) - min(input_row)


def get_checksum(differences: list[int]) -> int:
    """Sums all the differences from each row."""

    return sum(differences)


if __name__ == "__main__":

    with open('day_2.txt', 'r', encoding='utf-8') as f:
        data = [row for row in f.readlines()]

    data = [convert_str_to_int(row) for row in data]
    differences = [get_difference(row) for row in data]
    print(get_checksum(differences))
