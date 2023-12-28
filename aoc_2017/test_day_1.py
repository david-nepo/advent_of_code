"""Tests for Day 1."""


import pytest


from day_1 import (
    append_first_digit,
    get_matching_digits,
    sum_matching_digits,
    solve_part1,
    solve_part2
)


def test_append_first_digit():
    """Tests append_first_digit."""

    assert append_first_digit('1122') == '11221'


def test_get_matching_digits():
    """Tests get_matching_digits."""

    assert get_matching_digits('11221') == [1, 2]


def test_get_matching_digits_same_numbers():
    """Tests get_matching_digits when all digits the same."""

    assert get_matching_digits('11111') == [1, 1, 1, 1]


def test_get_matching_digits_end_numbers():
    """Tests get_matching_digits when for third example."""

    assert get_matching_digits('912121299') == [9]


def test_sum_matching_digits():
    """Tests sum_matching_digits."""

    assert sum_matching_digits([1, 1, 1, 1]) == 4


@pytest.mark.parametrize("test_input, expected", [("1122", 3), ("1111", 4), ("1234", 0), ('91212129', 9)])
def test_solve_part1(test_input, expected):
    """Tests solve_part1 for example inputs."""

    assert solve_part1(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [("1212", 6), ("1221", 0), ("123425", 4), ('123123', 12), ('12131415', 4)])
def test_solve_part2(test_input, expected):
    """Tests solve_part2 for example inputs."""

    assert solve_part2(test_input) == expected
