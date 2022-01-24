from core.domain.word import Word
from core.domain.translation_result import TranslationResult
from typing import List, Optional
from adapter.translator.translator_adapter import TranslatorAdapter
from presenter.presenter import Presenter
from adapter.spellchecker.spell_checker import correct_word_spelling
from adapter.persister.data_persister import DataPersister


class TranslatorService():
    def __init__(self, translator_adapter: TranslatorAdapter, presenter: Presenter, storage: DataPersister):
        self.translator_adapter = translator_adapter
        self.presenter = presenter
        self.storage = storage
        self.input_languages = ["English"]
        self.output_languages = ["Georgian"]

    def translate_word(self, input_word: Word, target_languages: List[str], minimalistic=False) -> None:
        word, corrected_word = correct_word_spelling(input_word.word)
        if word != corrected_word:
            input_word.word = corrected_word
            self.presenter.present_text(f"### Spelling of: '{input_word.word}' is not correct. Autocorrecting it "
                                        f"to: '{corrected_word}' ###")
        try:
            if not input_word:
                return
            result: List[TranslationResult] = []
            for language in target_languages:
                if language.lower() == "georgian":
                    storage_result: Optional[Word] = self.storage.search(input_word, language)
                    if storage_result:
                        result.append(TranslationResult(input_word, [storage_result]))
                    else:
                        translator_result = self.translator_adapter.get_georgian_translations_of_word(input_word.word)
                        self.storage.put(input_word, translator_result.output_words[0])
                        result.append(translator_result)
            self.presenter.present_translations(result[0].input_word, result[0].output_words if not minimalistic else [result[0].output_words[0]])
        except:
            print('Encountered problem with translating input word')

    def get_possible_input_languages(self) -> List[str]:
        return self.input_languages

    def get_possible_output_languages(self) -> List[str]:
        return self.output_languages
