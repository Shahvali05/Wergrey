import pygame


class Door:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.anim_door = [
            pygame.image.load(f"images/door/door_{i}.png").convert_alpha()
            for i in range(1, 6)
        ]
        self.chet = 0
        self.anim_start = False

    def draw(self, x, y):
        if self.anim_start:
            self.screen.blit(self.anim_door[self.chet // 5], (x, y))
            if self.chet >= 24:
                self.chet = 0
                self.anim_start = False
                return True
            else:
                self.chet += 1
        else:
            self.screen.blit(self.anim_door[0], (x, y))

    def check_door_open(self, player_x, player_y, door_x, door_y):
        if (
            player_y >= door_y
            and player_x < door_x + 90
            and player_x > door_x - 90
            and self.anim_start == False
        ):
            return True
        else:
            return False
