import pygame as pg
from dataclasses import dataclass


MB_LEFT = 1
MB_RIGHT = 2


@dataclass
class Inputs:
    mouse_pos: (int, int)
    mouse_just_pressed: (bool, bool)
    mouse_just_released: (bool, bool)
    mouse_state: (bool, bool)

    keys_just_pressed: set[int]
    modifiers: int

    text_editing: str
    text_input: str

    def contextualize(self, topleft: (int, int)):
        dup = self
        dup.mouse_pos = (
            self.mouse_pos[0] - topleft[0],
            self.mouse_pos[1] - topleft[1]
        )

        return dup


class EventLoop:
    def execute(self) -> Inputs | None:
        keys_just_pressed: set[int] = set()
        keys_just_released: set[int] = set()
        mouse_just_pressed = [False, False]
        mouse_just_released = [False, False]

        text_input = ""
        text_editing = ""

        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                return None

            if ev.type == pg.MOUSEBUTTONDOWN:
                if ev.button == MB_LEFT:
                    mouse_just_pressed[0] = True
                if ev.button == MB_RIGHT:
                    mouse_just_pressed[1] = True
            elif ev.type == pg.MOUSEBUTTONUP:
                if ev.button == MB_LEFT:
                    mouse_just_released[0] = True
                if ev.button == MB_RIGHT:
                    mouse_just_released[1] = True

            if ev.type == pg.KEYDOWN:
                keys_just_pressed.add(ev.key)
            elif ev.type == pg.KEYUP:
                keys_just_released.add(ev.key)

            if ev.type == pg.TEXTINPUT:
                text_input = ev.text
            if ev.type == pg.TEXTEDITING:
                text_editing = ev.text

        clicked_btns = pg.mouse.get_pressed()

        return Inputs(
            pg.mouse.get_pos(),
            tuple(mouse_just_pressed),
            tuple(mouse_just_released),
            (clicked_btns[MB_LEFT - 1], clicked_btns[MB_RIGHT - 1]),

            keys_just_pressed,
            pg.key.get_mods(),

            text_editing,
            text_input,
        )
