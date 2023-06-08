import consts as c
import pygame as pg
from button import Button
from input import Inputs
from input_dialog import InputDialog
import word
from copy import deepcopy


class WordDefinitionTab:

    screen: pg.Surface
    word_buttons: list[Button]

    current_word: str
    word_changed: bool

    name_label: Button
    name_change_button: Button

    vib_buttons: list[Button]

    def __init__(self):
        self.current_word = word.word_list.words[0].name
        self.word_changed = True
        self.screen = pg.Surface(c.WORD_DEF_TAB_RECT.size)

        BTN_WIDTH, BTN_HEIGHT = c.WORDLIST_WORD_BUTTON_SIZE

        self.word_buttons = []
        offsets = [
            (10, 20),
            (10 + BTN_WIDTH + 10, 20),
            (10, 20 + BTN_HEIGHT + 10),
            (10 + BTN_WIDTH + 10, 20 + BTN_HEIGHT + 10)
        ]

        # Create word list choice buttons

        base_rect = pg.Rect(
            c.WORD_DEF_TAB_WORDLIST_RECT.topleft,
            c.WORDLIST_WORD_BUTTON_SIZE
        )

        for (off, w) in zip(offsets, word.word_list.words):
            self.word_buttons.append(Button(
                lambda b: self.on_word_button_pressed(b),
                base_rect.move(off),
                w.name, c.WORDLIST_BUTTON_STYLE
            ))

        # Create name-setting buttons

        self.name_label = Button(
            None, c.NAME_LABEL_RECT,
            "动作名字", c.WORDLIST_BUTTON_STYLE
        )

        self.name_change_button = Button(
            lambda b: self.on_rename_button_pressed(b),
            c.NAME_CHANGE_BUTTON_RECT,
            "", c.TEXT_INPUT_STYLE
        )

        # Create vibration buttons

        self.vib_buttons = []
        vib_offset = c.SLOT_STARTING_POS

        for i in range(c.N_SLOTS_PER_WORD):
            self.vib_buttons.append(Button(
                self.binder(i),
                pg.Rect(vib_offset, c.SLOT_SIZE),
                "", c.SLOT_NONE_STYLE
            ))
            vib_offset = (
                vib_offset[0] + c.SLOT_SIZE[0],
                vib_offset[1]
            )

    def binder(self, i: int):
        return lambda b: self.on_vib_button_pressed(b, i)

    def on_word_button_pressed(self, btn: Button):
        self.current_word = btn.text
        self.word_changed = True
        print("Current:", self.current_word)

    def render(self) -> pg.Surface:
        self.screen.fill(c.GRAY)
        self.screen.fill(c.LIGHT_GRAY, c.WORD_DEF_TAB_WORDLIST_RECT)

        for i in self.word_buttons:
            i.render(self.screen)

        for i in self.vib_buttons:
            i.render(self.screen)

        self.name_label.render(self.screen)
        self.name_change_button.render(self.screen)

        return self.screen

    def update(self, i: Inputs):
        for b in self.word_buttons:
            b.update(i)

        for b in self.vib_buttons:
            b.update(i)

        self.name_label.update(i)
        self.name_change_button.update(i)

        if self.word_changed:
            self.word_changed = False
            self.sync_with_wordlist()

        if pg.K_ESCAPE in i.keys_just_pressed:
            for i in word.word_list.words:
                print(f"Word {i.name}: {i.vibs}")

    def sync_with_wordlist(self):
        self.name_change_button.update_text(self.current_word)

        current_vibs = word.word_list.find_word(self.current_word).vibs
        for i, on in enumerate(current_vibs):
            style = c.SLOT_VIB_STYLE
            if not on:
                style = c.SLOT_NONE_STYLE
            self.vib_buttons[i].update_style(style)

    def on_rename_button_pressed(self, btn: Button):
        res = InputDialog("请输入动作名字：").evaluate()

        for i in self.word_buttons:
            if i.text == self.current_word:
                i.update_text(res)

        word.word_list.rename_word(self.current_word, res)
        self.current_word = res
        self.word_changed = True

    def on_vib_button_pressed(self, btn: Button, index: int):
        word_vibs = word.word_list.find_word(self.current_word).vibs
        word_vibs[index] = not word_vibs[index]

        new_style = c.SLOT_NONE_STYLE
        if word_vibs[index]:
            new_style = c.SLOT_VIB_STYLE
        btn.update_style(new_style)
