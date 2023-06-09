import msg as m
import input
import pygame as pg
import word
import copy
import events as ev


class VibrationQueue:
    to_send: list[str | float]
    time_start: float | None

    def __init__(self):
        self.to_send = []
        self.time_start = None

    def send_sentence(self, sentence: list[str | float]) -> bool:
        if not m.Messenger.is_connected():
            print("[vib queue] cannot send sentence, " +
                  "messenger is not connected.")
            return False

        word.word_list.compile_words()
        self.to_send = copy.deepcopy(sentence)
        input.event_loop.post_notif(ev.VIB_STARTED_SENDING, None)
        return True

    def cancel(self):
        self.to_send = copy.deepcopy([None])

    def update(self):
        if len(self.to_send) == 0:
            return

        if type(self.to_send[0]) == str:

            compiled_word = word.word_list.compiled_words[self.to_send[0]]
            word_total_time = sum(compiled_word)

            m.Messenger.emit_message({
                "pattern": compiled_word,
                "interval": 0
            })

            self.time_start = None
            self.to_send.pop(0)

            # Wait for the word to finish its vibration
            if len(self.to_send) != 0:
                self.to_send[0] += word_total_time * 0.001

        elif type(self.to_send[0]) == float:

            if self.time_start is None:
                self.time_start = pg.time.get_ticks()

            time_diff = pg.time.get_ticks() - self.time_start
            if time_diff * 0.001 > self.to_send[0]:
                self.to_send.pop(0)

        elif self.to_send[0] is None:
            self.to_send.pop(0)
            print("Yup")

        if len(self.to_send) == 0:
            input.event_loop.post_notif(
                ev.VIB_FINISHED_SENDING,
                None
            )


vib_queue: VibrationQueue = VibrationQueue()
