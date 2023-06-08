import pygame as pg
from dataclasses import dataclass


@dataclass
class Style:
    hover: pg.Color
    click: pg.Color
    normal: pg.Color

    fg: pg.Color

    outline: pg.Color
    outline_width: int
