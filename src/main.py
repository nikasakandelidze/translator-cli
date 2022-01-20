from presenter.presenter import Presenter
from adapter.translator_adapter import TranslatorAdapter
from core.service.translate_service import TranslatorService


def interactive_translate(presenter: Presenter, translator_service: TranslatorService):
    presenter.present_text("Here are all the possible input languages: ")
    input_langs = translator_service.get_possible_input_languages()
    presenter.present_list_of_texts(input_langs)
    output_langs = translator_service.get_possible_output_languages()
    presenter.present_list_of_texts(output_langs)
    

def init():
    presenter = Presenter()
    translator_adapter = TranslatorAdapter()
    translator_service = TranslatorService(translator_adapter, presenter)
    presenter.present_text("Welcome to Translate like a Hacker!")
    while True:
        res = presenter.get_input_from_client("> ")
        if res.lower() == "exit":
            break
        if res.lower() == "translate":
            interactive_translate(presenter, translator_service)
    presenter.present_text("Good bye ;)")


if __name__ == '__main__':
    init()
