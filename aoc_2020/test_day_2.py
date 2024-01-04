"""Tests for Day 2."""


from unittest.mock import mock_open, patch
import pytest

from day_2 import (
    read_input,
    get_lowest_number,
    get_highest_number,
    get_policy_letter,
    get_password,
    is_valid,
    is_valid_pt2
)


def test_read_input():
    """Mocks file to test read_input."""

    file_content = '3-4 k: kqxm\n1-2 s: ssnsl'

    with patch('builtins.open', new_callable=mock_open, read_data=file_content):
        result = read_input('file.txt')

    assert result == ['3-4 k: kqxm', '1-2 s: ssnsl']


def test_get_lowest_number():
    """Tests get_lowest_number."""

    assert get_lowest_number('9-19 h: lhmwjzxchvjsxtmbmqh') == 9


def test_get_highest_number():
    """Tests get_highest_number."""

    assert get_highest_number('9-19 h: lhmwjzxchvjsxtmbmqh') == 19


def test_get_policy_letter():
    """Tests get_policy_letter."""

    assert get_policy_letter('9-19 h: lhmwjzxchvjsxtmbmqh') == 'h'


def test_get_password():
    """Tests get_password."""

    assert get_password('9-19 h: lhmwjzxchvjsxtmbmqh') == 'lhmwjzxchvjsxtmbmqh'


@pytest.mark.parametrize(('test_input, expected'),
                         [('1-3 a: abcde', True),
                          ('1-3 b: cdefg', False),
                          ('2-9 c: ccccccccc', True)])
def test_is_valid(test_input, expected):
    """Tests is_valid."""

    assert is_valid(test_input) == expected


@pytest.mark.parametrize(('test_input, expected'),
                         [('1-3 a: abcde', True),
                          ('1-3 b: cdefg', False),
                          ('2-9 c: ccccccccc', False)])
def test_is_valid_pt2(test_input, expected):
    """Tests is_valid_pt2."""

    assert is_valid_pt2(test_input) == expected
