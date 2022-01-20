from adapter.web_adapter import WebTranslatorAdapter
from core.domain.translation_result import TranslationResult


class TranslatorAdapter():
    def __init__(self):
        pass

    def get_georgian_translations_of_word(self, word) -> TranslationResult:
        pass


class TranslatorAdapterFactory():
    @staticmethod
    def get_translator() -> TranslatorAdapter:
        return WebTranslatorAdapter()
