"""Tests for Day 2."""

from unittest.mock import mock_open, patch


from day_2 import (
    get_input_data
)


def test_get_input_data():
    """Tests get_input_data with mock_open."""

    file_content = '1,9,10,3'

    with patch('builtins.open', new_callable=mock_open, read_data=file_content):
        result = get_input_data('input.txt')

        assert result == [1, 9, 10, 3]
