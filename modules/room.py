import pygame
from modules.pause import pause
from modules.dialog_box import Dialog_box
from modules.bill import Bill
from modules.character import Character
from modules.door import Door
from helper import settings
from helper import glava_1


class Room:
    def __init__(self):
        self.home_png = pygame.image.load("images/home.png").convert_alpha()
        self.character = Character()

    def run(self, screen, fps, clock):
        running = True
        door = Door(screen)

        while running:
            self.screen = screen
            self.screen.blit(self.home_png, (0, 0))
            self.screen.blit(self.home_png, (1920, 0))
            if door.draw(1500, 671) == True:
                return "street"
            Bill(self.screen).draw_bill()

            keys = pygame.key.get_pressed()
            self.character.draw_player(screen, keys, True, 10, 1780)

            if keys[pygame.K_ESCAPE]:
                if pause(self.screen, clock, fps) == False:
                    return True
            elif (
                keys[pygame.K_f]
                and not self.character.is_jump
                and Bill(self.screen).dialog_bill(
                    self.character.player_x, self.character.player_y
                )
            ):
                if (
                    Dialog_box(
                        self.screen,
                        settings["language"][settings["language"]["current"]][
                            "Grandfather"
                        ],
                        "images/grandfather_icon.png",
                        glava_1["grandfather"]["acquaintance"][
                            settings["language"]["current"]
                        ],
                        6,
                    ).run(clock, fps)
                    == False
                ):
                    return False
            elif (
                keys[pygame.K_f]
                and not self.character.is_jump
                and door.check_door_open(
                    self.character.player_x, self.character.player_y, 1500, 671
                )
            ):
                door.anim_start = True
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return False
            clock.tick(fps)
