from vocabulary_generator.core import get_all_words_in_text, get_unique_words, get_initial_form
from vocabulary_generator.core import get_all_words_in_initial_form, get_pos_tag, get_unique_words_in_initial_form
from vocabulary_generator.core import get_unknown_words


def test_get_all_words_in_text():
    text = 'Hello world'
    actual = get_all_words_in_text(text)
    expected = ['hello', 'world']

    assert actual == expected


def test_get_all_words_in_empty_text():
    text = ''
    actual = get_all_words_in_text(text)
    expected = []

    assert actual == expected


def test_get_all_words_in_text_with_spaces():
    text = '  '
    actual = get_all_words_in_text(text)
    expected = []

    assert actual == expected


def test_get_unique_words_count():
    words = ['first', 'second', 'third', 'fourth']
    actual = len(get_unique_words(words))
    expected = 4

    assert actual == expected


def test_get_unique_words_with_repeat_sequence_count():
    words = ['first', 'second', 'first', 'second']
    actual = len(get_unique_words(words))
    expected = 2

    assert actual == expected


def test_get_unique_words_with_empty_list():
    words = []
    actual = get_unique_words(words)
    expected = set()

    assert actual == expected


def test_get_initial_form_of_subject():
    word = 'cats'
    actual = get_initial_form(word)
    expected = 'cat'

    assert actual == expected


def test_get_initial_form_of_irregular_verb():
    word = 'took'
    actual = get_initial_form(word)
    expected = 'take'

    assert actual == expected


def test_get_initial_form_of_regular_verb():
    word = 'tested'
    actual = get_initial_form(word)
    expected = 'test'

    assert actual == expected


def test_get_pos_tag_adjective():
    word = 'small'

    actual = get_pos_tag(word)
    expected = 'a'

    assert actual == expected


def test_get_pos_tag_noun():
    word = 'languages'

    actual = get_pos_tag(word)
    expected = 'n'

    assert actual == expected


def test_get_pos_tag_verb():
    word = 'took'

    actual = get_pos_tag(word)
    expected = 'v'

    assert actual == expected


def test_get_all_words_in_initial_form():
    words = {'been', 'had', 'done', 'languages', 'cities', 'mice'}

    actual = get_all_words_in_initial_form(words)
    expected = {'be', 'have', 'do', 'language', 'city', 'mouse'}

    assert actual == expected


def test_get_unique_words_in_initial_form():
    text = 'been had done languages cities mice been had done languages cities mice been had done languages cities mice'

    actual = get_unique_words_in_initial_form(text)
    expected = {'be', 'have', 'do', 'language', 'city', 'mouse'}

    assert actual == expected


def test_get_unknown_words():
    text = 'been had done languages cities mice feet took went'
    known_words = {'be', 'do', 'take'}

    actual = get_unknown_words(text, known_words)
    expected = {'have', 'language', 'city', 'mouse', 'foot', 'go'}

    assert actual == expected


def test_get_unknown_words_with_not_unknown_words():
    text = 'been done took'
    known_words = {'be', 'do', 'take'}

    actual = get_unknown_words(text, known_words)
    expected = set()

    assert actual == expected
