from typing import List, Set

from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import nltk


def get_all_words_in_text(text: str) -> List[str]:
    text_without_spaces_around = text.strip()
    if not text_without_spaces_around:
        return []

    words = text_without_spaces_around.lower().split(' ')

    return words


def get_unique_words(words: List[str]) -> Set[str]:
    unique_words = set(words)

    return unique_words


def get_initial_form(word: str) -> str:
    lemmatizer = WordNetLemmatizer()

    initial_form = lemmatizer.lemmatize(word, get_pos_tag(word))

    return initial_form


def get_pos_tag(word: str) -> str:
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {
        'J': wordnet.ADJ,
        'N': wordnet.NOUN,
        'V': wordnet.VERB,
        'R': wordnet.ADV
    }
    return tag_dict.get(tag, wordnet.NOUN)


def get_all_words_in_initial_form(words: Set[str]) -> Set[str]:
    initial_words = set()
    for word in words:
        initial_word = get_initial_form(word)
        initial_words.add(initial_word)

    return initial_words


def get_unique_words_in_initial_form(text: str) -> Set[str]:
    words = get_all_words_in_text(text)
    unique_words = get_unique_words(words)
    words_in_initial_form = get_all_words_in_initial_form(unique_words)

    return words_in_initial_form


def get_unknown_words(text: str, known_words: Set[str]) -> Set[str]:
    words_from_text = get_unique_words_in_initial_form(text)
    unknown_words = words_from_text.difference(known_words)

    return unknown_words
