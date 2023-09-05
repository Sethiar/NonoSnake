import pygame

from menu import MenuScreen




pygame.init()

fenetre = pygame.display.set_mode((500, 700))
pygame.display.set_caption("Nosiris's Snake")

menu_screen = MenuScreen(fenetre)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    menu_screen.run_menu()
