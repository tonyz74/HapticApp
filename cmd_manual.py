import consts as c
import pygame as pg
from button import Button
import vib_queue
import events as ev
from input import Inputs
from cmd_common import CommandTabCommon


class CommandTabManual(CommandTabCommon):
    def __init__(self):
        super().__init__("实时", lambda b: self.on_src_button_pressed(b))

    def on_src_button_pressed(self, b: Button):
        vib_queue.vib_queue.send_sentence([b.text, 0])

    def sync(self, i: Inputs):
        super().sync(i)

        if ev.VIB_STARTED_SENDING in i.notifs:
            for b in self.src_buttons:
                b.enabled = False
            self.switch_button.enabled = False

        if ev.VIB_FINISHED_SENDING in i.notifs:
            for b in self.src_buttons:
                b.enabled = True
            self.switch_button.enabled = True

    def render(self) -> pg.Surface:
        self.screen.fill(c.BLUE)
        surf = super().render()

        return surf
