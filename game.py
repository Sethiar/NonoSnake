import pygame
from pygame.locals import *

from bombs import Bombs
from items import Items

from itemsappear import Itemsappear

class GameScreen:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.screen_color = (0, 0, 0)
        self.tool_color = (255, 255, 255)
        self.snake_length = 90
        self.snake_x = 10
        self.snake_y = 20
        self.snake_speed_x = 1
        self.snake_speed_y = 1
        self.direction_x = 0
        self.direction_y = 0
        self.snake_segments = []
        self.create_snake()
        self.clock = pygame.time.Clock()

        self.bombgreen = Bombs(20, 90)
        self.bombgreen.change_bomb_type('bombgreen')
        self.bombred = Bombs(220, 420)
        self.bombred.change_bomb_type("bombred")
        self.animation_counter = 0
        self.animation_speed = 5

        self.applegolden = Items(50, 220)
        self.applegolden.change_apple_type('applegolden')

        self.items = Itemsappear(150, 300)

    def create_snake(self):
        self.snake_segments.append(pygame.Rect(self.snake_x, self.snake_y, self.snake_length, 30))

    def game_over(self):
        self.background_gameover = pygame.image.load("image/game_over.jpg")
        self.background_gameover = pygame.transform.scale(self.background_gameover, (500, 700))

        # Ajouter un titre
        title_font = pygame.font.Font("font/Acme-Regular.ttf", 38)
        title_text = title_font.render("Game Over", True, pygame.Color("gold"))
        title_position = (self.fenetre.get_width() // 2, 50)
        self.fenetre.blit(title_text, title_position)

        pygame.display.update()

    def run_game(self):
        running = True
        FPS = 80
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Déplacement du serpent
            keys = pygame.key.get_pressed()

            if keys[K_UP] and self.direction_y != 1:
                self.direction_x = 0
                self.direction_y = -1

            if keys[K_DOWN] and self.direction_y != -1:
                self.direction_x = 0
                self.direction_y = 1

            if keys[K_RIGHT] and self.direction_x != -1:
                self.direction_x = 1
                self.direction_y = 0

            if keys[K_LEFT] and self.direction_x != 1:
                self.direction_x = -1
                self.direction_y = 0

            for i in range(len(self.snake_segments) - 1, 0, -1):
                self.snake_segments[i] = self.snake_segments[i - 1].copy()

            self.snake_segments[0].x += self.direction_x * self.snake_speed_x
            self.snake_segments[0].y += self.direction_y * self.snake_speed_y

            # Check for game over conditions
            if (
                    self.snake_segments[0].y < 0
                    or self.snake_segments[0].y > 700
                    or self.snake_segments[0].x < 0
                    or self.snake_segments[0].x > 500
            ):
                self.game_over()
                print("Game Over")


            # Clear the screen
            self.fenetre.fill(self.screen_color)

            # Draw each segment of the snake
            for segment in self.snake_segments:
                pygame.draw.rect(self.fenetre, self.tool_color, segment)

            # Mettre à jour l'animation de la bombe bombgreen
            if self.animation_counter % self.animation_speed == 0:
                self.bombgreen.change_image()
                self.bombred.change_image()
            self.animation_counter += 1

            self.bombgreen.draw_bombs(self.fenetre)
            self.bombred.draw_bombs(self.fenetre)

            self.applegolden.draw_apple(self.fenetre)
            self.apple_type.draw(self.fenetre)

            pygame.display.flip()
            # Control the FPS based on the desired speed
            self.clock.tick(FPS)

        pygame.quit()

