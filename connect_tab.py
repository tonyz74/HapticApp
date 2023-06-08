import consts as c
import pygame as pg


class ConnectTab:

    screen: pg.Surface

    def __init__(self):
        self.screen = pg.Surface(c.CONNECT_TAB_RECT.size)

    def render(self) -> pg.Surface:
        self.screen.fill(c.GREEN)
        return self.screen
