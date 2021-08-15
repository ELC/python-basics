"""FOR loops, range, len, enumerate and zip."""


def sum_numbers_for_range(start: int, end: int) -> int:
    """Given an start position and an end position, return the sum of all
    integers in between (extemes included)

    Restriction: Use a For loop and the built-in range
    Reference: https://docs.python.org/3/library/functions.html#func-range
    """


# DO NOT MODIFY - START
assert sum_numbers_for_range(1, 100) == 5050
assert sum_numbers_for_range(-100, 1) == -5050
assert sum_numbers_for_range(-100, 100) == 0
# DO NOT MODIFY - END


###############################################################################


def sum_numbers_sum_range(start: int, end: int) -> int:
    """Refactor to use the built-in sum and range.

    Restriction: Do NOT use any loops.
    Reference: https://docs.python.org/3/library/functions.html#func-range
    """


# DO NOT MODIFY - START
assert sum_numbers_sum_range(1, 100) == 5050
assert sum_numbers_sum_range(-100, 1) == -5050
assert sum_numbers_sum_range(-100, 100) == 0
# DO NOT MODIFY - END


###############################################################################

from typing import Iterable  # noqa: E402


def cumulative_sum_with_range(numbers: Iterable[float]) -> float:
    """Given an iterable of numbers, return the cumulative sum of all.
    If the list is empty, it should return 0.

    Restrictions:
        - Use one FOR loop.
        - Use the built-in range
        - Use the built-in len
        - Do NOT use the built-in sum.
        - Do NOT use the built-in len.
    """


# DO NOT MODIFY - START
assert cumulative_sum_with_range([1, 2, 3, 4]) == 10
assert cumulative_sum_with_range([2, 5]) == 7
assert cumulative_sum_with_range([-1, 1]) == 0
assert cumulative_sum_with_range([]) == 0
assert cumulative_sum_with_range([1, 2, 3, 0, 4, 5]) == 15
# DO NOT MODIFY - END


###############################################################################


def cumulative_sum_without_range(numbers: Iterable[float]) -> float:
    """Refactor to avoid using the built-in range nor len nor indexing.

    Restrictions:
        - Use one FOR loop.
        - Do NOT use the built-in range.
        - Do NOT use the built-in sum.
        - Do NOT use the built-in len.
        - Do NOT use indexing.
    """


# DO NOT MODIFY - START
assert cumulative_sum_without_range([1, 2, 3, 4]) == 10
assert cumulative_sum_without_range([2, 5]) == 7
assert cumulative_sum_without_range([-1, 1]) == 0
assert cumulative_sum_without_range([]) == 0
assert cumulative_sum_without_range([1, 2, 3, 0, 4, 5]) == 15
assert cumulative_sum_without_range(range(1, 20)) == 190
assert cumulative_sum_without_range(iter(range(20))) == 190
# DO NOT MODIFY - END


###############################################################################


def find_minimum_with_range(numbers: Iterable[float]) -> float:
    """Given an iterable of numbers, return the minimum and its index.

    If the iterable is empty, return empty list.

    Restrictions:
        - Use one FOR loop.
        - Use the built in range.
        - Use the built in len.
        - Do NOT use index method.
        - Do NOT use the built-in min.
    """


# DO NOT MODIFY - START
assert find_minimum_with_range([1, 2, 3, 4]) == (1, 0)
assert find_minimum_with_range([2, 5]) == (1, 0)
assert find_minimum_with_range([-1, 1]) == (1, 0)
assert find_minimum_with_range([]) == []
assert find_minimum_with_range([1, 2, 3, 0, 4, 5]) == (0, 3)
assert find_minimum_with_range(range(20, 1, -1)) == (2, 18)
# DO NOT MODIFY - END


###############################################################################


def find_minimum_with_enumerate(numbers: Iterable[float]) -> float:
    """Refactor to avoid using the built in range or len.

    If the iterable is empty, return empty list.

    Restrictions:
        - Use one FOR loop.
        - Use the built in enumerate.
        - Do NOT use index method.
        - Do NOT use the built-in min.
        - Do NOT use the built-in range.
        - Do NOT use indexing.
    """


# DO NOT MODIFY - START
assert find_minimum_with_enumerate([1, 2, 3, 4]) == (1, 0)
assert find_minimum_with_enumerate([2, 5]) == (1, 0)
assert find_minimum_with_enumerate([-1, 1]) == (1, 0)
assert find_minimum_with_enumerate([]) == []
assert find_minimum_with_enumerate([1, 2, 3, 0, 4, 5]) == (0, 3)
assert find_minimum_with_enumerate(range(20, 1, -1)) == (2, 18)
assert find_minimum_with_enumerate(iter(range(20, 1, -1))) == (2, 18)
# DO NOT MODIFY - END


###############################################################################


from typing import Tuple, List  # noqa: E402


def combine_range(
    names: Iterable[str], prices: Iterable[float], ids: Iterable[int]
) -> List[Tuple[str, float, int]]:
    """Given three iterables of names, prices and ides, returns a list of triplets.

    The returned list should be as long as the shortest iterable

    Restrictions:
        - Use one FOR loop.
        - Use the built in range.
        - Use the built in len.
    """


# DO NOT MODIFY - START
names = ["window", "lamp", "shampoo"]
prices = [100.48, 16.42, 5.20]
ids = [6852, 1459, 3578]

triplets = combine_range(names, prices, ids)

triplets_expected = [
    ("window", 100.48, 6852),
    ("lamp", 16.42, 1459),
    ("shampoo", 5.20, 3578),
]

assert triplets == triplets_expected
# DO NOT MODIFY - END


###############################################################################


from typing import Tuple, List  # noqa: E402


def combine_zip(
    names: Iterable[str], prices: Iterable[float], ids: Iterable[int]
) -> List[Tuple[str, float, int]]:
    """Refactor to avoid using range and len.

    The returned list should be as long as the shortest iterable

    Restrictions:
        - Use one FOR loop.
        - Use the built in zip.
        - Do NOT use the built-in len.
        - Do NOT use the built-in range.
    """


# DO NOT MODIFY - START
names = ["window", "lamp", "shampoo"]
prices = [100.48, 16.42, 5.20]
ids = [6852, 1459, 3578]

triplets = combine_zip(names, prices, ids)

triplets_expected = [
    ("window", 100.48, 6852),
    ("lamp", 16.42, 1459),
    ("shampoo", 5.20, 3578),
]

assert triplets == triplets_expected
# DO NOT MODIFY - END


###############################################################################


from typing import Tuple, List  # noqa: E402


def combine_zip_list(
    names: Iterable[str], prices: Iterable[float], ids: Iterable[int]
) -> List[Tuple[str, float, int]]:
    """Refactor to avoid using loops.

    The returned list should be as long as the shortest iterable

    Restrictions:
        - Use the built in zip.
        - Do NOT use FOR loops.
        - Do NOT use the built-in len.
        - Do NOT use the built-in range.
    """


# DO NOT MODIFY - START
names = ["window", "lamp", "shampoo"]
prices = [100.48, 16.42, 5.20]
ids = [6852, 1459, 3578]

triplets = combine_zip_list(names, prices, ids)

triplets_expected = [
    ("window", 100.48, 6852),
    ("lamp", 16.42, 1459),
    ("shampoo", 5.20, 3578),
]

assert triplets == triplets_expected
# DO NOT MODIFY - END


###############################################################################


from typing import Tuple, List  # noqa: E402


def combine_zip_enumerate(
    names: Iterable[str], prices: Iterable[float]
) -> List[Tuple[str, float, int]]:
    """Refactor to use index as ids. Loops allow.

    The returned list should be as long as the shortest iterable

    Restrictions:
        - Use one FOR loops.
        - Use the built in zip.
        - Use the built in enumerate.
        - Do NOT use the built-in len.
        - Do NOT use the built-in range.
        - Do NOT use indexing.
    """


# DO NOT MODIFY - START
names = ["window", "lamp", "shampoo"]
prices = [100.48, 16.42, 5.20]

triplets = combine_zip_enumerate(names, prices)

triplets_expected = [
    ("window", 100.48, 1),
    ("lamp", 16.42, 2),
    ("shampoo", 5.20, 3),
]

assert triplets == triplets_expected
# DO NOT MODIFY - END
