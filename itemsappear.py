import pygame
import random

from items import Items

# Définir des constantes pour les dimensions de l'écran
LARGEUR_ECRAN = 500
HAUTEUR_ECRAN = 700


class Itemsappear(Items):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.delay_appear = 100
        self.delay_disappear = 0
        self.delay_timer = 0

    def update(self):
        self.delay_timer -= 1
        if self.delay_appear <= 0:
            self.appear_apple_random()
            self.delay_timer = self.delay_appear

        if self.delay_disappear == 300:
            self.kill()

    def appear_apple_random(self):
        x = random.randint(0, LARGEUR_ECRAN - 30)
        y = random.randint(0, HAUTEUR_ECRAN - 30)
        apple_types = ['applegolden', 'applenormal', 'applerotten']
        apple_type = random.choice(apple_types)
        new_apple = Items(apple_type, x, y)
        self.apple.add(new_apple)

    def position_apple(self):
        apples_position = [(apple.rect.x, apple.rect.y) for apple in self.apples]
        return apples_position


