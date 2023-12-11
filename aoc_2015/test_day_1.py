"""Test file for AOC Day 1."""

import pytest

from day_1 import count_floor_movement

def test_count_floor_movement():
    assert count_floor_movement('(())') == 0
