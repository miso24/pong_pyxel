from __future__ import annotations
from typing import Iterable


class Vector2i:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self, v: Vector2i) -> Vector2i:
        return Vector2i(self.x + v.x, self.y + v.y)

    def __sub__(self, v: Vector2i) -> Vector2i:
        return Vector2i(self.x - v.x, self.y - v.y)

    def __mul__(self, s: int) -> Vector2i:
        return Vector2i(self.x * s, self.y * s)

    def __div__(self, s: int) -> Vector2i:
        return Vector2i(self.x // s, self.y // s)

    def __iter__(self) -> Iterable[int]:
        return iter([self.x, self.y])


def dot(v1: Vector2i, v2: Vector2i) -> int:
    return v1.x * v2.x + v1.y * v2.y
