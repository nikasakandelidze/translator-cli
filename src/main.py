from presenter.presenter import Presenter
from presenter.presenter_factory import PresenterFactory
from adapter.translator.translator_adapter_factory import TranslatorAdapterFactory
from adapter.persister.data_persister_factory import DataPersisterFactory
from core.service.translate_service import TranslatorService
from core.domain.word import Word
from sys import argv

COMMANDS = [("translate","Interactive translation in the terminal."), ("help","Help command for detailed descriptions of all available commands and etc.")]


def interactive_translate(presenter: Presenter, translator_service: TranslatorService):
    presenter.present_text("Here are all the possible input languages: ")
    input_langs = translator_service.get_possible_input_languages()
    presenter.present_list_of_texts(input_langs)
    input_language = presenter.get_input_from_client("Input language name from list above (case insensitive): ")
    presenter.present_text("Here are all the possible input languages: ")
    output_langs = translator_service.get_possible_output_languages()
    presenter.present_list_of_texts(output_langs)
    output_language = presenter.get_input_from_client("Output language name from list above (case insensitive): ")
    word = presenter.get_input_from_client(f"Type word in {input_language} to translate to {output_language}: ")
    translator_service.translate_word(Word(word, input_language), [output_language])


def show_commands(presenter: Presenter):
    presenter.present_text("Some of the useful commands: ")
    for command, description in COMMANDS:
        presenter.present_text(f"    Command: '{command}'. Description: '{description}'", False)


def init():
    presenter = PresenterFactory.get_presenter()
    storage = DataPersisterFactory.get_persister()
    translator_adapter = TranslatorAdapterFactory.get_translator()
    translator_service = TranslatorService(translator_adapter, presenter, storage)
    if len(argv) > 1:
        translator_service.translate_word(Word(argv[1], "English"), ["Georgian"], True)
    else:
        presenter.present_text("Welcome to Translate like a Hacker!")
        presenter.present_text("####################################", False)
        presenter.present_text("", False)
        presenter.present_text("Here you will be able to translate languages like a real Hacker!")
        show_commands(presenter)
        while True:
            res = presenter.get_input_from_client("")
            if res.lower() == "exit":
                break
            if res.lower() == "translate":
                interactive_translate(presenter, translator_service)
        presenter.present_text("Good bye ;)")


if __name__ == '__main__':
    init()
