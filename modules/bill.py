import pygame


class Bill:
    def __init__(self, screen) -> None:
        self.bill_png = pygame.image.load(
            "images/grandfather_stand.png"
        ).convert_alpha()
        self.bill_x = 100
        self.bill_y = 720
        self.screen = screen

    def draw_bill(self):
        self.screen.blit(self.bill_png, (self.bill_x, self.bill_y))

    def dialog_bill(self, player_x, player_y):
        if (
            player_y == self.bill_y
            and player_x < self.bill_x + 90
            and player_x > self.bill_x - 90
        ):
            return True
