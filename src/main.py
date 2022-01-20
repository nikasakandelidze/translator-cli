from presenter.presenter import Presenter
from presenter.Presenter_factory import PresenterFactory
from adapter.translator_adapter_factory import TranslatorAdapterFactory
from core.service.translate_service import TranslatorService
from core.domain.word import Word

def interactive_translate(presenter: Presenter, translator_service: TranslatorService):
    presenter.present_text("Here are all the possible input languages: ")
    input_langs = translator_service.get_possible_input_languages()
    presenter.present_list_of_texts(input_langs)
    input_language = presenter.get_input_from_client("Input language choice: ")
    presenter.present_text("Here are all the possible input languages: ")
    output_langs = translator_service.get_possible_output_languages()
    presenter.present_list_of_texts(output_langs)
    output_language = presenter.get_input_from_client("Output language choice: ")
    word = presenter.get_input_from_client(f"Type word in {input_language} to translate to {output_language}: ")
    translator_service.translate_word(Word(word, input_language), [output_language])

def init():
    presenter = PresenterFactory.get_presenter()
    translator_adapter = TranslatorAdapterFactory.get_translator()
    translator_service = TranslatorService(translator_adapter, presenter)
    presenter.present_text("Welcome to Translate like a Hacker!")
    while True:
        res = presenter.get_input_from_client("")
        if res.lower() == "exit":
            break
        if res.lower() == "translate":
            interactive_translate(presenter, translator_service)
    presenter.present_text("Good bye ;)")


if __name__ == '__main__':
    init()
