from turtle import Vec2D

from .polygon import is_convex


class ConvexPolygon:
    """Mixin for a convex polygon.

    Defines a setter for the vertices property which enforces the convex property.

    """

    @property
    def vertices(self) -> tuple[Vec2D, ...]:
        return self._vertices

    @vertices.setter
    def vertices(self, vertices: tuple[Vec2D, ...]) -> None:
        """Perform checks on vertices and set attributes.

        Check at least 3 vertices are passed and the vertices form a convex polygon are
        provided.

        """
        if len(vertices) < 3:
            raise ValueError("vertices must contain at least 3 points.")
        if not is_convex(vertices):
            raise ValueError("Supplied vertices are not convex.")
        self._vertices = vertices
