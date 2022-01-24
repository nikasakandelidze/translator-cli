from typing import List
import requests
import json
from core.domain.word import Word
from adapter.translator.translator_adapter import TranslatorAdapter
from core.domain.translation_result import TranslationResult

BASE_URL_OF_RESOURCE = 'https://translate.ge/api/{route}'


class WebTranslatorAdapter(TranslatorAdapter):
    def __init__(self):
        super().__init__()

    def get_georgian_translations_of_word(self, word: str) -> TranslationResult:
        translate_url = BASE_URL_OF_RESOURCE.format(route=f"{word}")
        response = requests.get(translate_url)
        dictionary = json.loads(response.text)
        output_words: List[Word] = []
        language = 'Georgian'
        for word in dictionary['rows']:
            translated_word_data = word['value']
            context = translated_word_data['Word']
            word = translated_word_data['Text']
            output_words.append(Word(word.replace('\n', ' ') , language, context))
        input_word = Word(word,  "English")
        return TranslationResult(input_word, output_words)