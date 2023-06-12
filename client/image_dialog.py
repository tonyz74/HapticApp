import pygame as pg
import input
from input import Inputs
from button import Button
import consts as c


DIALOG_OFF = 40


class ImageDialog:
    img: pg.Surface
    screen: pg.Surface
    close_button: Button
    running: bool
    clock: pg.time.Clock

    prompt_surf: pg.Surface
    titlebar_rect: pg.Rect
    window_rect: pg.Rect

    def __init__(self, img: pg.Surface, prompt: str):
        self.prompt_surf = c.FONTS.mid.render(prompt, True, c.BLACK)

        self.img = img
        self.clock = pg.time.Clock()
        self.screen = pg.display.get_surface()
        self.running = True

        img_size = self.img.get_size()

        self.titlebar_rect = pg.Rect(
            c.WINDOW_WIDTH // 2 - img_size[0] // 2 - 20,
            c.WINDOW_HEIGHT // 2 - img_size[1] // 2 - 110,
            img_size[0] + 40, 30
        )

        self.window_rect = pg.Rect(
            c.WINDOW_WIDTH // 2 - img_size[0] // 2 - 20,
            c.WINDOW_HEIGHT // 2 - img_size[1] // 2 - 80,
            img_size[0] + 40,
            img_size[1] + 100
        )

        self.close_button = Button(
            lambda b: self.close_button_pressed(b), pg.Rect(
                self.titlebar_rect.left,
                self.titlebar_rect.top,
                80, 29
            ),
            "取消", c.CLOSE_BUTTON_STYLE
        )

    def evaluate(self):
        self.screen.fill(
            (0x30, 0x30, 0x30),
            special_flags=pg.BLEND_SUB
        )

        while self.running:
            i = input.event_loop.execute()
            if i is None:
                exit(0)

            self.render()
            self.update(i)

            pg.display.flip()
            self.clock.tick(30)

    def close_button_pressed(self, b: Button):
        self.running = False

    def render(self):
        img_size = self.img.get_size()

        pg.draw.rect(
            self.screen,
            c.INPUT_DIALOG_TITLEBAR_BACKGROUND,
            self.titlebar_rect,
        )
        pg.draw.rect(
            self.screen,
            c.INPUT_DIALOG_TITLEBAR_FOREGROUND,
            self.titlebar_rect.inflate(2, 2),
            width=1
        )

        self.screen.fill(c.INPUT_DIALOG_FOREGROUND, self.window_rect.inflate(2, 2))
        self.screen.fill(c.INPUT_DIALOG_BACKGROUND, self.window_rect)

        self.close_button.render(self.screen)

        self.screen.blit(self.prompt_surf, self.window_rect.move(20, 20).topleft)

        self.screen.blit(self.img, (
            c.WINDOW_WIDTH // 2 - img_size[0] // 2,
            c.WINDOW_HEIGHT // 2 - img_size[1] // 2
        ))

    def update(self, i: Inputs):
        self.close_button.update(i)
