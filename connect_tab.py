import consts as c
import pygame as pg
from button import Button
from input import Inputs
import msg
import events as ev
from image_dialog import ImageDialog


class ConnectTab:
    screen: pg.Surface
    connect_button: Button
    qr_button: Button

    def __init__(self):
        self.screen = pg.Surface(c.CONNECT_TAB_RECT.size)

        connect_rect = c.CONNECT_BUTTON_RECT
        self.connect_button = Button(
            lambda btn: self.on_connect_clicked(btn),
            connect_rect, "链接", c.BUTTON_STYLE
        )

        self.qr_button = Button(
            lambda btn: self.on_qr_clicked(btn),
            c.CONNECT_BUTTON_RECT.move(-200, 0),
            "扫描QR码", c.BUTTON_STYLE
        )

    def render(self) -> pg.Surface:
        self.screen.fill(c.CONNECT_BACKGROUND)
        self.connect_button.render(self.screen)
        self.qr_button.render(self.screen)
        return self.screen

    def update(self, i: Inputs):
        self.connect_button.update(i)
        self.qr_button.update(i)

        self.sync(i)

    def sync(self, i: Inputs):
        if ev.MESSENGER_DISCONNECTED in i.notifs:
            self.connect_button.update_text("链接")
            self.connect_button.update_style(c.BUTTON_STYLE)

        if ev.MESSENGER_CONNECTED in i.notifs:
            self.connect_button.update_text("已链接")
            self.connect_button.update_style(c.START_BUTTON_STYLE)

    def on_qr_clicked(self, btn):
        import qr
        if self.connect_button.text == "已链接":
            qr.make_qr_to_path("qrcode.png")
            gen_qr = pg.image.load("qrcode.png")
            ImageDialog(gen_qr, "请扫描!").evaluate()

    def on_connect_clicked(self, btn):

        if msg.Messenger.is_connected():
            return

        try:
            msg.Messenger.init()
        except Exception:
            # just let them click it again
            pass
