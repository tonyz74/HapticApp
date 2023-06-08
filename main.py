import pygame as pg
import consts as c

from connect_tab import ConnectTab
from command_tab import CommandTab
from word_def_tab import WordDefinitionTab

from input import EventLoop, Inputs


class HapticApp:
    screen: pg.Surface
    clock: pg.time.Clock

    word_def_tab: WordDefinitionTab
    connect_tab: ConnectTab
    command_tab: CommandTab

    event_loop: EventLoop

    running: bool

    def __init__(self):
        pg.init()
        pg.font.init()
        pg.key.set_repeat(500, 50)

        win_size = (c.WINDOW_WIDTH, c.WINDOW_HEIGHT)
        self.screen = pg.display.set_mode(win_size)
        pg.display.set_caption("触觉反馈")

        self.clock = pg.time.Clock()

        self.running = True

        self.word_def_tab = WordDefinitionTab()
        self.connect_tab = ConnectTab()
        self.command_tab = CommandTab()

        self.event_loop = EventLoop()

    def mainloop(self):
        self.running = True

        while self.running:
            inputs = self.event_loop.execute()
            if inputs is None:
                self.running = False
                break

            self.screen.fill(c.WHITE)

            self.render()
            self.update(inputs)

            pg.display.flip()
            self.clock.tick(30)

    def render(self):
        word_def = self.word_def_tab.render()
        connect = self.connect_tab.render()
        command = self.command_tab.render()

        self.screen.blit(word_def, c.WORD_DEF_TAB_RECT)
        self.screen.blit(connect, c.CONNECT_TAB_RECT)
        self.screen.blit(command, c.COMMAND_TAB_RECT)

    def update(self, inputs):

        connect_inputs = inputs.contextualize(c.CONNECT_TAB_RECT.topleft)
        self.connect_tab.update(connect_inputs)


if __name__ == "__main__":
    HapticApp().mainloop()
