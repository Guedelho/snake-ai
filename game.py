import pygame
import random
import constants as Const

from block import Block
from snake import Snake
from constants import UP, DOWN, LEFT, RIGHT, RED, BLACK, GREEN, WHITE


class Game(object):

    def __init__(self, size, rows, fps):
        self._score = 0
        self._fps = fps
        self._size = size
        self._rows = rows
        self._running = True
        self._block_size = size // rows
        self._surface = pygame.display.set_mode((self._size, self._size))

    def _create_food(self):
        position = [random.randrange(self._block_size),
                    random.randrange(self._block_size)]
        self._food = Block(self._surface, RED,
                           position, self._block_size)

    def _create_snake(self):
        position = [5, 10]
        self._snake = Snake(self._surface, GREEN,
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
            self._create_food()
            self._snake.update_position(food=True)
        else:
            self._snake.update_position()

    def _has_hit_the_wall(self):
        x, y = self._snake.get_head_position()
        return x < 0 or x > self._rows or y < 0 or y > self._rows

    def _has_hit_the_body(self):
        return self._snake.get_head_position() in self._snake.get_body_positions()

    def _on_key_press(self, event):
        direction = RIGHT
        if event.key == pygame.K_UP:
            direction = UP
        elif event.key == pygame.K_DOWN:
            direction = DOWN
        elif event.key == pygame.K_LEFT:
            direction = LEFT
        elif event.key == pygame.K_RIGHT:
            direction = RIGHT
        self._snake.update_direction(direction)

    def _draw_game(self):
        if self._has_hit_the_body() or self._has_hit_the_wall():
            self._game_over()
        else:
            self._surface.fill(BLACK)
            self._food.draw()
            self._snake.draw()
            self._food_collision()
            self._show_score()
            pygame.display.update()

    def _show_score(self, is_game_over=False):
        score_font = pygame.font.SysFont('times', 30)
        score_surface = score_font.render(
            'Score : ' + str(self._score), True, WHITE)
        score_rect = score_surface.get_rect()
        if not is_game_over:
            score_rect.midtop = (self._size/10, 15)
        else:
            score_rect.midtop = (self._size/2, self._size/2)
        self._surface.blit(score_surface, score_rect)

    def _game_over(self):
        my_font = pygame.font.SysFont('times new roman', 90)
        game_over_surface = my_font.render('GAME OVER', True, WHITE)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (self._size/2, self._size/4)
        self._surface.fill(BLACK)
        self._surface.blit(game_over_surface, game_over_rect)
        self._show_score(True)
        pygame.display.flip()

    def run(self):
        pygame.init()
        pygame.display.set_caption('Snake AI')
        self._create_food()
        self._create_snake()
        self._loop()
