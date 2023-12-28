"""Test for Day 1."""

from day_1 import (
    change_frequency
)


def test_change_frequency_positive():
    """Tests change_frequency when positive."""

    assert change_frequency(0, '+3') == 3


def test_change_frequency_negative():
    """Tests change_frequency when negative."""

    assert change_frequency(0, '-34') == -34
