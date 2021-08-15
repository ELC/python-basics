"""IF block, logical operators, max function and ternary operator."""


def maximum_basic(a: float, b: float) -> float:
    """Return the maximum between a and b.

    >>> maximum_basic(10, 5)
    10
    >>> maximum_basic(9, 18)
    18

    Restriction: Do not use the built-in max function
    """


###############################################################################


def maximum_built_in(a: float, b: float) -> float:
    """Refactor using the built-in max.

    >>> maximum_basic(10, 5)
    10
    >>> maximum_basic(9, 18)
    18

    Reference: https://docs.python.org/3/library/functions.html#max
    """


###############################################################################


def maximum_ternary(a: float, b: float) -> float:
    """Refactor using the ternary operator.

    >>> maximum_ternary(10, 5)
    10
    >>> maximum_ternary(9, 18)
    18

    Reference: https://docs.python.org/3/reference/expressions.html#conditional-expressions # noqa: E501
    """


if __name__ == "__main__":
    import doctest

    assert doctest.testmod().failed == 0
