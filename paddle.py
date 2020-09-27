from enum import Enum
from constant import FIELD_LEFT, FIELD_RIGHT, FIELD_TOP, FIELD_BOTTOM, GAME_HEIGHT
from vector import Vector2i
import pyxel


class PaddleSide(Enum):
    LEFT = 0
    RIGHT = 1


class Paddle:
    def __init__(self, side: PaddleSide) -> None:
        if side == PaddleSide.LEFT:
            self.pos = Vector2i(FIELD_LEFT + 1, GAME_HEIGHT // 2)
        else:
            self.pos = Vector2i(FIELD_RIGHT - 2, GAME_HEIGHT // 2)
        self.height = 8

    def move_up(self) -> None:
        self.pos.y = max(FIELD_TOP + self.height // 2, self.pos.y - 1)

    def move_down(self) -> None:
        self.pos.y = min(FIELD_BOTTOM - self.height // 2, self.pos.y + 1)

    def draw(self) -> None:
        pyxel.rect(self.pos.x, self.pos.y - self.height // 2, 1, self.height, 7)
