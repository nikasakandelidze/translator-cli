from core.domain.word import Word
from core.domain.translation_result import TranslationResult
from typing import List
from adapter.translator_adapter import TranslatorAdapter
from presenter.presenter import Presenter


class TranslatorService():
    def __init__(self, translator_adapter: TranslatorAdapter, presenter: Presenter):
        self.translator_adapter = translator_adapter
        self.presenter = presenter
        self.input_languages = ["English"]
        self.output_languages = ["Georgian"]

    def translate_word(self, input_word: Word, target_languages:List[str]) -> None:
        if not input_word:
            return
        result: List[TranslationResult] = []
        for language in target_languages:
            if language.lower() == "georgian":
                result.append(self.translator_adapter.get_georgian_translations_of_word(input_word.word))
        self.presenter.present_translations(result[0].input_word, result[0].output_words)

    def get_possible_input_languages(self) -> List[str]:
        return self.input_languages

    def get_possible_output_languages(self) -> List[str]:
        return self.output_languages