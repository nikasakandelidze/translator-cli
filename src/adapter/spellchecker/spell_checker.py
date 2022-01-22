from autocorrect import Speller


def correct_word_spelling(word):
    if not word or len(word) == 0:
        return word
    spell = Speller()
    corrected_word = spell(word)
    return (word, corrected_word)