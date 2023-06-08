import consts as c
import pygame as pg


class WordDefinitionTab:

    screen: pg.Surface

    def __init__(self):
        self.screen = pg.Surface(c.WORD_DEF_TAB_RECT.size)

    def render(self) -> pg.Surface:
        self.screen.fill(c.BLUE)
        return self.screen
