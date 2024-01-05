"""Tests for Day 2."""

from unittest.mock import mock_open, patch
import pytest

from day_2 import (
    read_input,
    get_opponent_shape,
    get_your_shape,
    get_result_points,
    get_shape_points,
    determine_your_shape
)


def test_read_input():
    """Tests read_input by mocking file content."""

    file_content = "A Y\nC X"

    with patch('builtins.open', new_callable=mock_open, read_data=file_content):
        result = read_input('file.txt')

        assert result == ['A Y', 'C X']


def test_get_opponent_shape():
    """Tests get_opponent_shape."""

    assert get_opponent_shape('C X') == 'C'


def test_get_your_shape():
    """Tests get_your_shape."""

    assert get_your_shape('C X') == 'X'


@pytest.mark.parametrize(('test_input, expected'), [
    ('A Y', 6),
    ('B X', 0),
    ('C Z', 3)
])
def test_get_result_points(test_input, expected):
    """Tests get_result_points."""

    assert get_result_points(test_input) == expected


@pytest.mark.parametrize(('test_input, expected'), [
    ('X', 1),
    ('Y', 2),
    ('Z', 3)
])
def test_get_shape_points(test_input, expected):
    """Tests get_shape_points."""

    assert get_shape_points(test_input) == expected


@pytest.mark.parametrize(('test_input, expected'), [
    ('A Y', 'X'),
    ('B X', 'X'),
    ('C Z', 'X')
])
def test_get_your_shape_2(test_input, expected):
    """Tests get_your_shape_2."""

    assert determine_your_shape(test_input) == expected
