import consts as c

class Word:
    name: str
    vibs: list[bool]

    def __init__(self, name: str):
        self.name = name
        self.vibs = [False for _ in range(c.N_SLOTS_PER_WORD)]


class WordList:
    words: list[Word]

    def __init__(self):
        self.words = []
        for i in range(c.N_WORDS):
            self.words.append(Word(str(i + 1)))

    def word_exists(self, name: str):
        for i in self.words:
            if i.name == name:
                return True

    def rename_word(self, old: str, new_name: str):
        if not self.word_exists(old):
            raise NameError(f"Word name {old} doesn't exist!")

        for i in self.words:
            if i.name == old:
                i.name = new_name

    def find_word(self, name: str) -> Word | None:
        for i in self.words:
            if i.name == name:
                return i
        return None


word_list: WordList = WordList()
