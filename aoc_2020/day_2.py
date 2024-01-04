"""Day 2: Password Philosophy."""


def read_input(filename: str) -> list[str]:
    """Get input as list of strings."""

    with open(filename, 'r', encoding='utf-8') as f:
        return [row.strip() for row in f.readlines()]


def get_lowest_number(input_line: str) -> int:
    """Gets lowest number policy letter must appear."""

    return int(input_line.split('-')[0])


def get_highest_number(input_line: str) -> int:
    """Gets highest number policy letter must appear."""

    policy_range = input_line.split(' ')[0]

    return int(policy_range.split('-')[1])


def get_policy_letter(input_line: str) -> str:
    """Gets policy letter."""

    sub_str = input_line.split(' ')[1]

    return sub_str[0]


def get_password(input_line: str) -> str:
    """Gets password."""

    return input_line.split(' ')[-1]


def is_valid(input_line: str) -> bool:
    """Returns true if password is valid."""

    lowest_num = get_lowest_number(input_line)
    highest_num = get_highest_number(input_line)
    policy_letter = get_policy_letter(input_line)
    password = get_password(input_line)

    return bool(lowest_num <= password.count(policy_letter) <= highest_num)


def solve_part1(filename: str) -> int:
    """Solves part 1."""

    password_list = read_input(filename)

    return sum(is_valid(password_policy) for password_policy in password_list)


def is_valid_pt2(input_line: str) -> bool:
    """Returns true if password is valid according to part 2."""

    lowest_num = get_lowest_number(input_line)
    highest_num = get_highest_number(input_line)
    policy_letter = get_policy_letter(input_line)
    password = get_password(input_line)

    check_str = password[lowest_num - 1] + password[highest_num - 1]

    return bool(check_str.count(policy_letter) == 1)


def solve_part2(filename: str) -> int:
    """Solves part 2."""

    password_list = read_input(filename)

    return sum(is_valid_pt2(password_policy) for password_policy in password_list)


def main():
    """Main script logic."""

    print(f"Part 1: {solve_part1('input_day_2.txt')}")
    print(f"Part 2: {solve_part2('input_day_2.txt')}")


if __name__ == "__main__":
    main()
