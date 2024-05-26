import pygame
import sys
from helper import BLACK, RED, GREEN, YELLOW, CYAN


class MenuSettings:
    def __init__(self, screen, settings):
        self.screen = screen
        self.font = pygame.font.Font("fonts/SAIBA-45-Regular-(v1.1).otf", 36)
        self.pfone_for_language_seting = pygame.Surface((1200, 100))
        self.pfone_for_language_seting.fill((255, 0, 0))  # RED
        self.pfone_for_reset_seting = pygame.Surface((1200, 100))
        self.pfone_for_reset_seting.fill(RED)
        self.pfone_for_reset_sound = pygame.Surface((1200, 100))
        self.pfone_for_reset_sound.fill(RED)

        self.exit_button_rect = pygame.Rect(100, 50, 200, 70)
        self.exit_button_color = (255, 0, 0)  # RED
        self.cursor_over_button_exit = False

        self.language_button_rect = pygame.Rect(1300, 165, 200, 70)
        self.language_button_color = (255, 255, 0)  # YELLOW
        self.cursor_over_button_language = False

        self.reset_button_rect = pygame.Rect(1300, 315, 200, 70)
        self.reset_button_color = YELLOW
        self.cursot_over_button_reset = False

        self.okno_sound_rect = pygame.Rect(1300, 465, 200, 70)
        self.okno_sound_color = YELLOW
        self.cursor_over_button_sound = False

        self.settings = settings

    def run(self, change_language, set_default_setings, change_sound, clock, fps):
        while True:
            text_for_language_setting = self.font.render(
                self.settings["language"][self.settings["language"]["current"]][
                    "Language"
                ],
                True,
                (0, 0, 0),
            )  # BLACK
            text = (
                "English" if self.settings["language"]["current"] == "en" else "Русский"
            )
            txt_for_reset_seting = self.font.render(
                self.settings["language"][self.settings["language"]["current"]][
                    "Settings reset"
                ],
                True,
                BLACK,
            )
            txt_reset = self.font.render(
                self.settings["language"][self.settings["language"]["current"]][
                    "Reset"
                ],
                True,
                BLACK,
            )
            exit_text = self.font.render(
                self.settings["language"][self.settings["language"]["current"]]["Exit"],
                True,
                (0, 0, 0),
            )  # BLACK
            txt_sound = self.font.render(
                self.settings["language"][self.settings["language"]["current"]][
                    "Sound"
                ],
                True,
                BLACK,
            )
            txt_sound_state = self.font.render(
                self.settings["language"][self.settings["language"]["current"]][
                    self.settings["sound"]
                ],
                True,
                BLACK,
            )
            language_text = self.font.render(text, True, (0, 0, 0))  # BLACK

            self.screen.fill((32, 160, 245))
            self.screen.blit(self.pfone_for_language_seting, (400, 150))
            self.screen.blit(text_for_language_setting, (420, 185))
            self.screen.blit(self.pfone_for_reset_seting, (400, 300))
            self.screen.blit(txt_for_reset_seting, (420, 335))
            self.screen.blit(self.pfone_for_reset_sound, (400, 450))
            self.screen.blit(txt_sound, (420, 485))

            pygame.draw.rect(self.screen, self.exit_button_color, self.exit_button_rect)
            self.screen.blit(
                exit_text,
                (
                    self.exit_button_rect.centerx - exit_text.get_width() // 2,
                    self.exit_button_rect.centery - exit_text.get_height() // 2,
                ),
            )

            pygame.draw.rect(
                self.screen, self.language_button_color, self.language_button_rect
            )
            self.screen.blit(
                language_text,
                (
                    self.language_button_rect.centerx - language_text.get_width() // 2,
                    self.language_button_rect.centery - language_text.get_height() // 2,
                ),
            )

            pygame.draw.rect(
                self.screen, self.reset_button_color, self.reset_button_rect
            )
            self.screen.blit(
                txt_reset,
                (
                    self.reset_button_rect.centerx - txt_reset.get_width() // 2,
                    self.reset_button_rect.centery - txt_reset.get_height() // 2,
                ),
            )

            pygame.draw.rect(self.screen, self.okno_sound_color, self.okno_sound_rect)
            self.screen.blit(
                txt_sound_state,
                (
                    self.okno_sound_rect.centerx - txt_sound_state.get_width() // 2,
                    self.okno_sound_rect.centery - txt_sound_state.get_height() // 2,
                ),
            )

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.exit_button_rect.collidepoint(event.pos):
                            return True
                        elif self.language_button_rect.collidepoint(event.pos):
                            if self.settings["language"]["current"] == "ru":
                                change_language("en")
                            else:
                                change_language("ru")
                        elif self.reset_button_rect.collidepoint(event.pos):
                            if self.confirm(clock, fps) == True:
                                set_default_setings()
                        elif self.okno_sound_rect.collidepoint(event.pos):
                            if self.settings["sound"] == "off":
                                change_sound("on")
                            else:
                                change_sound("off")
                elif event.type == pygame.MOUSEMOTION:
                    self.cursor_over_button_exit = self.exit_button_rect.collidepoint(
                        event.pos
                    )
                    self.cursor_over_button_language = (
                        self.language_button_rect.collidepoint(event.pos)
                    )
                    self.cursot_over_button_reset = self.reset_button_rect.collidepoint(
                        event.pos
                    )
                    self.cursor_over_button_sound = self.okno_sound_rect.collidepoint(
                        event.pos
                    )

            self.exit_button_color = (
                (0, 255, 0) if self.cursor_over_button_exit else (255, 0, 0)
            )  # GREEN or RED
            self.language_button_color = (
                (0, 255, 0) if self.cursor_over_button_language else (255, 255, 0)
            )  # GREEN or YELLOW
            self.reset_button_color = GREEN if self.cursot_over_button_reset else YELLOW
            self.okno_sound_color = GREEN if self.cursor_over_button_sound else YELLOW

            pygame.display.update()
            clock.tick(fps)

    def confirm(self, clock, fps):
        okno = pygame.Surface((600, 300))
        okno.fill(CYAN)

        okno_yes_rect = pygame.Rect(730, 300, 200, 70)
        cursor_over_button_yes = False
        yes_button_color = RED

        okno_no_rect = pygame.Rect(990, 300, 200, 70)
        cursor_over_button_no = False
        no_button_color = RED

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if okno_yes_rect.collidepoint(event.pos):
                            return True
                        elif okno_no_rect.collidepoint(event.pos):
                            return False
                elif event.type == pygame.MOUSEMOTION:
                    if okno_yes_rect.collidepoint(event.pos):
                        cursor_over_button_yes = True
                    else:
                        cursor_over_button_yes = False
                    if okno_no_rect.collidepoint(event.pos):
                        cursor_over_button_no = True
                    else:
                        cursor_over_button_no = False

            if cursor_over_button_yes:
                yes_button_color = GREEN
            else:
                yes_button_color = RED
            if cursor_over_button_no:
                no_button_color = GREEN
            else:
                no_button_color = RED

            self.screen.blit(okno, (660, 100))
            pygame.draw.rect(self.screen, yes_button_color, okno_yes_rect)
            pygame.draw.rect(self.screen, no_button_color, okno_no_rect)
            # Вы уверены?
            txt_are_you_sure = self.font.render(
                self.settings["language"][self.settings["language"]["current"]][
                    "Are you sure?"
                ],
                True,
                BLACK,
            )
            txt_yes = self.font.render(
                self.settings["language"][self.settings["language"]["current"]]["Yes"],
                True,
                BLACK,
            )
            txt_no = self.font.render(
                self.settings["language"][self.settings["language"]["current"]]["No"],
                True,
                BLACK,
            )
            self.screen.blit(txt_are_you_sure, (800, 170))
            self.screen.blit(
                txt_yes,
                (
                    okno_yes_rect.centerx - txt_yes.get_width() // 2,
                    okno_yes_rect.centery - txt_yes.get_height() // 2,
                ),
            )
            self.screen.blit(
                txt_no,
                (
                    okno_no_rect.centerx - txt_no.get_width() // 2,
                    okno_no_rect.centery - txt_no.get_height() // 2,
                ),
            )
            pygame.display.update()
            clock.tick(fps)
