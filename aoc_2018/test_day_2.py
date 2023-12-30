"""Tests for Day 2."""

import pytest

from day_2 import (
    get_two_letter_count,
    get_three_letter_count,
    get_checksum
)


@pytest.mark.parametrize('test_input, expected',
                         [('abcdef', 0),
                          ('bababc', 1),
                          ('aabbcdgsdgddd', 1)])
def test_get_two_letter_count(test_input, expected):
    """Tests get_two_letter_count."""

    assert get_two_letter_count(test_input) == expected


@pytest.mark.parametrize('test_input, expected',
                         [('abcdef', 0),
                          ('bababc', 1),
                          ('aabbcdgsdagddgd', 1)])
def test_get_three_letter_count(test_input, expected):
    """Tests get_three_letter_count."""

    assert get_three_letter_count(test_input) == expected


def test_get_checksum():
    """Tests get_checksum."""

    assert get_checksum(3, 4) == 12
