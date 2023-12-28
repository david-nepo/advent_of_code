"""Tests for Day 2."""

from day_2 import (
    convert_str_to_int,
    get_difference,
    get_checksum
)


def test_convert_str_to_int():
    """Tests conversion of string to list of ints."""

    assert convert_str_to_int('5 1 9 5') == [5, 1, 9, 5]


def test_get_difference():
    """Tests get_difference."""

    assert get_difference([5, 1, 9, 5]) == 8


def test_get_checksum():
    """Tests get_checksum."""

    assert get_checksum([8, 4, 6]) == 18
