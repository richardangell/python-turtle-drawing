import pytest

from python_turtle_art.filling.stripes import (
    get_incremenets_from_origin_within_range,
)


@pytest.mark.parametrize(
    "increment",
    [
        0,
        -1,
    ],
)
def test_increment_less_than_zero_error(increment):
    with pytest.raises(ValueError, match="Increment must be greater than zero."):
        get_incremenets_from_origin_within_range(
            origin=0,
            increment=increment,
            min_=0,
            max_=10,
        )


def test_no_increments_in_range_warning():
    with pytest.warns(
        UserWarning, match="No increments of 20 in range 10 to 20, starting from 0."
    ):
        actual = get_incremenets_from_origin_within_range(
            origin=0,
            increment=20,
            min_=10,
            max_=20,
        )

    assert actual == []


@pytest.mark.parametrize(
    ["origin", "increment", "min_", "max_", "expected"],
    [
        (0, 5, 0, 10, [5]),
        (0, 5, 0, 20, [5, 10, 15]),
        (0, 1, 0, 10, [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        (0, 2, 0, 10, [2, 4, 6, 8]),
        (-1, 5, 0, 10, [4, 9]),
        (-2, 5, 0, 10, [3, 8]),
        (-22, 5, 0, 10, [3, 8]),
        (-23, 5, 0, 10, [2, 7]),
        (-44, 5, 0, 10, [1, 6]),
        (-555, 5, 0, 10, [5]),
        (1, 5, 0, 10, [1, 6]),
        (12, 5, 0, 10, [2, 7]),
        (93, 5, 0, 10, [3, 8]),
        (34, 5, 0, 10, [4, 9]),
        (15, 5, 0, 10, [5]),
        (0, 1, 0, 5, [1, 2, 3, 4]),
        (11, 1, 0, 5, [1, 2, 3, 4]),
        (42, 1, 0, 5, [1, 2, 3, 4]),
        (63, 1, 0, 5, [1, 2, 3, 4]),
        (84, 1, 0, 5, [1, 2, 3, 4]),
        (175, 1, 0, 5, [1, 2, 3, 4]),
        (0, 3, -12, 12, [-9, -6, -3, 0, 3, 6, 9]),
        (1, 3, -12, 12, [-11, -8, -5, -2, 1, 4, 7, 10]),
        (-2, 3, -12, 12, [-11, -8, -5, -2, 1, 4, 7, 10]),
        (6, 3, -12, 12, [-9, -6, -3, 0, 3, 6, 9]),
    ],
)
def test_expected_output(origin, increment, min_, max_, expected):
    actual = get_incremenets_from_origin_within_range(
        origin=origin,
        increment=increment,
        min_=min_,
        max_=max_,
    )

    assert actual == expected
