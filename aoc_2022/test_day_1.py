"""Tests for Day 1."""

from unittest.mock import mock_open, patch

from day_1 import (
    get_input_as_list,
    convert_input_to_list_of_lists,
    sum_calories_of_each_elf,
    get_index_of_max_calories
)


def test_get_input_as_list():
    """Tests get_input_as_list."""

    file_content = '1\n2\n\n3\n14'

    with patch('builtins.open', new_callable=mock_open, read_data=file_content):
        result = get_input_as_list('input.txt')

    assert result == [1, 2, '-', 3, 14]


def test_convert_input_to_list_of_lists():
    """Tests convert_input_to_list_of_lists."""

    assert convert_input_to_list_of_lists(
        [1, 210, '-', 3, 14, 45, '-', 54, 3, 1]) == [[1, 210], [3, 14, 45], [54, 3, 1]]


def tests_sum_calories_of_each_elf():
    """Tests sum_calories_of_each_elf."""

    assert sum_calories_of_each_elf([[1, 210], [3, 14, 45]]) == [211, 62]


def test_get_index_of_max_calories():
    """Tests get_index_of_max_calories."""

    assert get_index_of_max_calories([211, 62]) == 0
