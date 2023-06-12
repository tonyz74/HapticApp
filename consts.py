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

# Logical Constants

N_WORDS = 4
N_SLOTS_PER_WORD = 10
SLOT_TIME_MS = 200

TIMELINE_N_ROWS = 2
TIMELINE_ROW_N_SLOTS = 8

# Sizes

WINDOW_WIDTH = 680
WINDOW_HEIGHT = 720

WORD_DEF_TAB_WIDTH = WINDOW_WIDTH
WORD_DEF_TAB_HEIGHT = (WINDOW_HEIGHT / 4)
WORD_DEF_TAB_RECT = pg.Rect(0, 0, WORD_DEF_TAB_WIDTH, WORD_DEF_TAB_HEIGHT)

WORD_DEF_TAB_WORDLIST_RECT = pg.Rect(
    WORD_DEF_TAB_WIDTH - 200, 0,
    WORD_DEF_TAB_WIDTH, WORD_DEF_TAB_HEIGHT
)

WORDLIST_WORD_BUTTON_SIZE = (85, 40)

NAME_LABEL_RECT = pg.Rect(20, 20, 120, 40)

NAME_CHANGE_BUTTON_RECT = pg.Rect(20 + 120 + 20, 20, 260, 40)

SLOT_STARTING_POS = (20, 80)
SLOT_SIZE = (40, 80)

TIMELINE_SLOT_SIZE = (80, 40)
TIMELINE_START_POS = (20, 120)


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

MODE_SWITCH_BUTTON_RECT = pg.Rect(
    (COMMAND_TAB_WIDTH - 100, 20),
    (80, 40)
)

PLAY_BUTTON_RECT = MODE_SWITCH_BUTTON_RECT.move(
    (-100, 0)
)

INPUT_DIALOG_WIDTH = WINDOW_WIDTH - 120
INPUT_DIALOG_HEIGHT = WINDOW_HEIGHT - 600
INPUT_DIALOG_RECT = pg.Rect(
    60, 300, INPUT_DIALOG_WIDTH, INPUT_DIALOG_HEIGHT
)

INPUT_DIALOG_TITLEBAR_WIDTH = INPUT_DIALOG_WIDTH
INPUT_DIALOG_TITLEBAR_HEIGHT = 35
INPUT_DIALOG_TITLEBAR_RECT = pg.Rect(
    INPUT_DIALOG_RECT.left,
    INPUT_DIALOG_RECT.top - INPUT_DIALOG_TITLEBAR_HEIGHT,
    INPUT_DIALOG_TITLEBAR_WIDTH,
    INPUT_DIALOG_TITLEBAR_HEIGHT
)

INPUT_DIALOG_TEXT_INPUT_RECT = (INPUT_DIALOG_RECT
                                .inflate(-60, 0)
                                .move(0, 10)
                                .scale_by(1.0, 0.4))


PREVIEW_GRID_START_POS = (20, 240)
PREVIEW_GRID_TOTAL_WIDTH = 640
PREVIEW_GRID_TIME_SEP_WIDTH = 10
PREVIEW_GRID_SLOT_WIDTH = int(
    PREVIEW_GRID_TOTAL_WIDTH / (TIMELINE_ROW_N_SLOTS / 2)
) - PREVIEW_GRID_TIME_SEP_WIDTH
PREVIEW_GRID_BORDER_WIDTH = 1
PREVIEW_GRID_SLOT_HEIGHT = 80

CONNECT_BUTTON_RECT = pg.Rect(
    CONNECT_TAB_WIDTH / 2 - 60,
    CONNECT_TAB_HEIGHT / 2 - 30,
    120, 60
)


# Color definitions
WHITE = pg.Color(0xFF, 0xFF, 0xFF)
GREEN = pg.Color(0x00, 0xFF, 0x00)
BLUE = pg.Color(0x00, 0x00, 0xFF)
BLACK = pg.Color(0x00, 0x00, 0x00)
LIGHT_GRAY = pg.Color(0xF0, 0xF0, 0xF0)
GRAY = pg.Color(0xE0, 0xE0, 0xE0)

RED = pg.Color(0xFF, 0x40, 0x40)
LIGHT_RED = pg.Color(0xFF, 0x60, 0x60)
LIGHTER_RED = pg.Color(0xFF, 0x70, 0x70)
DARK_RED = pg.Color(0xCD, 0x4F, 0x44)

LIGHT_GREEN = pg.Color(0x65, 0xDB, 0x79)
LIGHTER_GREEN = pg.Color(0x89, 0xDF, 0x9E)

SLIGHTLY_DARK_GRAY = pg.Color(0x70, 0x70, 0x70)
SLIGHTLY_DARKER_GRAY = pg.Color(0x50, 0x50, 0x50)
DARK_GRAY = pg.Color(0x20, 0x20, 0x20)
DARKER_GRAY = pg.Color(0x10, 0x10, 0x10)

# Styles

COMMAND_AUTO_BACKGROUND = LIGHT_GRAY
COMMAND_AUTO_FOREGROUND = BLACK

COMMAND_MANUAL_BACKGROUND = LIGHT_GRAY
COMMAND_MANUAL_FOREGROUND = BLACK

CONNECT_BACKGROUND = LIGHT_GRAY
CONNECT_FOREGROUND = BLACK

INPUT_DIALOG_BACKGROUND = WHITE
INPUT_DIALOG_FOREGROUND = BLACK

INPUT_DIALOG_TITLEBAR_BACKGROUND = GRAY
INPUT_DIALOG_TITLEBAR_FOREGROUND = BLACK

WORD_DEF_BACKGROUND = GRAY
WORD_DEF_FOREGROUND = BLACK
WORDLIST_BACKGROUND = LIGHT_GRAY

PREVIEW_GRID_OUTLINE_COLOR = BLACK

BUTTON_STYLE = Style(
    hover=LIGHT_GRAY,
    click=WHITE,
    normal=GRAY,

    disabled_click=BLACK,
    disabled_hover=BLACK,
    disabled_normal=BLACK,

    fg=BLACK,
    outline=BLACK,
    outline_width=1
)

CLOSE_BUTTON_STYLE = Style(
    hover=LIGHTER_RED,
    click=LIGHTER_RED,
    normal=LIGHT_RED,

    disabled_click=BLACK,
    disabled_hover=BLACK,
    disabled_normal=BLACK,

    fg=BLACK,
    outline=BLACK,
    outline_width=1
)

WORDLIST_BUTTON_STYLE = Style(
    normal=pg.Color(0xf6, 0xc8, 0x54),
    hover=pg.Color(0xf7, 0xce, 0x67),
    click=pg.Color(0xf8, 0xd4, 0x7a),

    #dcae3b
    disabled_normal=pg.Color(0xdc, 0xae, 0x3b),
    disabled_hover=pg.Color(0xdc, 0xae, 0x3b),
    disabled_click=pg.Color(0xdc, 0xae, 0x3b),

    fg=BLACK,
    outline=BLACK,
    outline_width=1
)

TEXT_INPUT_STYLE = Style(
    hover=WHITE,
    click=WHITE,
    normal=WHITE,

    disabled_click=LIGHT_GRAY,
    disabled_hover=LIGHT_GRAY,
    disabled_normal=LIGHT_GRAY,

    fg=BLACK,
    outline=BLACK,
    outline_width=1
)

SLOT_NONE_STYLE = Style(
    hover=LIGHT_GRAY,
    click=LIGHT_GRAY,
    normal=GRAY,

    disabled_click=GRAY,
    disabled_hover=GRAY,
    disabled_normal=GRAY,

    fg=BLACK,
    outline=BLACK,
    outline_width=1
)

SLOT_VIB_STYLE = Style(
    normal=pg.Color(0xf6, 0xc8, 0x54),
    hover=pg.Color(0xf7, 0xce, 0x67),
    click=pg.Color(0xf8, 0xd4, 0x7a),

    disabled_normal=pg.Color(0xdc, 0xae, 0x3b),
    disabled_hover=pg.Color(0xdc, 0xae, 0x3b),
    disabled_click=pg.Color(0xdc, 0xae, 0x3b),
    # disabled_normal=(0x80, 0x80, 0x80),
    # disabled_hover=(0x80, 0x80, 0x80),
    # disabled_click=(0x80, 0x80, 0x80),

    fg=BLACK,
    outline=BLACK,
    outline_width=1
)

SRC_SELECTED_STYLE = Style(
    normal=pg.Color(0xb7, 0xdb, 0xf4),
    hover=pg.Color(0xc3, 0xe1, 0xf6),
    click=pg.Color(0xc3, 0xe1, 0xf6),

    disabled_click=BLACK,
    disabled_hover=BLACK,
    disabled_normal=BLACK,

    fg=BLACK,
    outline=BLACK,
    outline_width=1
)

TIMELINE_EMPTY_STYLE = Style(
    hover=pg.Color(0x54, 0x82, 0xf6),
    click=pg.Color(0x67, 0x90, 0xf7),
    normal=pg.Color(0x42, 0x75, 0xf5),

    disabled_click=pg.Color(0x43, 0x68, 0xc4),
    disabled_hover=pg.Color(0x43, 0x68, 0xc4),
    disabled_normal=pg.Color(0x43, 0x68, 0xc4),

    fg=BLACK,
    outline=BLACK,
    outline_width=1
)

TIMELINE_WORD_STYLE = Style(
    normal=pg.Color(0x88, 0xc4, 0xed),
    hover=pg.Color(0x93, 0xc9, 0xee),
    click=pg.Color(0x9f, 0xcf, 0xf0),

    disabled_click=pg.Color(0x7a, 0xb0, 0xd5),
    disabled_hover=pg.Color(0x7a, 0xb0, 0xd5),
    disabled_normal=pg.Color(0x7a, 0xb0, 0xd5),

    fg=BLACK,
    outline=BLACK,
    outline_width=1
)

TIMELINE_TIME_SLOT_STYLE = Style(
    normal=pg.Color(0x27, 0x46, 0x93),
    hover=pg.Color(0x2e, 0x51, 0xab),
    click=pg.Color(0x34, 0x5d, 0xc4),

    disabled_click=pg.Color(0x1f, 0x38, 0x75),
    disabled_hover=pg.Color(0x1f, 0x38, 0x75),
    disabled_normal=pg.Color(0x1f, 0x38, 0x75),

    fg=WHITE,
    outline=BLACK,
    outline_width=1
)

COMMAND_SWITCH_MODE_BUTTON_STYLE = Style(
    hover=SLIGHTLY_DARK_GRAY,
    click=SLIGHTLY_DARK_GRAY,
    normal=SLIGHTLY_DARKER_GRAY,

    disabled_click=pg.Color(0x30, 0x30, 0x30),
    disabled_hover=pg.Color(0x30, 0x30, 0x30),
    disabled_normal=pg.Color(0x30, 0x30, 0x30),

    fg=WHITE,
    outline=BLACK,
    outline_width=1
)

NAME_LABEL_STYLE = Style(
    hover=WHITE,
    click=WHITE,
    normal=WHITE,

    disabled_normal=LIGHT_GRAY,
    disabled_hover=LIGHT_GRAY,
    disabled_click=LIGHT_GRAY,

    fg=BLACK,
    outline=BLACK,
    outline_width=1
)

START_BUTTON_STYLE = Style(
    hover=LIGHTER_GREEN,
    click=LIGHTER_GREEN,
    normal=LIGHT_GREEN,

    disabled_normal=BLACK,
    disabled_click=BLACK,
    disabled_hover=BLACK,

    fg=BLACK,
    outline=BLACK,
    outline_width=1
)

CANCEL_BUTTON_STYLE = Style(
    hover=LIGHT_RED,
    click=LIGHT_RED,
    normal=RED,

    disabled_normal=BLACK,
    disabled_click=BLACK,
    disabled_hover=BLACK,

    fg=BLACK,
    outline=BLACK,
    outline_width=1
)
