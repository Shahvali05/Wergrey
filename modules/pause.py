import pygame
import sys
from helper import BLACK, RED, GREEN, MAGENTA, settings, change_sound


def pause(screen, clock, fps):
    font = pygame.font.Font("fonts/SAIBA-45-Regular-(v1.1).otf", 36)
    okno = pygame.Surface((1200, 600))
    okno.fill(MAGENTA)

    okno_continue_rect = pygame.Rect(460, 300, 1000, 100)
    okno_continue_color = RED

    okno_sound_rect = pygame.Rect(460, 430, 1000, 100)
    okno_sound_colot = RED

    okno_quit_rect = pygame.Rect(460, 560, 1000, 100)
    okno_quit_color = RED

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if okno_continue_rect.collidepoint(event.pos):
                        return True
                    elif okno_sound_rect.collidepoint(event.pos):
                        if settings["sound"] == "off":
                            change_sound("on")
                        else:
                            change_sound("off")
                    elif okno_quit_rect.collidepoint(event.pos):
                        return False
            elif event.type == pygame.MOUSEMOTION:
                if okno_continue_rect.collidepoint(event.pos):
                    okno_continue_color = GREEN
                else:
                    okno_continue_color = RED
                if okno_sound_rect.collidepoint(event.pos):
                    okno_sound_colot = GREEN
                else:
                    okno_sound_colot = RED
                if okno_quit_rect.collidepoint(event.pos):
                    okno_quit_color = GREEN
                else:
                    okno_quit_color = RED

        txt_pause = font.render(
            settings["language"][settings["language"]["current"]]["Pause"],
            True,
            BLACK,
        )
        txt_continue = font.render(
            settings["language"][settings["language"]["current"]]["Continue"],
            True,
            BLACK,
        )
        txt_sound = font.render(
            settings["language"][settings["language"]["current"]]["Sound"],
            True,
            BLACK,
        )
        txt_sound_state = font.render(
            settings["language"][settings["language"]["current"]][settings["sound"]],
            True,
            BLACK,
        )
        txt_quit = font.render(
            settings["language"][settings["language"]["current"]]["Quit"], True, BLACK
        )

        screen.blit(okno, (360, 100))
        pygame.draw.rect(screen, okno_continue_color, okno_continue_rect)
        pygame.draw.rect(screen, okno_sound_colot, okno_sound_rect)
        pygame.draw.rect(screen, okno_quit_color, okno_quit_rect)

        screen.blit(
            txt_pause, (okno_continue_rect.centerx - txt_pause.get_width() // 2, 170)
        )
        screen.blit(
            txt_continue,
            (475, okno_continue_rect.centery - txt_continue.get_height() // 2),
        )
        screen.blit(
            txt_sound, (475, okno_sound_rect.centery - txt_sound.get_height() // 2)
        )
        screen.blit(
            txt_sound_state,
            (1300, okno_sound_rect.centery - txt_sound_state.get_height() // 2),
        )
        screen.blit(
            txt_quit, (475, okno_quit_rect.centery - txt_quit.get_height() // 2)
        )

        pygame.display.update()
        clock.tick(fps)
