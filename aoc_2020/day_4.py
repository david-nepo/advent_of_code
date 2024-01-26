"""Day 4: Passport Processing."""


MANDATORY_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']


def get_passports(filename: str) -> list[str]:
    """Get puzzle input as passports."""

    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read().split('\n\n')

    return [passport.replace('\n', ' ') for passport in data]


def separate_passport_fields(raw_passports: list[str]) -> list[str]:
    """Cleans raw passports to get fields."""

    data = [passport.split(' ') for passport in raw_passports]

    new_data = []
    for passport in data:
        new_data.append([field[:3] for field in passport])

    return new_data


def check_for_mandatory_fields(passport: str) -> bool:
    """Check if all mandatory fields in passport."""

    if len(passport) == 8 or len(passport) == 7 and 'cid' not in passport:
        return True

    return False


def solve_part1(filename: str):
    """Solves Part 1."""

    passports = get_passports(filename)
    passport_fields = separate_passport_fields(passports)

    total = 0
    for passport in passport_fields:
        total += 1 if check_for_mandatory_fields(passport) else 0

    return total


if __name__ == "__main__":
    print(f"Part 1: {solve_part1('input_day_4.txt')}")
