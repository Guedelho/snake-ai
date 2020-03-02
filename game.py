import pygame
import random

from block import Block
from snake import Snake
from constants import UP, DOWN, LEFT, RIGHT


class Game(object):
    _score = 0
    _running = True
    _red = pygame.Color(255, 0, 0)
    _black = pygame.Color(0, 0, 0)
    _green = pygame.Color(0, 255, 0)
    _white = pygame.Color(255, 255, 255)

    def __init__(self, size, rows, fps):
        self._fps = fps
        self._size = size
        self._rows = rows
        self._block_size = size // rows
        self._surface = pygame.display.set_mode((self._size, self._size))

    def _create_food(self):
        position = [random.randrange(self._block_size),
                    random.randrange(self._block_size)]
        self._food = Block(self._surface, self._red,
                           position, self._block_size)

    def _create_snake(self):
        position = [5, 10]
        self._snake = Snake(self._surface, self._green,
                            position, self._block_size)

    def _loop(self):
        clock = pygame.time.Clock()
        while self._running:
            clock.tick(self._fps)
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

    def _has_hit_the_wall(self):
        x, y = self._snake.get_head_position()
        if x < 0 or x > self._rows or y < 0 or y > self._rows:
            return True
        return False

    def _has_hit_the_body(self):
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
        if not self._has_hit_the_body() and not self._has_hit_the_wall():
            self._surface.fill(self._black)
            self._food.draw()
            self._snake.draw()
            self._food_collision()
            self._show_score()
            pygame.display.update()
        else:
            self._game_over()

    def _show_score(self, is_game_over=False):
        score_font = pygame.font.SysFont('times', 30)
        score_surface = score_font.render(
            'Score : ' + str(self._score), True, self._white)
        score_rect = score_surface.get_rect()
        if not is_game_over:
            score_rect.midtop = (self._size/10, 15)
        else:
            score_rect.midtop = (self._size/2, self._size/2)
        self._surface.blit(score_surface, score_rect)

    def _game_over(self):
        my_font = pygame.font.SysFont('times new roman', 90)
        game_over_surface = my_font.render('GAME OVER', True, self._white)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (self._size/2, self._size/4)
        self._surface.fill(self._black)
        self._surface.blit(game_over_surface, game_over_rect)
        self._show_score(True)
        pygame.display.flip()

    def run(self):
        pygame.init()
        pygame.display.set_caption('Snake AI')
        self._create_food()
        self._create_snake()
        self._loop()
