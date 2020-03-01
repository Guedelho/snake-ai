import pygame

from block import Block


class Snake(object):
    _body = []
    _turns = {}

    def __init__(self, surface, color, position, block_size):
        self._color = color
        self.head = Block(surface, color, position, block_size)
        self._body.append(self.head)
        self._surface = surface
        self._block_size = block_size

    def _move(self, block):
        x, y = block.position
        dir_x, dir_y = block.direction
        block.position = (x + dir_x, y + dir_y)
        return block

    def _turns_control(self):
        # TODO

    def add_block(self):
        tail = self._body[-1]
        x, y = tail.position
        dir_x, dir_y = tail.direction

        if dir_x == 1 and dir_y == 0:
            self._body.append(
                Block(self._surface, self._color, (x-1, y), self._block_size))
        elif dir_x == -1 and dir_y == 0:
            self._body.append(
                Block(self._surface, self._color, (x+1, y), self._block_size))
        elif dir_x == 0 and dir_y == 1:
            self._body.append(
                Block(self._surface, self._color, (x, y-1), self._block_size))
        elif dir_x == 0 and dir_y == -1:
            self._body.append(
                Block(self._surface, self._color, (x, y+1), self._block_size))

        self._body[-1].position = (x, y)

    def update_direction(self, dir_x, dir_y):
        self.head.direction = (dir_x, dir_y)
        self._turns[self.head.position[:]] = [dir_x, dir_y]

    def draw(self):
        for block in self._body:
            new_block = self._move(block)
            new_block.draw()