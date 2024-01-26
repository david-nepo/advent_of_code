"""Tests for Day 4."""

from day_4 import (
    check_for_mandatory_fields
)


def test_check_for_mandatory_fields_true():

    passport = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'cid', 'hgt']

    assert check_for_mandatory_fields(passport)


def test_check_for_mandatory_fields_false():

    passport = ['iyr', 'ecl', 'cid', 'eyr', 'pid', 'hcl', 'byr']

    assert check_for_mandatory_fields(passport) == False
