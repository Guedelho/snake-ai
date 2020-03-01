import pygame


class Block(object):
    def __init__(self, surface, color, position, block_size):
        self._color = color
        self._surface = surface
        self._position = position
        self._block_size = block_size

    def draw(self):
        x = self._position[0]
        y = self._position[1]

        pygame.draw.rect(self._surface, self._color, (x*self._block_size,
                                                      y*self._block_size,
                                                      self._block_size,
                                                      self._block_size))

    def get_position(self):
        return self._position
