from core.domain.word import Word
from typing import List

class Presenter():
    def __init__(self):
        pass

    def present_text(self, text, prompt=True) -> None:
        pass

    def present_list_of_texts(self, texts: List[str]) -> None:
        pass

    def present_translations(self, input_word: Word, translations: List[Word]) -> None:
        pass

    def get_input_from_client(self, data: str) -> str:
        pass
