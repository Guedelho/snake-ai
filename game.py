import pygame
import random

from block import Block
from snake import Snake
from const import UP, DOWN, LEFT, RIGHT


class Game(object):
    _food_color = pygame.Color(255, 0, 0)  # Red
    _snake_color = pygame.Color(0, 255, 0)  # Green
    _surface_color = pygame.Color(0, 0, 0)  # Black
    _line_color = pygame.Color(255, 255, 255)  # White

    def __init__(self, size, rows, tick_rate):
        self._size = size
        self._rows = rows
        self._tick_rate = tick_rate
        self._block_size = size // rows
        self._surface = pygame.display.set_mode((self._size, self._size))

    def _create_food(self):
        position = [random.randrange(self._block_size),
                    random.randrange(self._block_size)]
        self._food = Block(self._surface, self._food_color,
                           position, self._block_size)

    def _create_snake(self):
        position = [5, 10]
        self._snake = Snake(self._surface, self._snake_color,
                            position, self._block_size)

    def _loop(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            clock.tick(self._tick_rate)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    self._on_key_press(event)
            self._draw_game()

    def _food_collision(self):
        if self._food.get_position() == self._snake.get_head_position():
            with_food = True
            self._create_food()
            self._snake.update_position(with_food)
        else:
            self._snake.update_position()

    def _on_key_press(self, event):
        if event.key == pygame.K_UP:
            self._snake.update_direction(UP)
        elif event.key == pygame.K_DOWN:
            self._snake.update_direction(DOWN)
        elif event.key == pygame.K_LEFT:
            self._snake.update_direction(LEFT)
        elif event.key == pygame.K_RIGHT:
            self._snake.update_direction(RIGHT)

    def _draw_game(self):
        self._surface.fill(self._surface_color)
        self._food.draw()
        self._snake.draw()
        self._food_collision()
        pygame.display.update()

    def run(self):
        pygame.init()
        pygame.display.set_caption('Snake AI')
        self._create_food()
        self._create_snake()
        self._loop()
