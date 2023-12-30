"""Tests for Day 1."""

import pytest

from day_1 import (
    get_required_fuel,
    get_required_fuel_recursive
)


@pytest.mark.parametrize('test_input, expected',
                         [(12, 2),
                          (14, 2),
                          (1969, 654),
                          (100756, 33583)])
def test_get_required_fuel(test_input, expected):
    """Tests get_required_fuel."""

    assert get_required_fuel(test_input) == expected


@pytest.mark.parametrize('test_input, expected',
                         [(14, 2),
                          (1969, 966),
                          (100756, 50346)])
def test_get_required_fuel_recursive(test_input, expected):
    """Tests get_required_fuel_recursive for part 2."""

    assert get_required_fuel_recursive(test_input) == expected
