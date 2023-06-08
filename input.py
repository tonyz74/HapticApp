import pygame as pg
from dataclasses import dataclass


@dataclass
class Inputs:
    mouse_pos: (int, int)
    mouse_just_pressed: (bool, bool)
    mouse_just_released: (bool, bool)
    mouse_state: (bool, bool)
    pressed_keys: set[int]
    modifiers: int

    def contextualize(self, topleft: (int, int)):
        dup = self
        dup.mouse_pos = (
            self.mouse_pos[0] - topleft[0],
            self.mouse_pos[1] - topleft[1]
        )

        return dup


class EventLoop:
    def execute(self) -> Inputs | None:
        pressed_keys = {}
        mouse_just_pressed = [False, False]
        mouse_just_released = [False, False]

        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                return None

            if ev.type == pg.MOUSEBUTTONDOWN:
                if ev.button == 1:
                    mouse_just_pressed[0] = True
                if ev.button == 2:
                    mouse_just_pressed[1] = True

            if ev.type == pg.MOUSEBUTTONUP:
                if ev.button == 1:
                    mouse_just_released[0] = True
                if ev.button == 2:
                    mouse_just_released[1] = True

        pressed_btns = pg.mouse.get_pressed()

        return Inputs(
            pg.mouse.get_pos(),
            tuple(mouse_just_pressed),
            tuple(mouse_just_released),
            # 0 is left, 2 is right
            (pressed_btns[0], pressed_btns[2]),
            pressed_keys,
            0
        )
