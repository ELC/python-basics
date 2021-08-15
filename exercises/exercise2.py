"""Chained Comparisons, arbitary number of parameters, recursivity."""


def maximum_chained(a: float, b: float, c: float) -> float:
    """Takes 3 numbers and return the maximum

    Restriction: Use 2 IFs (no more no less) and chained comparisons
    Reference: https://docs.python.org/3/reference/expressions.html#comparisons
    """


# DO NOT MODIFY - START
assert maximum_chained(1, 10, 5) == 10
assert maximum_chained(5, 10, 1) == 10
assert maximum_chained(5, 10, 5) == 10

assert maximum_chained(4, 9, 18) == 18
assert maximum_chained(9, 4, 18) == 18
assert maximum_chained(9, 9, 18) == 18

assert maximum_chained(24, 9, 18) == 24
assert maximum_chained(24, 18, 9) == 24
assert maximum_chained(24, 18, 18) == 24
# DO NOT MODIFY - END


###############################################################################


def maximum_quartet(a: float, b: float, c: float, d: float) -> float:
    """Refactor to take 4 parameters, use the built-in max function.

    Reference: https://docs.python.org/3/library/functions.html#max
    """


# DO NOT MODIFY - START
assert maximum_quartet(1, 10, 5, -5) == 10
assert maximum_quartet(4, 9, 18, 6) == 18
assert maximum_quartet(24, 9, 18, 20) == 24
assert maximum_quartet(24, 9, 18, 30) == 30
# DO NOT MODIFY - END


###############################################################################


def maximo_arbitrary(*args) -> float:
    """Refactor to take any number of parameters. Use the built-in max
    function.
    Reference: https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists  # noqa: E501
    """


# DO NOT MODIFY - START
assert maximo_arbitrary(1, 10, -5) == 10
assert maximo_arbitrary(4, 2) == 4
assert maximo_arbitrary(24, 9, 18, 20, 60) == 60
assert maximo_arbitrary(24, 9, 18, 30) == 30
# DO NOT MODIFY - END


###############################################################################


def maximum_recursive(*args) -> float:
    """Refactor Recursively for any number of parameters.

    Restriction: No other function (including built-in max) is allowed.
    """


# DO NOT MODIFY - START
assert maximum_recursive(1, 10, -5) == 10
assert maximum_recursive(4, 2) == 4
assert maximum_recursive(24, 9, 18, 20, 60) == 60
assert maximum_recursive(24, 9, 18, 30) == 30
# DO NOT MODIFY - END
