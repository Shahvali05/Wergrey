import pygame
from helper import BLACK, settings


class Dialog_box:
    def __init__(self, screen, name: str, icon, lines, lines_count: int) -> None:
        self.screen = screen
        self.box = pygame.image.load("images/bar_chat.png").convert_alpha()
        self.font = pygame.font.Font(None, 32)
        self.txt_name = name
        self.lines_count = lines_count
        self.lines = lines
        self.icon = pygame.image.load(icon).convert_alpha()

    def run(self, clock, fps):

        num = 7
        running = True
        while running:
            x = 410
            y = 110
            self.screen.blit(self.box, (110, 80))
            self.screen.blit(self.icon, (120, 96))
            for i in range(num - 7, num):
                if i < self.lines_count:
                    text = self.font.render(
                        "%s"
                        % (self.lines["%s" % (i)]).replace("ffff", settings["name"]),
                        True,
                        BLACK,
                    )
                    self.screen.blit(text, (x, y))
                    y += 40
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if num >= self.lines_count:
                            return True
                        num += 7
            txt_name = self.font.render(self.txt_name, True, BLACK)
            self.screen.blit(txt_name, (140, 383))
            pygame.display.update(110, 80, 1700, 350)
            clock.tick(fps)
