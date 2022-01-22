from adapter.translator.translator_adapter import TranslatorAdapter
from adapter.translator.web_adapter import WebTranslatorAdapter


class TranslatorAdapterFactory():
    @staticmethod
    def get_translator() -> TranslatorAdapter:
        return WebTranslatorAdapter()
