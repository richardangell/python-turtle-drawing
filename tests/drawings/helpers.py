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
    difference: Image,
    tolerance_non_matching_pixels: int,
    tolerance_adjacent_pixels: int,
):
    """Assert that number of different pixels is less than a certain amount.

    Also tests that none of the differing pixels are adjacent.

    Args:
        difference (Image): Image of difference between expected and actual images.
        tolerance_non_matching_pixels (int): Maximum number of matching pixels that are
            allowed to differ (i.e. be non-zero) in difference.
        tolerance_adjacent_pixels (int): Maximum number of adjacent pixels allowed to
            each non-matching pixels.

    """

    # sum over 3 channels for each pixel
    difference_arr = np.asarray(difference).sum(axis=2)

    non_matching_pixels = difference_arr > 0

    count_non_matching_pixels = (non_matching_pixels).sum()

    assert count_non_matching_pixels <= tolerance_non_matching_pixels, (
        "Number of non-matching pixels outside tolerance."
    )

    for i, (y, x) in enumerate(zip(*np.where(non_matching_pixels), strict=False)):
        values_adjacent_to_non_matching_pixel = get_adjacent_values(
            arr=difference_arr, index_y=y, index_x=x
        )

        count_adjacent_non_matching_pixels = len(
            [x for x in values_adjacent_to_non_matching_pixel if x > 0]
        )

        assert count_adjacent_non_matching_pixels <= tolerance_adjacent_pixels, (
            f"Non-matching pixel {i} is adjacent to "
            f"{count_adjacent_non_matching_pixels} non-matching pixels."
        )
