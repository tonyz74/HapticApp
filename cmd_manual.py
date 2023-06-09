import consts as c
import pygame as pg
from cmd_common import CommandTabCommon


class CommandTabManual(CommandTabCommon):
    def __init__(self):
        super().__init__("实时", None)

    def render(self) -> pg.Surface:
        self.screen.fill(c.BLUE)
        surf = super().render()

        return surf
