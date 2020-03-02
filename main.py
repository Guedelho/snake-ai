import pygame
from game import Game


def main():
    rows = 30
    size = 600
    fps = 20

    game = Game(size, rows, fps)
    game.run()


if __name__ == "__main__":
    main()
