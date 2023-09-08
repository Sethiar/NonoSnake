import pygame


class Bombs(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = {'bombgreen': [], 'bombice': [], 'bombred': [], 'bombsound': []}
        self.load_images()
        self.bomb_type = 'bombgreen'
        self.image_index = 0
        self.image = self.images[self.bomb_type][self.image_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def load_images(self):
        spritesheet_bombgreen = pygame.image.load("pixelart/bombs/bombgreen/idel.png")
        self.image_rects_bombgreen = [
            (10, 20, 30, 30),
            (60, 20, 30, 30)
        ]
        for rect in self.image_rects_bombgreen:
            image = pygame.Surface(rect[2:], pygame.SRCALPHA).convert()
            image.blit(spritesheet_bombgreen, (0, 0), rect)
            image = pygame.transform.scale(image, (30, 30))
            self.images['bombgreen'].append(image)

        spritesheet_bombice = pygame.image.load("pixelart/bombs/bombice/idel.png")
        self.image_rects_bombice = [
            (10, 20, 30, 30),
        ]
        for rect in self.image_rects_bombice:
            image = pygame.Surface(rect[2:], pygame.SRCALPHA).convert()
            image.blit(spritesheet_bombice, (0, 0), rect)
            image = pygame.transform.scale(image, (30, 30))
            self.images['bombice'].append(image)

        spritesheet_bombred = pygame.image.load("pixelart/bombs/bombred/idel.png")
        self.image_rects_bombred = [
            (10, 20, 30, 30),
            (60, 20, 30, 30),
            (110, 20, 30, 30)
        ]
        for rect in self.image_rects_bombred:
            image = pygame.Surface(rect[2:], pygame.SRCALPHA).convert()
            image.blit(spritesheet_bombred, (0, 0), rect)
            image = pygame.transform.scale(image, (30, 30))
            self.images['bombred'].append(image)

        spritesheet_bombsound = pygame.image.load("pixelart/bombs/bombsound/idel.png")
        self.image_rects_bombsound = [
            (10, 20, 30, 30),
            (60, 20, 30, 30),
            (110, 20, 30, 30),
            (160, 20, 30, 30)
        ]
        for rect in self.image_rects_bombsound:
            image = pygame.Surface(rect[2:], pygame.SRCALPHA).convert()
            image.blit(spritesheet_bombsound, (0, 0), rect)
            image = pygame.transform.scale(image, (30, 30))
            self.images['bombsound'].append(image)

        spritesheet_exicebomb = pygame.image.load("pixelart/bombs/bombice/exp_ice.png")

        spritesheet_exredbomb = pygame.image.load("pixelart/bombs/bombred/expl_bomb.png")

        spritesheet_exgreenbomb = pygame.image.load("pixelart/bombs/bombgreen/expl_green.png")

        spritesheet_exsoundbomb = pygame.image.load("pixelart/bombs/bombsound/sound_ex.png")

    def change_bomb_type(self, bomb_type):
        self.bomb_type = bomb_type
        self.image_index = 0
        self.image = self.images[self.bomb_type][self.image_index]

    def change_image(self):
        self.image_index = (self.image_index + 1) % len(self.images[self.bomb_type])
        self.image = self.images[self.bomb_type][self.image_index]

    def draw_bombs(self, fenetre):
        fenetre.blit(self.image, (self.rect.x, self.rect.y))


