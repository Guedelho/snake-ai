import pygame
from game import Game


def main():
    game = Game(size=600, rows=30, fps=20)
    game.run()


if __name__ == "__main__":
    main()
