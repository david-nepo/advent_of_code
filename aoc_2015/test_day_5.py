"""Tests for Day 5."""

from day_5 import (
    contains_bad_substrings,
    contains_three_vowels,
    contains_double_letter,
    contains_recurring_pair_no_overlap,
    contains_sandwiched_letter
)


def test_contains_bad_substrings_true():
    """Tests contains_bad_substrings when True."""

    assert contains_bad_substrings('ffasdpqsdf') == True


def test_contains_bad_substrings_false():
    """Tests contains_bad_substrings when False"""

    assert contains_bad_substrings('hellothereqp') == False


def test_contains_three_vowels_true():
    """Tests contains_three_vowels when True."""

    assert contains_three_vowels('three is great') == True


def test_contains_three_vowels_false():
    """Tests contains_three_vowels when False."""

    assert contains_three_vowels('rhythm') == False


def test_contains_double_letter_true():
    """Tests contains_double_letter when True."""

    assert contains_double_letter('bgfaaahethv') == True


def test_contains_double_letter_false():
    """Tests contains_double_letter when False."""

    assert contains_double_letter('xafrhfaefthv') == False


def test_contains_recurring_pair_no_overlap_true():
    """Tests contains_recurring_pair_no_overlap when True."""

    assert contains_recurring_pair_no_overlap('xyhajkdfhxykl') == True


def test_contains_recurring_pair_no_overlap_false():
    """Tests contains_recurring_pair_no_overlap when False."""

    assert contains_recurring_pair_no_overlap('klpjxxxfsg') == False


def test_contains_sandwiched_letter_true():
    """Tests contains_sandwiched_letter when True."""

    assert contains_sandwiched_letter('ieodomkazucvgmuy') == True


def test_contains_sandwiched_letter_false():
    """Tests contains_sandwiched_letter when False."""

    assert contains_sandwiched_letter('uurcxstgmygtbstg') == False
