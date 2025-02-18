import pytest

from python_turtle_art.filling.horizontal_stripe_fill import (
    StepsBetweenIndices,
    get_number_of_steps_between_indices,
)

PARAMS = [
    (0, 1, 5, 1, 4),
    (0, 2, 5, 2, 3),
    (0, 3, 5, 3, 2),
    (0, 4, 5, 4, 1),
    (1, 2, 5, 1, 4),
    (1, 3, 5, 2, 3),
    (1, 4, 5, 3, 2),
    (2, 3, 5, 1, 4),
    (2, 4, 5, 2, 3),
    (3, 4, 5, 1, 4),
]


@pytest.mark.parametrize(
    ["index_a", "index_b", "n", "expected_a_to_b", "expected_b_to_a"], PARAMS
)
def test_expected_output_a_lt_b(index_a, index_b, n, expected_a_to_b, expected_b_to_a):
    sequence = [0] * n

    expected = StepsBetweenIndices(a_to_b=expected_a_to_b, b_to_a=expected_b_to_a)

    actual = get_number_of_steps_between_indices(
        index_a=index_a, index_b=index_b, sequence=sequence
    )

    assert actual == expected


@pytest.mark.parametrize(
    ["index_b", "index_a", "n", "expected_b_to_a", "expected_a_to_b"], PARAMS
)
def test_expected_output_b_lt_a(index_a, index_b, n, expected_a_to_b, expected_b_to_a):
    """Note, parameters are reversed in this test."""

    sequence = [0] * n

    expected = StepsBetweenIndices(a_to_b=expected_a_to_b, b_to_a=expected_b_to_a)

    actual = get_number_of_steps_between_indices(
        index_a=index_a, index_b=index_b, sequence=sequence
    )

    assert actual == expected


@pytest.mark.parametrize(
    ["index_a", "index_b", "n", "expected_a_to_b", "expected_b_to_a"], PARAMS
)
def test_expected_output_a_eq_b(index_a, index_b, n, expected_a_to_b, expected_b_to_a):
    """Test first number is n and second number is 0 when a and b are equal."""

    sequence = [0] * n

    expected = StepsBetweenIndices(a_to_b=expected_a_to_b + expected_b_to_a, b_to_a=0)

    assert expected_a_to_b + expected_b_to_a == n

    actual = get_number_of_steps_between_indices(
        index_a=index_a, index_b=index_a, sequence=sequence
    )

    assert actual == expected
