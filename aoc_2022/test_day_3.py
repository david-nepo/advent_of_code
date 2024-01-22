"""Tests for Day 3."""

from day_3 import (
    split_rucksack,
    get_shared_letter,
    convert_letter_to_priority,
    solve_part1,
    get_shared_letter_pt2,
    solve_part2
)


def test_split_rucksack_basic():
    """Tests split_rucksack with basic letters."""

    assert split_rucksack("abbs") == ["ab", "bs"]


def test_split_rucksack_extended():
    """Tests split_rucksack with AoC examples."""

    assert split_rucksack("vJrwpWtwJgWrhcsFMMfFFhFp") == [
        "vJrwpWtwJgWr", "hcsFMMfFFhFp"]


def test_get_shared_letter_basic():
    """Tests shared_letter with basic letters."""

    assert get_shared_letter("abcdex", "fghijx") == "x"


def test_get_shared_letter_extended():
    """Tests shared_letter with AoC examples."""

    assert get_shared_letter("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL") == "L"


def test_convert_letter_to_priority_lowercase():
    """Tests convert_letter_to_priority with lowercase letter."""

    assert convert_letter_to_priority('z') == 26


def test_convert_letter_to_priority_uppercase():
    """Tests convert_letter_to_priority with uppercase letter."""

    assert convert_letter_to_priority('A') == 27


def test_solve_part1():
    """Tests Part 1 logic."""

    assert solve_part1('test_input_day_3.txt') == 157


def test_get_shared_letter_pt2_basic():
    """Tests get_shared_letter_pt2 with basic letters."""

    assert get_shared_letter_pt2("abcy", "defy", "ghiy") == "y"


def test_get_shared_letter_pt2_extended():
    """Tests get_shared_letter_pt2 with AoC examples."""

    assert get_shared_letter_pt2(
        "vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg") == "r"


def test_solve_part2():
    """Tests Part 2 logic."""

    assert solve_part2('test_input_day_3.txt') == 70
