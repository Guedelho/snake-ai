import pygame
from game import Game


def main():
    rows = 20
    size = 400
    fps = 30

    game = Game(size, rows, fps)
    game.run()


if __name__ == "__main__":
    main()
