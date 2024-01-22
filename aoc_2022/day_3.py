"""Day 3: Rucksack Reorganization."""

import string


def read_input(filename: str) -> list[str]:
    """Gets input from txt file."""

    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read().split('\n')

    return data


def split_rucksack(rucksack: str) -> list[str]:
    """Splits rucksack in half."""

    half = len(rucksack) // 2

    first_compartment = rucksack[:half]
    second_compartment = rucksack[half:]

    return [first_compartment, second_compartment]


def get_shared_letter(first_compartment: str, second_compartment: str) -> str:
    """Gets common letter between two compartments in rucksack."""

    set1 = set(first_compartment)
    set2 = set(second_compartment)

    return list(set1.intersection(set2))[0]


def convert_letter_to_priority(shared_letter: str) -> int:
    """Converts letter to priority."""

    alphabet = string.ascii_lowercase + string.ascii_uppercase

    for i, letter in enumerate(alphabet):
        if letter == shared_letter:
            return i + 1

    raise ValueError('No valid letter.')


def solve_part1(filename: str) -> int:
    """Main logic for Part 1."""

    puzzle_input = read_input(filename)

    total = 0
    for rucksack in puzzle_input:
        compartments = split_rucksack(rucksack)
        common_letter = get_shared_letter(compartments[0], compartments[1])
        priority = convert_letter_to_priority(common_letter)
        total += priority

    return total


def get_shared_letter_pt2(first_rucksack: str, second_rucksack: str, third_rucksack: str):
    """Gets shared letter between group of three rucksacks."""

    set1 = set(first_rucksack)
    set2 = set(second_rucksack)
    set3 = set(third_rucksack)

    return list(set1.intersection(set2).intersection(set3))[0]


def solve_part2(filename: str) -> int:
    """Main logic for Part 2."""

    puzzle_input = read_input(filename)

    total = 0
    for i in range(0, len(puzzle_input), 3):
        rucksacks = [puzzle_input[i], puzzle_input[i+1], puzzle_input[i+2]]
        common_letter = get_shared_letter_pt2(
            rucksacks[0], rucksacks[1], rucksacks[2])
        priority = convert_letter_to_priority(common_letter)
        total += priority

    return total


if __name__ == "__main__":
    print(f"Part 1: {solve_part1('input_day_3.txt')}")
    print(f"Part 2: {solve_part2('input_day_3.txt')}")
