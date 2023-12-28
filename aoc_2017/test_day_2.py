"""Tests for Day 2."""

import pytest


from day_2 import (
    convert_str_to_int,
    get_difference,
    get_checksum,
    get_evenly_divisible_values
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


@pytest.mark.parametrize(
    'test_input, expected',
    [([5, 9, 2, 8], 4),
     ([9, 4, 7, 3], 3),
     ([3, 8, 6, 5], 2)])
def test_get_evenly_divisible_values(test_input, expected):
    """Tests get_evenly_divisible_values."""

    assert get_evenly_divisible_values(test_input) == expected
