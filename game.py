import pygame
import random

from block import Block
from snake import Snake
from const import UP, DOWN, LEFT, RIGHT


class Game(object):
    _score = 0
    _running = True
    _food_color = pygame.Color(255, 0, 0)  # Red
    _snake_color = pygame.Color(0, 255, 0)  # Green
    _surface_color = pygame.Color(0, 0, 0)  # Black
    _score_color = pygame.Color(255, 255, 255)  # White

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
        clock = pygame.time.Clock()
        while self._running:
            clock.tick(self._tick_rate)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._game_over()
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    self._on_key_press(event)
            self._draw_game()

    def _food_collision(self):
        if self._food.get_position() == self._snake.get_head_position():
            self._score += 1
            with_food = True
            self._create_food()
            self._snake.update_position(with_food)
        else:
            self._snake.update_position()

    def _wall_collision(self):
        snake_head_position_x, snake_head_position_y = self._snake.get_head_position()
        if snake_head_position_x < 0 or snake_head_position_x > self._rows or snake_head_position_y < 0 or snake_head_position_y > self._rows:
            return True
        return False

    def _body_collision(self):
        snake_head_position = self._snake.get_head_position()
        snake_body_positions = self._snake.get_body_positions()
        if snake_head_position in snake_body_positions:
            return True
        return False

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
        if not self._body_collision() and not self._wall_collision():
            self._surface.fill(self._surface_color)
            self._food.draw()
            self._snake.draw()
            self._food_collision()
            self._show_score()
            pygame.display.update()

    def _show_score(self):
        score_font = pygame.font.SysFont('consolas', 20)
        score_surface = score_font.render('Score : ' + str(self._score), True, self._score_color)
        score_rect = score_surface.get_rect()
        score_rect.midtop = (self._size/10, 15)
        self._surface.blit(score_surface, score_rect)

    def run(self):
        pygame.init()
        pygame.display.set_caption('Snake AI')
        self._create_food()
        self._create_snake()
        self._loop()
