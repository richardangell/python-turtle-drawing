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
    ps = canvas.postscript(colormode="color", height=height, width=width)
    img = Image.open(BytesIO(ps.encode("utf-8")))
    img.save(file)


def save_turtle_screengrab(file: str) -> None:
    """Save turtle screen to file."""
    ImageGrab.grab().convert("RGB").save(file)
