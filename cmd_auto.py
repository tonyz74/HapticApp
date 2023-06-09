import consts as c
import pygame as pg
from cmd_common import CommandTabCommon
from button import Button
from input import Inputs
from input_dialog import InputDialog


class CommandTabAutomatic(CommandTabCommon):
    timeline_buttons: list[Button]
    currently_selected: str | None

    timeline_data: list[str | float]
    should_sync_timeline: bool

    def __init__(self):
        super().__init__("自动", lambda b: self.on_src_button_pressed(b))

        self.currently_selected = None

        self.timeline_buttons = []
        self.timeline_data = ["" if i % 2 == 0 else 0.0 for i in range(
            c.TIMELINE_N_ROWS * c.TIMELINE_ROW_N_SLOTS
        )]

        button_n = 0
        y = c.TIMELINE_START_POS[1]

        for _ in range(c.TIMELINE_N_ROWS):
            x = c.TIMELINE_START_POS[0]

            for _ in range(c.TIMELINE_ROW_N_SLOTS):
                self.timeline_buttons.append(Button(
                    self.timeline_button_callback(button_n),
                    pg.Rect((x, y), c.TIMELINE_SLOT_SIZE),
                    "", c.SLOT_NONE_STYLE
                ))

                x += c.TIMELINE_SLOT_SIZE[0]
                button_n += 1

            y += c.TIMELINE_SLOT_SIZE[1]

        self.should_sync_timeline = True

    def timeline_button_callback(self, button_n):
        if button_n % 2 == 0:
            return lambda b: self.on_assign_btn_pressed(b, button_n)
        else:
            return lambda b: self.on_set_wait_btn_pressed(b, button_n)

    def on_assign_btn_pressed(self, btn: Button, n: int):
        if self.currently_selected is None:
            return

        self.timeline_data[n] = self.currently_selected
        self.should_sync_timeline = True

    def on_set_wait_btn_pressed(self, btn: Button, n: int):
        wait_time = InputDialog("请输入停顿的时间：").evaluate()

        try:
            wait_time = round(float(wait_time), 2)
            if wait_time > 60.0:
                raise ValueError

        except ValueError:
            wait_time = float(self.timeline_data[n])

        self.should_sync_timeline = True
        self.timeline_data[n] = wait_time

    def on_src_button_pressed(self, b: Button):
        for i in self.src_buttons:
            if i.text == self.currently_selected:
                i.update_style(c.WORDLIST_BUTTON_STYLE)

        self.currently_selected = b.text
        b.update_style(c.SLOT_NONE_STYLE)

    def render(self) -> pg.Surface:
        self.screen.fill(c.RED)
        surf = super().render()

        for b in self.timeline_buttons:
            b.render(self.screen)

        return surf

    def update(self, i: Inputs):
        super().update(i)
        for b in self.timeline_buttons:
            b.update(i)

    def sync(self, i: Inputs):
        if self.should_sync_timeline:
            for (index, v) in enumerate(self.timeline_data):
                self.timeline_buttons[index].update_text(str(v))

        super().sync(i)

        if "word_renamed" in i.notifs:
            for rn in i.notifs["word_renamed"]:
                if self.currently_selected == rn["from"]:
                    self.currently_selected = rn["to"]

                for idx in range(0, len(self.timeline_data)):
                    if self.timeline_data[idx] == rn["from"]:
                        self.timeline_data[idx] = rn["to"]
                        self.should_sync_timeline = True
