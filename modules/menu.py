import pygame
import sys
from helper import BLACK, RED, GREEN


class Menu:
    def __init__(self, set_name, MenuSettings, gameplay):
        self.screen_width = 1920
        self.screen_height = 1080
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height), pygame.FULLSCREEN
        )
        self.font = pygame.font.Font("fonts/SAIBA-45-Regular-(v1.1).otf", 36)
        self.running = True
        self.set_name = set_name
        self.MenuSettings = MenuSettings
        self.gameplay = gameplay

    def menu_settings(
        self, settings, change_sound, set_default_setings, change_language, clock, fps
    ):
        while self.running:
            if self.MenuSettings(self.screen, settings).run(
                change_language, set_default_setings, change_sound, clock, fps
            ):
                return True
            else:
                self.running = False

    def display_menu(
        self,
        settings,
        change_language,
        set_default_setings,
        change_sound,
        change_name,
        clock,
        fps,
    ):
        quit_botton_rect = pygame.Rect(760, 700, 400, 200)
        settings_botton_rect = pygame.Rect(760, 450, 400, 200)
        play_button_rect = pygame.Rect(760, 200, 400, 200)
        # Переменная для отслеживания нахождения курсора над кнопкой
        cursor_over_button_play = False
        play_button_color = RED
        cursor_over_button_quit = False
        quit_button_color = RED
        cursor_over_button_settings = False
        settings_button_color = RED

        while self.running:
            play_text = self.font.render(
                settings["language"][settings["language"]["current"]]["Play"],
                True,
                BLACK,
            )
            settings_text = self.font.render(
                settings["language"][settings["language"]["current"]]["Settings"],
                True,
                BLACK,
            )
            quit_text = self.font.render(
                settings["language"][settings["language"]["current"]]["Quit"],
                True,
                BLACK,
            )
            self.screen.fill((32, 160, 245))
            pygame.draw.rect(self.screen, play_button_color, play_button_rect)
            pygame.draw.rect(self.screen, settings_button_color, settings_botton_rect)
            pygame.draw.rect(self.screen, quit_button_color, quit_botton_rect)
            self.screen.blit(
                play_text,
                (
                    play_button_rect.centerx - play_text.get_width() // 2,
                    play_button_rect.centery - play_text.get_height() // 2,
                ),
            )
            self.screen.blit(
                settings_text,
                (
                    settings_botton_rect.centerx - settings_text.get_width() // 2,
                    settings_botton_rect.centery - settings_text.get_height() // 2,
                ),
            )
            self.screen.blit(
                quit_text,
                (
                    quit_botton_rect.centerx - quit_text.get_width() // 2,
                    quit_botton_rect.centery - quit_text.get_height() // 2,
                ),
            )

            pygame.display.update()

            if cursor_over_button_play:
                play_button_color = GREEN
            else:
                play_button_color = RED
            if cursor_over_button_quit:
                quit_button_color = GREEN
            else:
                quit_button_color = RED
            if cursor_over_button_settings:
                settings_button_color = GREEN
            else:
                settings_button_color = RED

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if play_button_rect.collidepoint(event.pos):
                            # Запуск игры
                            cursor_over_button_play = False
                            if settings["name"] == "NULL":
                                if (
                                    self.set_name(self.screen).input_name(
                                        settings, change_name, clock, fps
                                    )
                                    == False
                                ):
                                    pygame.quit()
                                    sys.exit()
                                    self.running = False
                            if self.gameplay(self.screen) == False:
                                pygame.quit()
                                sys.exit()
                                self.running = False
                        elif quit_botton_rect.collidepoint(event.pos):
                            pygame.quit()
                            sys.exit()
                            self.running = False
                        elif settings_botton_rect.collidepoint(event.pos):
                            cursor_over_button_settings = False
                            if (
                                self.MenuSettings(self.screen, settings).run(
                                    change_language,
                                    set_default_setings,
                                    change_sound,
                                    clock,
                                    fps,
                                )
                                == False
                            ):
                                self.running = False
                elif event.type == pygame.MOUSEMOTION:
                    if quit_botton_rect.collidepoint(event.pos):
                        cursor_over_button_quit = True
                    else:
                        cursor_over_button_quit = False
                    if play_button_rect.collidepoint(event.pos):
                        cursor_over_button_play = True
                    else:
                        cursor_over_button_play = False
                    if settings_botton_rect.collidepoint(event.pos):
                        cursor_over_button_settings = True
                    else:
                        cursor_over_button_settings = False
            clock.tick(fps)
