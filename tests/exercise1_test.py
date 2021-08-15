"""Test Suite for Exercise 1"""
import doctest
from exercises import exercise1


def test_doctest():
    assert doctest.testmod(exercise1).failed == 0


def test_maximum_basic():
    assert exercise1.maximum_basic(10, 5) == 10
    assert exercise1.maximum_basic(9, 18) == 18


def test_maximum_built_in():
    assert exercise1.maximum_built_in(10, 5) == 10
    assert exercise1.maximum_built_in(9, 18) == 18


def test_maximum_ternary():
    assert exercise1.maximum_ternary(10, 5) == 10
    assert exercise1.maximum_ternary(9, 18) == 18
