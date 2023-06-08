import consts as c
import pygame as pg


class CommandTab:

    screen: pg.Surface

    def __init__(self):
        self.screen = pg.Surface(c.COMMAND_TAB_RECT.size)

    def render(self) -> pg.Surface:
        self.screen.fill(c.RED)
        return self.screen
