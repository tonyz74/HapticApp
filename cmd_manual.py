import pygame as pg
from button import Button
from input import Inputs
import consts as c


class CommandTabManual:

    screen: pg.Surface
    switch_button: Button
    switch_requested: bool

    def __init__(self):
        self.screen = pg.Surface(c.COMMAND_TAB_RECT.size)

        self.switch_requested = False
        self.switch_button = Button(
            lambda b: self.on_switch_button_pressed(b),
            c.MODE_SWITCH_BUTTON_RECT,
            "实时", c.WORDLIST_BUTTON_STYLE
        )

    def render(self):
        self.screen.fill(c.RED)

        self.switch_button.render(self.screen)

        return self.screen

    def on_switch_button_pressed(self, btn: Button):
        self.switch_requested = True

    def update(self, i: Inputs):
        self.switch_button.update(i)
