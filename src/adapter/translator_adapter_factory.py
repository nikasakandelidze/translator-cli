from adapter.translator_adapter import TranslatorAdapter
from adapter.web_adapter import WebTranslatorAdapter


class TranslatorAdapterFactory():
    @staticmethod
    def get_translator() -> TranslatorAdapter:
        return WebTranslatorAdapter()
