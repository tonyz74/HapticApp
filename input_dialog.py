import consts as c
import pygame as pg
from input import EventLoop, Inputs
from button import Button


class InputDialog:
    event_loop: EventLoop
    running: bool

    result_str: str
    edit_buffer: str
    text_updated: bool

    cursor_index: int
    cursor_int: int

    text_surf: pg.Surface
    prompt_surf: pg.Surface

    def get_text_preview(self) -> str:
        return self.result_str + self.edit_buffer

    def __init__(self, prompt: str):
        self.clock = pg.time.Clock()
        self.screen = pg.display.get_surface()
        self.event_loop = EventLoop()
        self.running = True

        self.result_str = ""
        self.edit_buffer = ""

        self.text_updated = True
        self.cursor_index = 0
        self.cursor_pos = 0

        self.close_button = Button(
            lambda b: self.close_pressed(b),
            pg.Rect(
                c.INPUT_DIALOG_TITLEBAR_RECT.left,
                c.INPUT_DIALOG_TITLEBAR_RECT.top,
                c.INPUT_DIALOG_TITLEBAR_HEIGHT + 30 - 1,
                c.INPUT_DIALOG_TITLEBAR_HEIGHT - 1
            ),
            "取消",
            c.CLOSE_BUTTON_STYLE
        )

        self.prompt_surf = c.FONTS.mid.render(
            prompt, True, c.INPUT_DIALOG_FOREGROUND)

    def close_pressed(self, btn: Button):
        self.running = False
        self.result_str = None

    def evaluate(self) -> str | None:
        self.screen.fill(
            (0x30, 0x30, 0x30),
            special_flags=pg.BLEND_SUB
        )

        while self.running:
            input = self.event_loop.execute()
            if input is None:
                exit(0)

            self.render()
            self.update(input)

            pg.display.flip()
            self.clock.tick(30)

        if self.result_str is None:
            return ""
        return self.result_str

    def render(self):
        self.screen.fill(
            c.INPUT_DIALOG_FOREGROUND,
            rect=c.INPUT_DIALOG_TITLEBAR_RECT.inflate(2, 2)
        )
        self.screen.fill(
            c.INPUT_DIALOG_TITLEBAR_BACKGROUND,
            rect=c.INPUT_DIALOG_TITLEBAR_RECT
        )

        self.screen.fill(
            c.INPUT_DIALOG_FOREGROUND,
            rect=c.INPUT_DIALOG_RECT.inflate(2, 2)
        )
        self.screen.fill(
            c.INPUT_DIALOG_BACKGROUND,
            rect=c.INPUT_DIALOG_RECT
        )

        text_pos = c.INPUT_DIALOG_RECT.topleft
        text_pos = (text_pos[0] + 12, text_pos[1] + 6)
        self.screen.blit(self.prompt_surf, text_pos)

        self.close_button.render(self.screen)

        pg.draw.rect(
            self.screen, c.INPUT_DIALOG_FOREGROUND,
            c.INPUT_DIALOG_TEXT_INPUT_RECT,
            width=1
        )

        if self.text_updated:
            preview = self.get_text_preview()
            self.text_surf = c.FONTS.mid.render(
                preview, True, c.INPUT_DIALOG_FOREGROUND
            )
            self.cursor_pos = c.FONTS.mid.size(
                preview[:self.cursor_index]
            )[0]

        text_blit_pos = (c.INPUT_DIALOG_TEXT_INPUT_RECT
                         .move(0, c.INPUT_DIALOG_TEXT_INPUT_RECT.height / 2)
                         .move(10, -self.text_surf.get_size()[1] / 2))

        self.screen.blit(self.text_surf, text_blit_pos)

        start_point = (
            text_blit_pos.x + self.cursor_pos + 1,
            text_blit_pos.y + self.text_surf.get_size()[1] / 2
        )
        pg.draw.line(
            self.screen, c.INPUT_DIALOG_FOREGROUND,
            (start_point[0], start_point[1] - 12),
            (start_point[0], start_point[1] + 12),
        )
        pass

    def update(self, i: Inputs):
        self.close_button.update(i)

        if self.result_str is None:
            return

        if pg.K_RETURN in i.keys_just_pressed:
            self.running = False
            return

        if i.text_editing != "":
            diff = len(i.text_editing) - len(self.edit_buffer)
            self.cursor_index += diff
            self.edit_buffer = i.text_editing
            self.text_updated = True
        else:
            if pg.K_BACKSPACE in i.keys_just_pressed:
                self.cursor_index -= 1
                if len(self.edit_buffer) == 1:
                    self.edit_buffer = ""
                else:
                    self.result_str = self.result_str[:-1]
                    self.text_updated = True

        if i.text_input:
            self.result_str += i.text_input
            self.edit_buffer = ""
            self.text_updated = True
            self.cursor_index += len(i.text_input)
