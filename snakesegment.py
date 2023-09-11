import pygame


class SnakeSegment:
    def __init__(self, x, y, direction_x, direction_y, previous_segment=None):
        self.snake_height = 15
        self.snake_width = 60
        self.rect = pygame.Rect(x, y, self.snake_width, self.snake_height)
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.previous_segment = previous_segment

    def move(self):
        self.rect.x += self.direction_x
        self.rect.y += self.direction_y


