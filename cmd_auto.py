import consts as c
import pygame as pg
from cmd_common import CommandTabCommon
from button import Button
from input import Inputs
from input_dialog import InputDialog
import word
import events as ev
import vib_queue


class CommandTabAutomatic(CommandTabCommon):
    timeline_buttons: list[Button]
    currently_selected: str | None

    timeline_data: list[str | float]
    should_sync_timeline: bool

    play_button: Button

    def __init__(self):
        super().__init__("自动", lambda b: self.on_src_button_pressed(b))

        self.currently_selected = None

        self.play_button = Button(
            lambda b: self.on_play_button_pressed(b),
            c.PLAY_BUTTON_RECT,
            "开始", c.START_BUTTON_STYLE
        )

        self.timeline_buttons = []
        self.timeline_data = ["" if i % 2 == 0 else 0.0 for i in range(
            c.TIMELINE_N_ROWS * c.TIMELINE_ROW_N_SLOTS
        )]

        button_n = 0
        y = c.TIMELINE_START_POS[1]

        for _ in range(c.TIMELINE_N_ROWS):
            x = c.TIMELINE_START_POS[0]

            for _ in range(c.TIMELINE_ROW_N_SLOTS):
                style = None
                if button_n % 2 == 1:
                    style = c.TIMELINE_TIME_SLOT_STYLE
                else:
                    style = c.TIMELINE_EMPTY_STYLE

                self.timeline_buttons.append(Button(
                    self.timeline_button_callback(button_n),
                    pg.Rect((x, y), c.TIMELINE_SLOT_SIZE),
                    "", style
                ))

                x += c.TIMELINE_SLOT_SIZE[0]
                button_n += 1

            y += c.TIMELINE_SLOT_SIZE[1]

        self.should_sync_timeline = True

    def timeline_button_callback(self, button_n):
        if button_n % 2 == 0:
            return lambda b: self.on_assign_btn_pressed(b, button_n)
        else:
            return lambda b: self.on_set_wait_btn_pressed(b, button_n)

    def on_assign_btn_pressed(self, btn: Button, n: int):
        if self.currently_selected is None:
            return

        if self.timeline_data[n] == self.currently_selected:
            self.timeline_data[n] = ""
        else:
            self.timeline_data[n] = self.currently_selected

        self.should_sync_timeline = True

    def on_set_wait_btn_pressed(self, btn: Button, n: int):
        wait_time = InputDialog("请输入停顿的时间：").evaluate()

        try:
            wait_time = round(float(wait_time), 2)
            if wait_time > 60.0:
                raise ValueError

        except ValueError:
            wait_time = float(self.timeline_data[n])

        self.should_sync_timeline = True

        for i in range(len(self.timeline_data)):
            if i % 2 == 1:
                self.timeline_data[i] = wait_time

    def on_src_button_pressed(self, b: Button):
        for i in self.src_buttons:
            if i.text == self.currently_selected:
                i.update_style(c.TIMELINE_WORD_STYLE)

        self.currently_selected = b.text
        b.update_style(c.SRC_SELECTED_STYLE)

    def on_play_button_pressed(self, b: Button):
        if b.text == "取消":
            vib_queue.vib_queue.cancel()
            b.update_style(c.START_BUTTON_STYLE)
            return

        if vib_queue.vib_queue.send_sentence(self.timeline_data):
            b.update_style(c.CANCEL_BUTTON_STYLE)
            self.play_button.update_text("取消")

    def render(self) -> pg.Surface:
        self.screen.fill(c.COMMAND_AUTO_FOREGROUND)
        self.screen.fill(
            c.COMMAND_AUTO_BACKGROUND,
            rect=pg.Rect((0, 0), c.COMMAND_TAB_RECT.size).inflate(0, -2)
        )
        surf = super().render()

        for b in self.timeline_buttons:
            b.render(self.screen)

        self.play_button.render(self.screen)

        self.draw_preview()
        self.draw_preview_lines()

        return surf

    def draw_preview(self):
        pg.draw.rect(self.screen, c.COMMAND_AUTO_FOREGROUND, pg.Rect(
            (c.PREVIEW_GRID_START_POS[0] - c.PREVIEW_GRID_BORDER_WIDTH,
             c.PREVIEW_GRID_START_POS[1] - c.PREVIEW_GRID_BORDER_WIDTH),

            (c.PREVIEW_GRID_TOTAL_WIDTH + 2 * c.PREVIEW_GRID_BORDER_WIDTH,
             2 * c.PREVIEW_GRID_SLOT_HEIGHT + 3 * c.PREVIEW_GRID_BORDER_WIDTH)
        ))

        preview_pos = [
            c.PREVIEW_GRID_START_POS[0],
            c.PREVIEW_GRID_START_POS[1]
        ]

        preview_slots = int(c.TIMELINE_ROW_N_SLOTS / 2)

        for row in range(c.TIMELINE_N_ROWS):
            preview_pos[0] = c.PREVIEW_GRID_START_POS[0]

            for col in range(preview_slots):
                n = row * c.TIMELINE_ROW_N_SLOTS + col * 2

                pg.draw.rect(self.screen, c.SLOT_NONE_STYLE.normal, pg.Rect(
                    (preview_pos[0], preview_pos[1]),
                    (c.PREVIEW_GRID_SLOT_WIDTH, c.PREVIEW_GRID_SLOT_HEIGHT)
                ))

                subslot_width = c.PREVIEW_GRID_SLOT_WIDTH / c.N_SLOTS_PER_WORD

                if word.word_list.word_exists(self.timeline_data[n]):
                    w = word.word_list.find_word(self.timeline_data[n])
                    for (off, enabled) in enumerate(w.vibs):
                        if enabled:
                            shift = subslot_width * off
                            pg.draw.rect(
                                self.screen,
                                c.SLOT_VIB_STYLE.normal,
                                pg.Rect(
                                    (preview_pos[0] + shift, preview_pos[1]),
                                    (subslot_width, c.PREVIEW_GRID_SLOT_HEIGHT)
                                )
                            )

                block_color = c.TIMELINE_TIME_SLOT_STYLE.normal
                slot_width = c.PREVIEW_GRID_SLOT_WIDTH
                pg.draw.rect(self.screen, block_color, pg.Rect(
                    (preview_pos[0] + slot_width, preview_pos[1]),
                    (c.PREVIEW_GRID_TIME_SEP_WIDTH, c.PREVIEW_GRID_SLOT_HEIGHT)
                ))

                preview_pos[0] += c.PREVIEW_GRID_SLOT_WIDTH
                preview_pos[0] += c.PREVIEW_GRID_TIME_SEP_WIDTH

            preview_pos[1] += (c.PREVIEW_GRID_SLOT_HEIGHT +
                               c.PREVIEW_GRID_BORDER_WIDTH)

    def draw_preview_lines(self):
        # Draw the preview
        ln_start = list(c.PREVIEW_GRID_START_POS)
        for col in range(int(c.TIMELINE_ROW_N_SLOTS / 2)):
            x = ln_start[0] + (c.PREVIEW_GRID_SLOT_WIDTH +
                               c.PREVIEW_GRID_TIME_SEP_WIDTH) * col

            for subcol in range(c.N_SLOTS_PER_WORD):
                x += c.PREVIEW_GRID_SLOT_WIDTH / c.N_SLOTS_PER_WORD
                pg.draw.line(
                    self.screen,
                    c.COMMAND_AUTO_FOREGROUND,
                    (x, ln_start[1]),
                    (x, ln_start[1] + 2 * c.PREVIEW_GRID_SLOT_HEIGHT
                                    + c.PREVIEW_GRID_BORDER_WIDTH)
                )

    def update(self, i: Inputs):
        super().update(i)
        for b in self.timeline_buttons:
            b.update(i)

        self.play_button.update(i)

    def sync(self, i: Inputs):
        if self.should_sync_timeline:
            for (index, v) in enumerate(self.timeline_data):
                self.timeline_buttons[index].update_text(str(v))

                if type(v) == float:
                    continue

                if str(v) == "":
                    self.timeline_buttons[index].update_style(
                        c.TIMELINE_EMPTY_STYLE
                    )
                else:
                    self.timeline_buttons[index].update_style(
                        c.TIMELINE_WORD_STYLE
                    )

        super().sync(i)

        if ev.VIB_RENAMED in i.notifs:
            for rn in i.notifs[ev.VIB_RENAMED]:
                if self.currently_selected == rn["from"]:
                    self.currently_selected = rn["to"]

                for idx in range(0, len(self.timeline_data)):
                    if self.timeline_data[idx] == rn["from"]:
                        self.timeline_data[idx] = rn["to"]
                        self.should_sync_timeline = True

        if ev.VIB_STARTED_SENDING in i.notifs:
            # for b in self.src_buttons:
            #     b.enabled = False
            for b in self.timeline_buttons:
                b.enabled = False
            self.switch_button.enabled = False

        if ev.VIB_FINISHED_SENDING in i.notifs:
            # for b in self.src_buttons:
            #     b.enabled = True
            for b in self.timeline_buttons:
                b.enabled = True
            self.switch_button.enabled = True
            self.play_button.update_text("开始")
            self.play_button.update_style(c.START_BUTTON_STYLE)
