import pygame as pg
from style import Style


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

WORD_DEF_TAB_WIDTH = WINDOW_WIDTH
WORD_DEF_TAB_HEIGHT = (WINDOW_HEIGHT / 4)
WORD_DEF_TAB_RECT = pg.Rect(0, 0, WORD_DEF_TAB_WIDTH, WORD_DEF_TAB_HEIGHT)

CONNECT_TAB_WIDTH = WINDOW_WIDTH
CONNECT_TAB_HEIGHT = (WINDOW_HEIGHT / 8)
CONNECT_TAB_RECT = pg.Rect(
    0, WINDOW_HEIGHT - CONNECT_TAB_HEIGHT,
    CONNECT_TAB_WIDTH, CONNECT_TAB_HEIGHT
)

COMMAND_TAB_WIDTH = WINDOW_WIDTH
COMMAND_TAB_HEIGHT = WINDOW_HEIGHT - WORD_DEF_TAB_HEIGHT - CONNECT_TAB_HEIGHT
COMMAND_TAB_RECT = pg.Rect(
    0, WORD_DEF_TAB_HEIGHT,
    COMMAND_TAB_WIDTH, COMMAND_TAB_HEIGHT
)

# Color definitions
WHITE = pg.Color(0xFF, 0xFF, 0xFF)
RED = pg.Color(0xFF, 0x00, 0x00)
GREEN = pg.Color(0x00, 0xFF, 0x00)
BLUE = pg.Color(0x00, 0x00, 0xFF)
BLACK = pg.Color(0x00, 0x00, 0x00)
LIGHT_GRAY = pg.Color(0xF0, 0xF0, 0xF0)
GRAY = pg.Color(0xE0, 0xE0, 0xE0)

# Styles
BUTTON_STYLE = Style(
    hover=LIGHT_GRAY,
    click=WHITE,
    normal=GRAY,

    fg=BLACK,
    outline=BLACK,
    outline_width=1
)
