import pygame
from helper import RED


class Character:
    def __init__(self):
        self.font = pygame.font.Font(None, 64)
        self.work_left = [
            pygame.image.load(f"images/Shah/Shah_togo_l_{i}.png").convert_alpha()
            for i in range(1, 5)
        ]
        self.work_right = [
            pygame.image.load(f"images/Shah/Shah_togo_r_{i}.png").convert_alpha()
            for i in range(1, 5)
        ]
        self.player_r = pygame.image.load(
            "images/Shah/Shah_stand_r.png"
        ).convert_alpha()
        self.player_l = pygame.image.load(
            "images/Shah/Shah_stand_l.png"
        ).convert_alpha()
        self.player_anim_count = 0
        self.player_speed = 5
        self.player_x = 150
        self.player_y = 720
        self.pos_player = "r"
        self.jump_count = 10
        self.is_jump = False
        self.anim = False
        self.step = False
        self.time_jamp = 20
        self.max_hp = 100
        self.hp = 100

    def move_left(self):
        self.player_x -= self.player_speed
        self.pos_player = "l"

    def move_right(self):
        self.player_x += self.player_speed
        self.pos_player = "r"

    def jump(self):
        if self.jump_count >= -10:
            if self.jump_count > 0:
                self.player_y -= (self.jump_count**2) / 2
            else:
                self.player_y += (self.jump_count**2) / 2
            self.jump_count -= 1
        else:
            self.jump_count = 10
            self.is_jump = False
            self.step = not self.step

    def draw_player(self, screen, keys, control, map_x_l, map_x_r):
        text_hp = self.font.render(
            "%s hp" % (int(100 / self.max_hp * self.hp)), True, RED
        )
        self.anim = False
        if (
            (keys[pygame.K_LEFT] or keys[pygame.K_a])
            and self.player_x > map_x_l
            and control
        ):
            self.move_left()
            self.anim = True
        elif (
            (keys[pygame.K_RIGHT] or keys[pygame.K_d])
            and self.player_x < map_x_r
            and control
        ):
            self.move_right()
            self.anim = True
        if not self.is_jump:
            if keys[pygame.K_SPACE] and self.time_jamp == 0:
                self.is_jump = True
                self.time_jamp = 20
            if self.time_jamp > 0:
                self.time_jamp -= 1
        else:
            if control:
                self.jump()

        screen.blit(text_hp, (1770, 30))

        if self.anim:
            if self.is_jump:
                if self.step:
                    self.player_anim_count = 4
                else:
                    self.player_anim_count = 24
            (
                screen.blit(
                    self.work_left[self.player_anim_count // 10],
                    (self.player_x, self.player_y),
                )
                if self.pos_player == "l"
                else screen.blit(
                    self.work_right[self.player_anim_count // 10],
                    (self.player_x, self.player_y),
                )
            )
            if self.player_anim_count == 39:
                self.player_anim_count = 0
            else:
                self.player_anim_count += 1
        else:
            self.player_anim_count = 0
            screen.blit(
                (self.player_l if self.pos_player == "l" else self.player_r),
                (self.player_x, self.player_y),
            )
