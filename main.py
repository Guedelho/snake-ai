import pygame
from game import Game


def main():
    rows = 20
    size = 400
    tick_rate = 10

    game = Game(size, rows, tick_rate)
    game.run()


if __name__ == "__main__":
    main()
