import consts as c
import pygame as pg
from typing import Callable, Any

from style import Style
from input import Inputs


class Button:
    cb: Callable[[Any], Any] | None

    text: str
    text_surf: pg.Surface

    rect: pg.Rect
    style: Style

    state: str
    color: pg.Color
    disabled: bool

    def __init__(
        self,
        cb: Callable[[Any], Any] | None,
        rect: pg.Rect,
        text: str,
        style: Style
    ):
        self.cb = cb
        self.rect = rect
        self.text = text
        self.style = style

        self.state = "NORMAL"

        self.update_style(self.style)
        self.update_text(self.text)

        self.disabled = False

    def update_text(self, text: str):
        self.text = text
        self.text_surf = c.FONTS.mid.render(text, True, self.style.fg)

    def update_style(self, style: Style):
        self.style = style
        # Todo lmao

    def render(self, target: pg.Surface):
        # Judge color based on state
        bg = None
        if self.state == "HOVER":
            bg = self.style.hover
        elif self.state == "CLICK":
            bg = self.style.click
        elif self.state == "NORMAL":
            bg = self.style.normal

        pg.draw.rect(target, bg, self.rect)

        rect_mid = self.rect.center
        mid = (
            rect_mid[0] - self.text_surf.get_size()[0] / 2,
            rect_mid[1] - self.text_surf.get_size()[1] / 2
        )

        target.blit(self.text_surf, mid)

    def update(self, inputs: Inputs):
        execute = False

        if self.rect.collidepoint(inputs.mouse_pos):
            if inputs.mouse_state[0]:
                self.state = "CLICK"
            else:
                self.state = "HOVER"

            if inputs.mouse_just_released[0]:
                execute = True
        else:
            self.state = "NORMAL"

        if execute and self.cb is not None:
            self.cb(self)
