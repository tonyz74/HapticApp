import pygame as pg
import consts as c

from connect_tab import ConnectTab
from command_tab import CommandTab
from word_def_tab import WordDefinitionTab


class HapticApp:
    screen: pg.Surface
    clock: pg.time.Clock

    word_def_tab: WordDefinitionTab
    connect_tab: ConnectTab
    command_tab: CommandTab

    running: bool

    def __init__(self):
        pg.init()
        pg.font.init()

        win_size = (c.WINDOW_WIDTH, c.WINDOW_HEIGHT)
        self.screen = pg.display.set_mode(win_size)
        pg.display.set_caption("触觉反馈")

        self.clock = pg.time.Clock()

        self.running = True

        self.word_def_tab = WordDefinitionTab()
        self.connect_tab = ConnectTab()
        self.command_tab = CommandTab()

    def mainloop(self):
        self.running = True

        while self.running:
            for ev in pg.event.get():
                if ev.type == pg.QUIT:
                    self.running = False

            self.screen.fill(c.WHITE)

            # Render
            self.render()

            pg.display.flip()
            self.clock.tick(30)

    def render(self):
        word_def = self.word_def_tab.render()
        connect = self.connect_tab.render()
        command = self.command_tab.render()

        self.screen.blit(word_def, c.WORD_DEF_TAB_RECT)
        self.screen.blit(connect, c.CONNECT_TAB_RECT)
        self.screen.blit(command, c.COMMAND_TAB_RECT)


if __name__ == "__main__":
    HapticApp().mainloop()
