"""Day 5: Doesn't He Have Intern-Elves For This?"""

import re


def contains_bad_substrings(input_string: str) -> bool:
    """Checks if string contains naughty substrings."""

    naughty_substrings = ['ab', 'cd', 'pq', 'xy']

    for substring in naughty_substrings:
        if substring in input_string:
            return True

    return False


def contains_three_vowels(input_string: str) -> bool:
    """Checks if string contains three vowels."""

    vowels = 'aeiou'
    vowel_count = sum(1 for char in input_string if char in vowels)

    return bool(vowel_count >= 3)


def contains_double_letter(input_string: str) -> bool:
    """Checks if string contains double letter."""

    pattern = re.compile(r'(.)\1')

    return bool(pattern.search(input_string))


def solve_part1():
    """Solves Part 1."""

    with open('day_5_input.txt', 'r', encoding='utf-8') as f:
        data = [str.strip() for str in f.readlines()]

    total = 0
    for string in data:
        if (
            not contains_bad_substrings(string)
            and contains_double_letter(string)
            and contains_three_vowels(string)
        ):
            total += 1

    return total


def contains_recurring_pair_no_overlap(input_string: str) -> bool:
    """Checks if string contains a recurring pair with no overlaps."""

    for i in range(len(input_string) - 1):
        pair = input_string[i] + input_string[i+1]

        if input_string.count(pair) >= 2:
            return True

    return False


def contains_sandwiched_letter(input_string: str) -> bool:
    """
    Checks if string contains at least one letter which 
    repeats with exactly one letter between them.
    """

    for i in range(len(input_string)):
        if (0 < i < len(input_string) - 1) and input_string[i-1] == input_string[i+1]:
            return True

    return False


def solve_part2():
    """Solves Part 2."""

    with open('day_5_input.txt', 'r', encoding='utf-8') as f:
        data = [str.strip() for str in f.readlines()]

    total = 0
    for string in data:
        if (
            contains_recurring_pair_no_overlap(string) and
            contains_sandwiched_letter(string)
        ):
            total += 1

    return total


if __name__ == "__main__":
    print(f"Part 1: {solve_part1()} nice strings")
    print(f"Part 2: {solve_part2()} nice strings")
