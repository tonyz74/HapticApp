import consts as c
import pygame as pg
from button import Button
from input import Inputs
import msg


class ConnectTab:
    screen: pg.Surface
    connect_button: Button

    def __init__(self):
        self.screen = pg.Surface(c.CONNECT_TAB_RECT.size)

        connect_rect = pg.Rect(
            c.CONNECT_TAB_WIDTH / 2 - 60,
            c.CONNECT_TAB_HEIGHT / 2 - 30,
            120, 60
        )
        self.connect_button = Button(
            lambda btn: self.on_connect_clicked(btn),
            connect_rect, "链接Server", c.BUTTON_STYLE
        )

    def render(self) -> pg.Surface:
        self.screen.fill(c.GREEN)
        self.connect_button.render(self.screen)
        return self.screen

    def update(self, i: Inputs):
        self.connect_button.update(i)

    def on_connect_clicked(self, btn):
        try:
            msg.Messenger.init()
        except Exception:
            print("Failed to connect!")
