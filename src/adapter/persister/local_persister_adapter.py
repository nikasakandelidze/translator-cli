from typing import Optional

from adapter.persister.data_persister import DataPersister
from core.domain.word import Word
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root
LOCAL_FOLDER_PATH = f"{ROOT_DIR}/data"


# Translations data format written in file:    from-language:word:to-language:word


class LocalPersisterAdapter(DataPersister):
    def __init__(self):
        super().__init__()

    def put(self, input_word: Word, output_word: Word) -> None:
        try:
            if self.search(input_word, output_word.language):
                return
            with open(LOCAL_FOLDER_PATH, 'a+', encoding='utf-8') as f:
                content = f"{input_word.language}:{input_word.word}:{output_word.language}:" + output_word.word.replace('\r',' ')+'\n'
                f.write(content)
        except Exception:
            pass

    def search(self, search_word: Word, output_language: str) -> Optional[Word]:
        try:
            with open(LOCAL_FOLDER_PATH, 'r', encoding='utf-8') as f:
                for line in f.readlines():
                    parts = line.split(":")
                    if parts[1].lower() == search_word.word.lower() and parts[
                        0].lower() == search_word.language.lower() and parts[2].lower() == output_language.lower():
                        return Word(parts[3].lower(), output_language)
            return None
        except Exception:
            # Problem with reading file
            return None