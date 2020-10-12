from constant import GAME_WIDTH, GAME_HEIGHT, MAX_POINT
from ball import Ball
from vector import Vector2i
from paddle import Paddle, PaddleSide
from enum import Enum
import random
import pyxel


class GameState(Enum):
    SERVE = 0
    GAME = 1
    FINISH = 2


class Game:
    def __init__(self) -> None:
        pyxel.init(GAME_WIDTH, GAME_HEIGHT)
        self.ball = Ball(GAME_WIDTH // 2, GAME_HEIGHT // 2)
        self.points = {
            "LEFT": 0,
            "RIGHT": 0,
        }
        self.paddles = [
            Paddle(PaddleSide.LEFT),
            Paddle(PaddleSide.RIGHT),
        ]
        self.state = GameState.SERVE
        self.choice_serve_side()
        self.init_ball_pos()
        self.init_sound()

    def init_sound(self) -> None:
        pyxel.sound(0).set(
            "C3",
            "T",
            "7",
            "",
            5
        )
        pyxel.sound(1).set(
            "E2E2E2E2",
            "P",
            "7",
            "",
            5
        )

    def choice_serve_side(self) -> None:
        self.serve_side = random.choice(['LEFT', 'RIGHT'])

    def init_ball_pos(self) -> None:
        if self.serve_side == "LEFT":
            self.ball.pos.x = self.paddles[0].pos.x + 2
        else:
            self.ball.pos.x = self.paddles[1].pos.x - 2

    def serve_ball(self) -> None:
        vy = random.choice([1, -1])
        vx = 1 if self.serve_side == "LEFT" else -1
        self.ball.velocity = Vector2i(vx, vy)
        self.state = GameState.GAME

    def serve_state(self) -> None:
        if self.serve_side == "LEFT":
            self.ball.pos.y = self.paddles[0].pos.y
        else:
            self.ball.pos.y = self.paddles[1].pos.y
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.serve_ball()

    def game_state(self) -> None:
        # check collision
        for paddle in self.paddles:
            bx, by = self.ball.pos
            px, py = paddle.pos
            half_height = paddle.height // 2
            if px == bx and py - half_height <= by <= py + half_height:
                self.ball.reflect_horizontally()
                pyxel.play(0, 0)
        # ball
        if not self.ball.is_reach_edge():
            return
        self.ball.stop()
        self.ball.pos = Vector2i(-1, -1)
        pyxel.play(1, 1)
        if self.ball.is_reach_left():
            self.points["RIGHT"] += 1
            self.serve_side = "LEFT"
        elif self.ball.is_reach_right():
            self.points["LEFT"] += 1
            self.serve_side = "RIGHT"
        # end game or continue
        if self.points["LEFT"] == MAX_POINT or self.points["RIGHT"] == MAX_POINT:
            self.state = GameState.FINISH
        else:
            self.init_ball_pos()
            self.state = GameState.SERVE

    def run(self) -> None:
        pyxel.run(self.update, self.draw)

    def update(self) -> None:
        # move left paddle
        if pyxel.btn(pyxel.KEY_W):
            self.paddles[0].move_up()
        if pyxel.btn(pyxel.KEY_S):
            self.paddles[0].move_down()
        # move right paddle
        if pyxel.btn(pyxel.KEY_O):
            self.paddles[1].move_up()
        if pyxel.btn(pyxel.KEY_L):
            self.paddles[1].move_down()
        # update ball
        self.ball.update()
        if self.state == GameState.SERVE:
            self.serve_state()
        elif self.state == GameState.GAME:
            self.game_state()

    def draw(self) -> None:
        pyxel.cls(0)
        self.ball.draw()
        for paddle in self.paddles:
            paddle.draw()
        # draw field
        pyxel.rectb(0, 0, GAME_WIDTH, GAME_HEIGHT, 7)
        for i in range(GAME_HEIGHT // 2):
            pyxel.pset(GAME_WIDTH // 2, i * 2, 7)
        # draw point
        pyxel.text(GAME_WIDTH // 2 + 4, 4, f"{self.points['RIGHT']:02}", 7)
        pyxel.text(GAME_WIDTH // 2 - 12, 4, f"{self.points['LEFT']:02}", 7)

        if self.state == GameState.FINISH:
            if self.points["LEFT"] == MAX_POINT:
                winner = "LEFT"
            else:
                winner = "RIGHT"
            pyxel.text(GAME_WIDTH // 2 - (len(winner) * 4) // 2, 26, winner, 8)
            pyxel.text(GAME_WIDTH // 2 - 5, 34, "win!", 8)


if __name__ == "__main__":
    game = Game()
    game.run()
