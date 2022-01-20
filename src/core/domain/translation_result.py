from core.domain.word import Word
from typing import List


class TranslationResult():
    def __init__(self, input_word: Word, output_words: List[Word]):
        self.input_word = input_word
        self.output_words = output_words

