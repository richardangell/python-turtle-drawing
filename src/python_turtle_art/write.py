from io import BytesIO
from tkinter import Canvas
from typing import Optional

from PIL import Image, ImageGrab


def save_turtle_screen(
    canvas: Canvas,
    file: str,
    height: Optional[int] = None,
    width: Optional[int] = None,
) -> None:
    """Save turtle screen to file."""
    img = get_canvas_image(canvas, height, width)
    img.save(file)


def get_canvas_image(
    canvas: Canvas, height: Optional[int] = None, width: Optional[int] = None
) -> Image.Image:
    """Get image on canvas.

    Requires ghostscript to be installed.

    """
    ps = canvas.postscript(colormode="color")  # , height=height, width=width)
    return Image.open(BytesIO(ps.encode("utf-8")))


def save_turtle_screengrab(file: str) -> None:
    """Save turtle screen to file."""
    ImageGrab.grab().convert("RGB").save(file)
