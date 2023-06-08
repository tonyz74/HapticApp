import pygame as pg
import consts as c


class HapticApp:
    screen: pg.Surface
    clock: pg.time.Clock

    running: bool

    def __init__(self):
        pg.init()
        pg.font.init()

        win_size = (c.WINDOW_WIDTH, c.WINDOW_HEIGHT)
        self.screen = pg.display.set_mode(win_size)
        pg.display.set_caption("触觉反馈")

        self.clock = pg.time.Clock()

    def mainloop(self):
        self.running = True

        while self.running:
            for ev in pg.event.get():
                if ev.type == pg.QUIT:
                    self.running = False

            self.screen.fill(c.WHITE)

            # Render

            pg.display.flip()
            self.clock.tick(30)

    def render():
        pass


if __name__ == "__main__":
    HapticApp().mainloop()
