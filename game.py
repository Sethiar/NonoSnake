import pygame
from pygame.locals import *

from bombs import Bombs
from items import Items

from itemsappear import Itemsappear

from snakesegment import SnakeSegment

class GameScreen:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.screen_color = (0, 0, 0)
        self.tool_color = (255, 255, 255)
        self.snake_speed_x = 1
        self.snake_speed_y = 1
        self.direction_x = 0
        self.direction_y = 0
        self.snake_segments = []
        self.create_snake()
        self.clock = pygame.time.Clock()
        self.snake_height = 15
        self.snake_width = 60
        self.is_game_over = False
        self.game_over_displayed = False


        self.bombgreen = Bombs(20, 90)
        self.bombgreen.change_bomb_type('bombgreen')
        self.bombred = Bombs(220, 420)
        self.bombred.change_bomb_type("bombred")
        self.animation_counter = 0
        self.animation_speed = 5

        self.applegolden = Items(50, 220)
        self.applegolden.change_apple_type('applegolden')

        self.items = Itemsappear(200, 190)

    def create_snake(self):
        self.snake_segments = [SnakeSegment(10,20, 20, 60)]


    def update_chain(self):
        current_segment = self.snake_segments[0]
        while current_segment.previous_segment:
            # Mettez à jour la position du segment en fonction de la position du segment précédent
            current_segment.x = current_segment.previous_segment.x
            current_segment.y = current_segment.previous_segment.y
            # Déplacez le segment de sa longueur
            current_segment.x += current_segment.length
            current_segment = current_segment.previous_segment



    def game_over(self):
        # Charger le fond d'écran
        self.background_gameover = pygame.image.load("image/game_over.jpg")
        self.background_gameover = pygame.transform.scale(self.background_gameover, (500, 700))

        # Effacer l'écran
        self.fenetre.fill(self.screen_color)

        # Afficher le fond d'écran
        self.fenetre.blit(self.background_gameover, (0, 0))

        # Ajouter un titre
        title_font = pygame.font.Font("font/Acme-Regular.ttf", 38)
        title_text = title_font.render("Game Over", True, pygame.Color("#a92c11"))
        title_frame = pygame.Rect(230, 90, 210, 65)
        pygame.draw.rect(self.fenetre, pygame.Color("black"), title_frame)
        pygame.draw.rect(self.fenetre, pygame.Color("#a92c11"), title_frame, 3)

        sentence_text = title_font.render("Tu es devenu un joli sac à main !!", True, pygame.Color("#FFC300"))
        sentence_position = (10, 630)
        sentence_title_frame = pygame.Rect(0, 620, 500, 65)
        pygame.draw.rect(self.fenetre, pygame.Color("black"), sentence_title_frame)
        pygame.draw.rect(self.fenetre, pygame.Color("#FFC300"), sentence_title_frame, 3)
        title_position = (self.fenetre.get_width() // 2, 100)
        self.fenetre.blit(sentence_text, sentence_position)
        self.fenetre.blit(title_text, title_position)

        pygame.display.update()

    def run_game(self):
        running = True
        FPS = 80
        game_over_displayed = False  # Variable pour indiquer si l'écran de fin de jeu a été affiché
        FPS = 80
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if not self.is_game_over:

                # Déplacement du serpent
                keys = pygame.key.get_pressed()

                if keys[K_UP] and self.direction_y != 1:
                    self.direction_x = 0
                    self.direction_y = -1
                    print("K_up")

                if keys[K_DOWN] and self.direction_y != -1:
                    self.direction_x = 0
                    self.direction_y = 1

                if keys[K_RIGHT] and self.direction_x != -1:
                    self.direction_x = 1
                    self.direction_y = 0

                if keys[K_LEFT] and self.direction_x != 1:
                    self.direction_x = -1
                    self.direction_y = 0

                self.snake_segments[0].rect.x += self.direction_x * self.snake_speed_x
                self.snake_segments[0].rect.y += self.direction_y * self.snake_speed_y
                self.update_chain()

                # Mise à jour des
                if (
                        self.snake_segments[0].rect.y < 0
                        or self.snake_segments[0].rect.y + self.snake_height >= 700
                        or self.snake_segments[0].rect.x < 0
                        or self.snake_segments[0].rect.x + self.snake_width >= 500
                        ):

                    self.is_game_over = True
                    print("Game Over")


                # Effacer l'écran
                self.fenetre.fill(self.screen_color)


                self.items.update()

                # Dessiner chaque segment du serpent
                for segment in self.snake_segments:
                    segment_rect = pygame.Rect(segment.rect.x, segment.rect.y, self.snake_width, self.snake_height)
                    pygame.draw.rect(self.fenetre, self.tool_color, segment_rect)

                # Mettre à jour l'animation de la bombe bombgreen
                if self.animation_counter % self.animation_speed == 0:
                    self.bombgreen.change_image()
                    self.bombred.change_image()
                self.animation_counter += 1

                self.bombgreen.draw_bombs(self.fenetre)
                self.bombred.draw_bombs(self.fenetre)

                self.applegolden.draw_apple(self.fenetre)
            else:
                if not game_over_displayed:
                    self.game_over()
                    game_over_displayed = True
                    pygame.display.flip()


            pygame.display.flip()

            # Control the FPS based on the desired speed
            self.clock.tick(FPS)

        pygame.quit()

