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

    def add_block(self):
        position = ()
        tail = self._body[-1]
        x, y = tail.position
        dir_x, dir_y = tail.direction

        if dir_x == 1 and dir_y == 0:
            position = (x-1, y)
        elif dir_x == -1 and dir_y == 0:
            position = (x+1, y)
        elif dir_x == 0 and dir_y == 1:
            position = (x, y-1)
        elif dir_x == 0 and dir_y == -1:
            position = (x, y+1)

        self._body.append(Block(self._surface, self._color,
                                position, self._block_size, (dir_x, dir_y)))

    def update_direction(self, dir_x, dir_y):
        self.head.direction = (dir_x, dir_y)
        self._turns[self.head.position[:]] = [dir_x, dir_y]

    def draw(self):
        for i, block in enumerate(self._body):
            self._move(block).draw()

            position = block.position[:]
            x, y = position
            dir_x, dir_y = block.direction

            if position in self._turns:
                block.direction = self._turns[position]
                if i == len(self._body)-1:
                    self._turns.pop(position)
            else:
                if dir_x == -1 and x <= 0:
                    block.position = (self._block_size-1, y)
                elif dir_x == 1 and x >= self._block_size-1:
                    block.position = (0, y)
                elif dir_y == 1 and y >= self._block_size-1:
                    block.position = (x, 0)
                elif dir_y == -1 and y <= 0:
                    block.position = (x, self._block_size-1)
                else:
                    block.direction = (dir_x, dir_y)
