import consts as c
import pygame as pg
from input import Inputs
from typing import Any

from cmd_auto import CommandTabAutomatic
from cmd_manual import CommandTabManual


class CommandTab:

    screen: pg.Surface
    mode_is_manual: bool

    auto: CommandTabAutomatic
    manual: CommandTabManual

    current: Any

    def __init__(self):
        self.screen = pg.Surface(c.COMMAND_TAB_RECT.size)

        self.auto = CommandTabAutomatic()
        self.manual = CommandTabManual()

        self.mode_is_manual = True
        self.current = self.manual

    def render(self) -> pg.Surface:
        surf = self.current.render()
        self.screen.blit(surf, (0, 0))
        return self.screen

    def update(self, i: Inputs):
        self.current.update(i)

        if self.current.switch_requested:
            self.current.switch_requested = False
            self.mode_is_manual = not self.mode_is_manual

            if self.mode_is_manual:
                self.current = self.manual
            else:
                self.current = self.auto
