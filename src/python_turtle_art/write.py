from io import BytesIO
from turtle import TurtleScreen

from PIL import Image, ImageGrab

from .helpers.turtle import update_screen


def save_turtle_screen(
    screen: TurtleScreen,
    file: str,
    height: int,
    width: int,
) -> None:
    """Save turtle screen to file.

    Args:
        canvas (Canvas): The canvas to save.
        file (str): The file to save the canvas to.
        height (int): The height of the canvas.
        width (int): The width of the canvas.

    """

    img = get_canvas_image(screen, height, width)
    img.save(file)


def get_canvas_image(screen: TurtleScreen, height: int, width: int) -> Image.Image:
    """Get image on canvas.

    Requires ghostscript to be installed.

    A single pixel is removed from the width and height in the postscript call to
    prevent an extra white border being added along two edges of the image.

    Args:
        canvas (Canvas): The canvas to get the image from.
        height (int): The height of the image.
        width (int): The width of the image.

    """
    update_screen(screen)
    canvas = screen.getcanvas()

    ps = canvas.postscript(
        colormode="color", pagewidth=width - 1, pageheight=height - 1
    )
    return Image.open(BytesIO(ps.encode("utf-8")))


def save_turtle_screengrab(file: str) -> None:
    """Save turtle screen to file."""
    ImageGrab.grab().convert("RGB").save(file)
