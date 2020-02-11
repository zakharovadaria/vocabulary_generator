import re
from collections import Counter
from typing import List

from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import nltk


def get_clear_text(text: str) -> str:
    text_without_punctuation = re.sub(r"[^\w\s]", "", text)
    text_without_space_around = text_without_punctuation.strip()
    text_with_one_spaces = re.sub(r" +", " ", text_without_space_around)
    return text_with_one_spaces


def get_words_in_text(text: str) -> List[str]:
    words = get_clear_text(text).lower().split(' ')
    filtered_words = list(filter(lambda word: word, words))
    return filtered_words


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


def get_words_in_initial_form(words: List[str]) -> List[str]:
    initial_words = []
    for word in words:
        initial_word = get_initial_form(word)
        initial_words.append(initial_word)

    return initial_words


def get_words_frequency(words: List[str], *, most_common: int = None) -> dict:
    return dict(Counter(words).most_common(most_common))


def get_unknown_words(text: str, known_words: List[str]) -> List[str]:
    words = get_words_in_text(text)
    words_in_initial_form = get_words_in_initial_form(words)
    known_words_in_initial_form = get_words_in_initial_form(known_words)
    unknown_words = []

    for word in words_in_initial_form:
        if word not in known_words_in_initial_form:
            unknown_words.append(word)

    return unknown_words
