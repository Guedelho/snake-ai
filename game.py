import pygame
import random

from block import Block
from snake import Snake


class Game(object):
    _food_color = (255, 0, 0)  # Red
    _snake_color = (0, 255, 0)  # Green
    _surface_color = (0, 0, 0)  # Black
    _line_color = (255, 255, 255)  # White

    def __init__(self, size, rows, tick_rate):
        self._size = size
        self._rows = rows
        self._tick_rate = tick_rate
        self._block_size = size // rows
        self._surface = pygame.display.set_mode((size, size))

    def _create_food(self):
        position = (random.randrange(self._rows), random.randrange(self._rows))
        self._food = Block(self._surface, self._food_color,
                           position, self._block_size)

    def _create_snake(self):
        snake_initial_position = (5, 10)
        self._snake = Snake(self._surface, self._snake_color,
                            snake_initial_position, self._block_size)

    def _loop(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            clock.tick(self._tick_rate)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    self._on_key_press()
            self._draw_game()

    def _draw_game(self):
        self._surface.fill(self._surface_color)
        self._food.draw()
        self._snake.draw()
        self._food_collision()
        pygame.display.update()

    def _food_collision(self):
        if self._snake.head.position == self._food.position:
            self._snake.add_block()
            self._create_food()

    def _on_key_press(self):
        keys = pygame.key.get_pressed()

        for key in keys:
            if keys[pygame.K_LEFT]:
                self._snake.update_direction(-1, 0)
            if keys[pygame.K_RIGHT]:
                self._snake.update_direction(1, 0)
            if keys[pygame.K_UP]:
                self._snake.update_direction(0, -1)
            if keys[pygame.K_DOWN]:
                self._snake.update_direction(0, 1)

    def run(self):
        self._create_food()
        self._create_snake()
        self._loop()
