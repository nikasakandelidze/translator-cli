class Word():
    def __init__(self, word: str, language: str, context:str):
        '''
        :param word: Word's character sequence
        :param language: Language of the word
        :param context: Additional data used for storing this word. This mainly is used to store the additional data/text/context specific sentences provided with some translations.
        '''
        self.word= word
        self.context = context
        self.language = language