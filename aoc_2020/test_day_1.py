"""Tests for Day 1."""

from day_1 import (
    find_two_entries
)


def test_find_two_entries():
    """Tests find_two_entries."""

    assert find_two_entries([1721, 979, 366, 299, 675, 1456]) == (1721, 299)
