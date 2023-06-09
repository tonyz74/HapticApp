import pygame as pg
from button import Button
from input import Inputs
import consts as c
import word


class CommandTabCommon:

    screen: pg.Surface
    switch_button: Button
    switch_requested: bool

    src_buttons: list[Button]

    def __init__(self, btn_text: str, callback):
        self.screen = pg.Surface(c.COMMAND_TAB_RECT.size)

        self.switch_requested = False
        self.switch_button = Button(
            lambda b: self.on_switch_button_pressed(b),
            c.MODE_SWITCH_BUTTON_RECT,
            btn_text, c.WORDLIST_BUTTON_STYLE
        )

        src_start = (20, 20)
        self.src_buttons = []

        for w in word.word_list.words:
            self.src_buttons.append(Button(
                callback, pg.Rect(src_start, c.WORDLIST_WORD_BUTTON_SIZE),
                w.name, c.WORDLIST_BUTTON_STYLE
            ))
            src_start = (
                src_start[0] + 10 + c.WORDLIST_WORD_BUTTON_SIZE[0],
                src_start[1]
            )

    def render(self):
        self.switch_button.render(self.screen)

        for i in self.src_buttons:
            i.render(self.screen)

        return self.screen

    def on_switch_button_pressed(self, btn: Button):
        self.switch_requested = True

    def update(self, i: Inputs):
        self.switch_button.update(i)

        for b in self.src_buttons:
            b.update(i)

    def sync(self, i: Inputs):
        if "word_renamed" in i.notifs:
            for rn in i.notifs["word_renamed"]:
                for b in self.src_buttons:
                    if b.text == rn["from"]:
                        b.update_text(rn["to"])
