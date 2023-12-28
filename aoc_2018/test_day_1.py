"""Test for Day 1."""

import pytest


from day_1 import (
    change_frequency
)


@pytest.mark.parametrize(('test_input1, test_input2, expected'),
                         [(0, '+3', 3),
                          (0, '-34', -34),
                          (6, '+26', 32)])
def test_change_frequency(test_input1, test_input2, expected):
    """Tests change_frequency."""

    assert change_frequency(test_input1, test_input2) == expected
