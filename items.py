import pygame


class Items:
    def __init__(self, x, y):
        self.images = {'applegolden': [], 'applenormal': [], 'applerotten': []}
        self.load_images()
        self.apple_type = 'applegolden'
        self.image_index = 0
        self.image = self.images[self.apple_type][self.image_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def load_images(self):

        apple_golden = pygame.image.load("pixelart/apples_pack/apple_golden.png")
        rect_applegolden = (0, 0, 30, 30)  # Les coordonnées du rectangle
        # Utilisez les coordonnées du rectangle pour créer la surface
        image = pygame.Surface((rect_applegolden[2], rect_applegolden[3]), pygame.SRCALPHA).convert()
        image.blit(apple_golden, (0, 0), rect_applegolden)
        image = pygame.transform.scale(image, (30, 30))
        self.images['applegolden'].append(image)

        apple_normal = pygame.image.load("pixelart/apples_pack/apple_regular.png")
        rect_appelnormal = (0, 0, 30, 30)  # Les coordonnées du rectangle
        # Utilisez les coordonnées du rectangle pour créer la surface
        image = pygame.Surface((rect_appelnormal[2], rect_appelnormal[3]), pygame.SRCALPHA).convert()
        image.blit(apple_normal, (0, 0), rect_appelnormal)
        image = pygame.transform.scale(image, (30, 30))
        self.images['applenormal'].append(image)

        apple_rotten = pygame.image.load("pixelart/apples_pack/apple_rotten.png")
        rect_appelrotten = (0, 0, 30, 30)  # Les coordonnées du rectangle
        # Utilisez les coordonnées du rectangle pour créer la surface
        image = pygame.Surface((rect_appelrotten[2], rect_appelrotten[3]), pygame.SRCALPHA).convert()
        image.blit(apple_rotten, (0, 0), rect_appelrotten)
        image = pygame.transform.scale(image, (30, 30))
        self.images['applerotten'].append(image)



    def change_apple_type(self, apple_type):
        self.apple_type = apple_type
        self.image_index = 0
        self.image = self.images[self.apple_type][self.image_index]

    def draw_apple(self, fenetre):
        fenetre.blit(self.image, (self.rect.x, self.rect.y))