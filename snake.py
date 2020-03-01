import pygame

from block import Block
from const import UP, DOWN, LEFT, RIGHT


class Snake(object):
    _direction = RIGHT

    def __init__(self, surface, color, position, block_size):
        self._color = color
        self._surface = surface
        self._block_size = block_size
        self._body = [Block(surface, color, position, block_size)]

    def update_direction(self, new_direction):
        if new_direction == UP and self._direction != DOWN:
            self._direction = UP
        elif new_direction == DOWN and self._direction != UP:
            self._direction = DOWN
        elif new_direction == LEFT and self._direction != RIGHT:
            self._direction = LEFT
        elif new_direction == RIGHT and self._direction != LEFT:
            self._direction = RIGHT

    def update_position(self, food=False):
        x, y = self._body[0].get_position()
        new_position = []
        if self._direction == UP:
            new_position = [x, y-1]
        elif self._direction == DOWN:
            new_position = [x, y+1]
        elif self._direction == LEFT:
            new_position = [x-1, y]
        elif self._direction == RIGHT:
            new_position = [x+1, y]
        self._body.insert(0, Block(self._surface, self._color,
                                   new_position, self._block_size))
        if not food:
            self._body.pop()

    def get_head_position(self):
        return self._body[0].get_position()

    def get_body_positions(self):
        return [block.get_position() for block in self._body[1:]]

    def draw(self):
        for block in self._body:
            block.draw()
