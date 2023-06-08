import pygame as pg


class FontMap:
    small: pg.font.Font
    mid: pg.font.Font
    large: pg.font.Font
    heading: pg.font.Font

    def __init__(self):
        pg.font.init()
        tc_sans = "asset/TencentSans-W7.ttf"
        self.small = pg.font.Font(tc_sans, 12)
        self.mid = pg.font.Font(tc_sans, 20)
        self.large = pg.font.Font(tc_sans, 28)
        self.heading = pg.font.Font(tc_sans, 36)


FONTS = FontMap()

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 720

# Color definitions
WHITE = pg.Color(0xFF, 0xFF, 0xFF)
RED = pg.Color(0xFF, 0x00, 0x00)
GREEN = pg.Color(0x00, 0xFF, 0x00)
BLUE = pg.Color(0x00, 0x00, 0xFF)
