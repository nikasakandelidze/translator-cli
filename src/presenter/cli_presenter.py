from typing import List

from core.domain.word import Word
from presenter.presenter import Presenter


class CliPresenter(Presenter):
    def __init__(self):
        super().__init__()

    def present_text(self, text, prompt=True):
        print(f"{'>' if prompt else ''} {text}")

    def present_translations(self, input_word: Word, translations: List[Word]):
        number_of_translations = len(translations)
        print("")
        print(f"> Found {number_of_translations} translations in {translations[0].language} for input word: {input_word.word}.")
        print(" ")
        print("######## Results ########")
        for index, word in enumerate(translations):
            print(f"> {index+1}) {word.word}")
        print("> ")
        print("######## Results ########")

    def get_input_from_client(self, data: str) -> str:
        return input(f"> {data}")

    def present_list_of_texts(self, texts: List[str]) -> None:
        for text in texts:
            self.present_text(f"  - {text}", False)