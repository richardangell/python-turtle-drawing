import numpy as np
from numpy.typing import NDArray
from PIL.Image import Image


def get_adjacent_values(
    arr: NDArray,
    index_y: int,
    index_x: int,
) -> list:
    """Get adjacent values to given cell in 2d array."""

    size_y, size_x = arr.shape

    adjacent_cell_values = []
    for y in range(index_y - 1, index_y + 2):
        for x in range(index_x - 1, index_x + 2):
            if (
                y < 0
                or y >= size_y
                or x < 0
                or x >= size_x
                or (y == index_y and x == index_x)
            ):
                continue
            adjacent_cell_values.append(arr[y, x])
    return adjacent_cell_values


def assert_image_difference_within_tolerance(
    difference: Image, tolerance_non_matching_pixels: int
):
    """Assert that number of different pixels is less than a certain amount.

    Also tests that none of the differing pixels are adjacent.

    """

    # sum over 3 channels for each pixel
    difference_arr = np.asarray(difference).sum(axis=2)

    non_matching_pixels = difference_arr > 0

    count_non_matching_pixels = (non_matching_pixels).sum()

    assert count_non_matching_pixels < tolerance_non_matching_pixels, (
        "Number of non-matching pixels outside tolerance."
    )

    for i, (y, x) in enumerate(zip(*np.where(non_matching_pixels), strict=False)):
        values_adjacent_to_non_matching_pixel = get_adjacent_values(
            arr=difference_arr, index_y=y, index_x=x
        )

        assert sum(values_adjacent_to_non_matching_pixel) == 0, (
            f"Non-matching pixel {i} is adjacent to another non-matching pixel."
        )
