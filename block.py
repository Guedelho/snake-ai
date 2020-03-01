import pygame


class Block(object):
    def __init__(self, surface, color, position, block_size, direction=(1, 0)):
        self._color = color
        self._surface = surface
        self.position = position
        self.direction = direction
        self._block_size = block_size

    def draw(self):
        x = self.position[0]
        y = self.position[1]

        pygame.draw.rect(self._surface, self._color, (x*self._block_size,
                                                    y*self._block_size,
                                                    self._block_size,
                                                    self._block_size))