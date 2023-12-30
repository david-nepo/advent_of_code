"""Day 2: Inventory Management System."""


def get_input_as_list(filename: str) -> list[str]:
    """Gets input data as list of strings."""

    with open(filename, 'r', encoding='utf-8') as f:
        data = [row.strip() for row in f.readlines()]

    return data


def get_two_letter_count(id_str: str) -> int:
    """Get count of letters that appear twice."""

    unique_chars = set(id_str)

    for char in unique_chars:
        if id_str.count(char) == 2:
            return 1

    return 0


def get_three_letter_count(id_str: str) -> int:
    """Get count of letters that appear three times."""

    unique_chars = set(id_str)

    for char in unique_chars:
        if id_str.count(char) == 3:
            return 1

    return 0


def get_checksum(two_letter_count: int, three_letter_count: int) -> int:
    """Gets checksum by multiplying counts."""

    return two_letter_count * three_letter_count


def solve_part1() -> int:
    """Solves part 1."""

    data = get_input_as_list('input_day_2.txt')

    double_letters = 0
    triple_letters = 0

    for id_str in data:
        double_letters += get_two_letter_count(id_str)
        triple_letters += get_three_letter_count(id_str)

    return get_checksum(double_letters, triple_letters)


def solve_part2() -> str:
    """Solves part 2."""

    data = get_input_as_list('input_day_2.txt')

    found_pair = False

    for str_x in data:
        if found_pair:
            break

        for str_y in data:

            count = 0
            result_str = ""
            for char_x, char_y in zip(str_x, str_y):
                if char_x == char_y:
                    result_str += char_x
                else:
                    count += 1

            if count == 1:
                found_pair = True
                break

    return result_str


def main():
    """Main script."""

    print(f"Part 1: {solve_part1()}")
    print(f"Part 2: {solve_part2()}")


if __name__ == "__main__":
    main()
