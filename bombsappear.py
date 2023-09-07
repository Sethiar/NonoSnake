import pygame


class ItemsAppear(pygame.sprite.Sprite):
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
        self.apple_images = {'applegolden': [], 'applenormal': [], 'applerotten': []}
        self.apple_type = 'applegolden'
        self.apple_image_index = 0
        self.apple_image = self.apple_images[self.apple_type][self.apple_image_index]
        self.load_images()

    def load_images(self):
        apple_golden = pygame.image.load("pixelart/apples_pack/apple_golden.png")
        rect_applegolden = [(0, 0, 30, 30)]
        image_applegolden = pygame.Surface(rect_applegolden[2:], pygame.SRCALPHA).convert()
        image_applegolden.blit(apple_golden, (0, 0), rect_applegolden)
        image_applegolden = pygame.transform.scale(image_applegolden, (30, 30))
        self.apple_images['applegolden'].append(image_applegolden)

        apple_normal = pygame.image.load("pixelart/apples_pack/apple_regular.png")
        rect_applenormal = [(0, 0, 30, 30)]
        image = pygame.Surface(rect_applenormal[2:], pygame.SRCALPHA).convert()
        image.blit(apple_normal, (0, 0), rect_applenormal)
        image = pygame.transform.scale(image, (30, 30))
        self.apple_images['applenormal'].append(image)

        apple_rotten = pygame.image.load("pixelart/apples_pack/apple_rotten.png")
        self.rect_applerotten = [
            (0, 0, 30, 30)
        ]
        for rect in self.rect_applerotten:
            image = pygame.Surface(rect[2:], pygame.SRCALPHA).convert()
            image.blit(apple_rotten, (0, 0), rect)
            image = pygame.transform.scale(image, (30, 30))
            self.apple_images['applerotten'].append(image)

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

    def change_apple_type(self, apple_type):
        self.apple_type = apple_type
        self.apple_image_index = 0
        self.apple_image = self.apple_images[self.apple_type][self.apple_image_index]

    def draw_apple(self, fenetre):
        fenetre.blit(self.apple_image, (self.rect.x, self.rect.y))
