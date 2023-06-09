import pygame as pg
from dataclasses import dataclass


@dataclass
class Style:
    hover: pg.Color
    click: pg.Color
    normal: pg.Color

    disabled_hover: pg.Color
    disabled_click: pg.Color
    disabled_normal: pg.Color

    fg: pg.Color

    outline: pg.Color
    outline_width: int
