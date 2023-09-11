import pygame


class SnakeSegment:
    def __init__(self, x, y, direction_x, direction_y):
        self.snake_height = 15
        self.snake_width = 60
        self.rect = pygame.Rect(x, y, self.snake_width, self.snake_height)
        self.direction_x = direction_x
        self.direction_y = direction_y