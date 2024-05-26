import pygame
from modules.menu import Menu
from modules.set_name import set_name
from modules.menuSettings import MenuSettings
from helper import (
    settings,
    change_sound,
    change_language,
    change_name,
    set_default_setings,
)
from modules.room import Room

# Название игры
pygame.display.set_caption("Wergrey")
# Иконка игры
icon = pygame.image.load("images/icons8-вестерн-48.png")
pygame.display.set_icon(icon)
# FPS
fps = 60
clock = pygame.time.Clock()


class LoadingScreen:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 608
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.loading_font = pygame.font.Font("fonts/SAIBA-45-Regular-(v1.1).otf", 80)
        self.png_loading = pygame.image.load(
            "images/background_with.png"
        ).convert_alpha()

    def display_loading_screen(self):
        for loading_int in range(1, 641):
            loading = pygame.Surface((loading_int, 48))
            loading.fill((63, 74, 92))
            loading = pygame.transform.scale(loading, (loading_int, 48))
            self.screen.blit(self.png_loading, (0, 0))
            text_for_loading = self.loading_font.render("Wergrey", True, "White")
            self.screen.blit(text_for_loading, (350, 130))
            self.screen.blit(loading, (80, 528))
            pygame.display.update()


def gameplay(screen):
    num = Room().run(screen, fps, clock)
    if num == False:
        return False
    elif num == "street":
        print("Виииин")


def main():
    pygame.init()

    LoadingScreen().display_loading_screen()

    Menu_main = Menu(set_name, MenuSettings, gameplay)
    Menu_main.display_menu(
        settings,
        change_language,
        set_default_setings,
        change_sound,
        change_name,
        clock,
        fps,
    )


if __name__ == "__main__":
    main()
