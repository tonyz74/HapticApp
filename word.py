import consts as c
import events as ev
import input
import copy


class Word:
    name: str
    vibs: list[bool]

    def __init__(self, name: str):
        self.name = name
        self.vibs = [False for _ in range(c.N_SLOTS_PER_WORD)]


class WordList:
    words: list[Word]
    compiled_words: dict[str, list[int]]

    def __init__(self):
        self.words = []
        self.compiled_words = {"": [0, c.SLOT_TIME_MS * c.N_SLOTS_PER_WORD]}
        for i in range(c.N_WORDS):
            self.words.append(Word(str(i + 1)))

    def word_exists(self, name: str):
        for i in self.words:
            if i.name == name:
                return True

    def rename_word(self, old: str, new_name: str):
        if not self.word_exists(old):
            raise NameError(f"Word name {old} doesn't exist!")

        input.event_loop.post_notif(ev.VIB_RENAMED, {
            "from": copy.deepcopy(old),
            "to": copy.deepcopy(new_name)
        })

        for i in self.words:
            if i.name == old:
                i.name = new_name

    def find_word(self, name: str) -> Word | None:
        for i in self.words:
            if i.name == name:
                return i
        return None

    def compile_words(self):
        for w in self.words:
            pattern = []
            contiguous = 0
            prev = None

            if w.vibs[0] is False:
                pattern.append(0)

            for v in w.vibs:
                if prev is None or v == prev:
                    contiguous += 1
                else:
                    pattern.append(contiguous * c.SLOT_TIME_MS)
                    contiguous = 1
                prev = v

            pattern.append(contiguous * c.SLOT_TIME_MS)

            self.compiled_words[w.name] = pattern

        print(self.compiled_words)


word_list: WordList = WordList()
