"""Tests for AOC Day 2."""

from day_2 import (
    split_string,
    convert_to_integers,
    calculate_wrapping_paper,
    get_smallest_area,
    calculate_total_wrapping_paper,
    get_smallest_side_perimeter,
    calculate_cubic_volume
)

def test_split_string():
    assert split_string('20x1x27') == ['20', '1', '27']


def test_convert_to_integers():
    assert convert_to_integers(['20', '1', '27']) == [20, 1, 27]


def test_calculate_wrapping_paper():
    assert calculate_wrapping_paper([2, 2, 2]) == 24


def test_get_smallest_area():
    assert get_smallest_area([2, 3, 4]) == 6


def test_calculate_total_wrapping_paper():
    assert calculate_total_wrapping_paper('1x1x10') == 43


def test_get_smallest_side_perimeter():
    assert get_smallest_side_perimeter([2, 3, 4]) == 10

def test_calculate_cubic_volume():
    assert calculate_cubic_volume([2, 3, 4]) == 24