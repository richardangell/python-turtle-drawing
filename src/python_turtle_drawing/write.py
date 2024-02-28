from PIL import Image, ImageGrab
from io import BytesIO
from turtle import ScrolledCanvas
from typing import Optional


def save_turtle_screen(
    canvas: ScrolledCanvas,
    file: str,
    height: Optional[int] = None,
    width: Optional[int] = None,
) -> None:
    """Save turtle screen to file."""
    img = get_canvas_image(canvas, height, width)
    img.save(file)


def get_canvas_image(
    canvas: ScrolledCanvas, height: Optional[int] = None, width: Optional[int] = None
) -> Image.Image:
    """Get image on canvas.

    Requires ghostscript to be installed.

    """
    ps = canvas.postscript(colormode="color", height=height, width=width)
    return Image.open(BytesIO(ps.encode("utf-8")))


def save_turtle_screengrab(file: str) -> None:
    """Save turtle screen to file."""
    ImageGrab.grab().convert("RGB").save(file)
