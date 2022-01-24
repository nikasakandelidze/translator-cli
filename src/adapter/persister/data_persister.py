from typing import Optional

from core.domain.word import Word


class DataPersister():
    def __init__(self):
        pass

    def put(self, input_word: Word, output_word: Word) -> None:
        pass

    def search(self, search_word: Word, output_language: str) -> Optional[Word]:
        pass
