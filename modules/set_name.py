import pygame
from helper import BLACK, RED, ORANGE, GREEN, GRAY


class set_name:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.font = pygame.font.Font(None, 64)

    def input_name(self, settings, change_name, clock, fps):
        input_box = pygame.Rect(1920 / 2 - 200, 1080 / 2, 400, 64)
        enter_button_rect = pygame.Rect(1920 / 2 - 100, 1080 / 2 + 100, 200, 64)
        color_inactive = pygame.Color("lightskyblue3")
        color_active = pygame.Color("dodgerblue2")
        color = color_inactive
        active = False
        text = ""
        done = False
        cursor_over_button_enter = False
        enter_button_color = RED

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return done
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    color = color_active if active else color_inactive
                    if enter_button_rect.collidepoint(event.pos):
                        done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return True
                    if active:
                        if event.key == pygame.K_RETURN:
                            done = True
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        elif len(text) < 12:  # Проверка на максимальную длину имени
                            text += event.unicode
                elif event.type == pygame.MOUSEMOTION:
                    if enter_button_rect.collidepoint(event.pos):
                        cursor_over_button_enter = True
                    else:
                        cursor_over_button_enter = False

            self.screen.fill(GRAY)
            pygame.draw.rect(self.screen, color, input_box, 8)
            pygame.draw.rect(self.screen, enter_button_color, enter_button_rect)
            txt_surface = self.font.render(text, True, color)
            txt_set_name = self.font.render(
                settings["language"][settings["language"]["current"]]["Name_text"],
                True,
                ORANGE,
            )
            txt_enter = self.font.render("Enter", True, BLACK)
            width = max(400, txt_surface.get_width() + 10)
            input_box.w = width
            self.screen.blit(txt_set_name, (1920 / 2 - 250, 1080 / 2 - 100))
            self.screen.blit(txt_surface, (input_box.x + 10, input_box.y + 12))
            self.screen.blit(txt_enter, (1920 / 2 - 50, 1080 / 2 + 112))
            pygame.display.flip()

            if cursor_over_button_enter:
                enter_button_color = GREEN
            else:
                enter_button_color = RED
            clock.tick(fps)

        change_name(text)

        return done
