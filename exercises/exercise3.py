"""Boolean Expresions, multiple returns, single returns."""


def is_vowerl_multiple_if(letter: str) -> bool:
    """Takes a string of length 1 and returns a boolean depending on the string
    being a vowel

    Restriction: Use 5 IFs, one for each posibility. Use multiple returns
    Reference: https://docs.python.org/3/library/stdtypes.html#string-methods
    """


# DO NOT MODIFY - START
assert is_vowerl_multiple_if("a")
assert not is_vowerl_multiple_if("b")
assert not is_vowerl_multiple_if("B")
assert is_vowerl_multiple_if("A")
# DO NOT MODIFY - END


###############################################################################


def is_vowel_single_if(letter: str) -> bool:
    """Refactor to use a single IF and the IN operator.
    Reference: https://docs.python.org/3/reference/expressions.html#membership-test-operations  # noqa: E501
    """


# DO NOT MODIFY - START
assert is_vowel_single_if("a")
assert not is_vowel_single_if("b")
assert not is_vowel_single_if("B")
assert is_vowel_single_if("A")
# DO NOT MODIFY - END


###############################################################################


def is_vowel_no_if(letter: str) -> bool:
    """Refactor to avoid using IFs and use a single return."""


# DO NOT MODIFY - START
assert is_vowel_no_if("a")
assert not is_vowel_no_if("b")
assert not is_vowel_no_if("B")
assert is_vowel_no_if("A")
# DO NOT MODIFY - END
