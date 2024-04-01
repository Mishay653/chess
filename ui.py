import pygame
import pygame_menu
from pygame_menu import themes
import subprocess


pygame.init()
surface = pygame.display.set_mode((600, 400))


def start_the_game():
    subprocess.call(["python", "main.py"])


mainmenu = pygame_menu.Menu('Дароу', 600, 400, theme=themes.THEME_DARK)
mainmenu.add.button('Игра с другом', start_the_game)
mainmenu.add.button('Выход', pygame_menu.events.EXIT)

mainmenu.mainloop(surface)