from vector import Vector2i
from constant import (
    FIELD_TOP,
    FIELD_BOTTOM,
    FIELD_LEFT,
    FIELD_RIGHT,
)
import pyxel


class Ball:
    def __init__(self, x: int, y: int) -> None:
        self.pos = Vector2i(x, y)
        self.velocity = Vector2i(0, 0)

    def stop(self) -> None:
        self.velocity = Vector2i(0, 0)

    def reflect_horizontally(self) -> None:
        self.velocity.x = -self.velocity.x

    def reflect_vertically(self) -> None:
        self.velocity.y = -self.velocity.y
        if self.pos.y <= FIELD_TOP:
            self.pos.y = FIELD_TOP
        else:
            self.pos.y = FIELD_BOTTOM

    def move(self) -> None:
        self.pos = self.pos + self.velocity
        if self.pos.y <= FIELD_TOP or self.pos.y >= FIELD_BOTTOM:
            self.reflect_vertically()

    def update(self) -> None:
        self.move()

    def draw(self) -> None:
        pyxel.pset(self.pos.x, self.pos.y, 7)

    def is_reach_left(self) -> bool:
        return self.pos.x < FIELD_LEFT

    def is_reach_right(self) -> bool:
        return self.pos.x >= FIELD_RIGHT

    def is_reach_edge(self) -> None:
        return self.is_reach_left() or self.is_reach_right()
