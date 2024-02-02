"""Tests for Day 3: Binary Diagnostic."""

from day_3 import (
    SMALL_INPUT_FILE,
    get_input,
    get_digits_at_each_bit,
    get_digit_counts,
    solve_part1
)


def test_get_input_first_line():
    assert get_input(SMALL_INPUT_FILE)[0] == '00100'


def test_get_input_length():
    assert len(get_input(SMALL_INPUT_FILE)) == 12


def test_get_digits_at_each_bit():
    assert get_digits_at_each_bit(['433', '424', '473']) == [
        '444', '327', '343']


def test_get_digit_counts():
    assert get_digit_counts('01101') == [2, 3]


def test_solve_part1():
    assert solve_part1(SMALL_INPUT_FILE) == 198
