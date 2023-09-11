import pygame
import random

from items import Items

class Itemsappear(Items):
    def __init__(self, screen_width, screen_height):
        self.screen_width = 500
        self.screen_height = 700
        self.delay_appear = 0
        self.delay_disappear = 0
        self.delay_timer = 0
        self.apple = None

    def update(self):
        self.delay_timer += 1
        self.delay_disappear += 1

        if self.delay_appear >= 180:
            self.spawn_apple()
            self.delay_appear = 0

        if self.delay_disappear >= 600:
            self.remove_apple()
            self.delay_disappear = 0

        if self.apple:
            self.apple.update()

    def spawn_apple(self):
        x = random.randint(0, self.screen_width - 30)
        y = random.randint(0, self.screen_height - 30)
        apple_types = ['applegolden', 'applenormal', 'applerotten']
        apple_type = random.choice(apple_types)
        self.apple = Items(apple_type, x, y)

    def remove_apple(self):
        if self.apple:
            self.apple.kill()
            self.apple = None



