from vocabulary_generator.core import get_words_in_text, get_initial_form
from vocabulary_generator.core import get_pos_tag, get_words_in_initial_form
from vocabulary_generator.core import get_words_frequency, get_unknown_words
from vocabulary_generator.core import get_clear_text


class TestGetWords:
    def test_get_clear_text(self):
        text = '  '

        actual = get_clear_text(text)
        expected = ''

        assert actual == expected

        text = ' Hello,   world! '

        actual = get_clear_text(text)
        expected = 'Hello world'

        assert actual == expected

    def test_get_words_in_text(self):
        text = 'Hello world'
        actual = get_words_in_text(text)
        expected = ['hello', 'world']

        assert actual == expected

    def test_get_words_with_spaces_in_middle(self):
        text = 'Hello    world'
        actual = get_words_in_text(text)
        expected = ['hello', 'world']

        assert actual == expected

    def test_get_words_in_empty_text(self):
        text = ''
        actual = get_words_in_text(text)
        expected = []

        assert actual == expected

    def test_get_words_in_text_with_spaces(self):
        text = '  '
        actual = get_words_in_text(text)
        expected = []

        assert actual == expected

    # def test_get_words_in_text_with_punctuation(self):
    #     text = 'Hello, world!!!!! It, - winter...'
    #     actual = get_words_in_text(text)
    #     print(actual)
    #     expected = ['hello', 'world', 'it', 'winter']
    #
    #     assert actual == expected


class TestInitialForm:
    def test_get_initial_form_of_subject(self):
        word = 'cats'
        actual = get_initial_form(word)
        expected = 'cat'

        assert actual == expected

    def test_get_initial_form_of_irregular_verb(self):
        word = 'took'
        actual = get_initial_form(word)
        expected = 'take'

        assert actual == expected

    def test_get_initial_form_of_regular_verb(self):
        word = 'tested'
        actual = get_initial_form(word)
        expected = 'test'

        assert actual == expected

    def test_get_words_in_initial_form(self):
        words = ['been', 'had', 'done', 'languages', 'cities', 'mice']

        actual = get_words_in_initial_form(words)
        expected = ['be', 'have', 'do', 'language', 'city', 'mouse']

        assert actual == expected


class TestPosTags:
    def test_get_pos_tag_adjective(self):
        word = 'small'

        actual = get_pos_tag(word)
        expected = 'a'

        assert actual == expected

    def test_get_pos_tag_noun(self):
        word = 'languages'

        actual = get_pos_tag(word)
        expected = 'n'

        assert actual == expected

    def test_get_pos_tag_verb(self):
        word = 'took'

        actual = get_pos_tag(word)
        expected = 'v'

        assert actual == expected


class TestCountWords:
    def test_words_frequency(self):
        words = ['been', 'had', 'been', 'had', 'be', 'was', 'been']

        actual = get_words_frequency(words)
        expected = {
            'been': 3,
            'had': 2,
            'be': 1,
            'was': 1,
        }

        assert actual == expected

        actual = get_words_frequency(words, most_common=2)
        expected = {
            'been': 3,
            'had': 2,
        }

        assert actual == expected

    def test_frequency_of_empty_list(self):
        words = []

        actual = get_words_frequency(words)
        expected = {}

        assert actual == expected


class TestUnknownWords:
    def test_get_unknown_words(self):
        text = 'been had done languages cities mice feet took went'
        known_words = ['be', 'do', 'take']

        actual = get_unknown_words(text, known_words)
        expected = ['have', 'language', 'city', 'mouse', 'foot', 'go']

        assert actual == expected

    def test_get_unknown_words_with_not_unknown_words(self):
        text = 'been done took'
        known_words = ['be', 'do', 'take']

        actual = get_unknown_words(text, known_words)
        expected = []

        assert actual == expected

    def test_get_unknown_words_with_not_known_words(self):
        text = 'been done took'
        known_words = []

        actual = get_unknown_words(text, known_words)
        expected = ['be', 'do', 'take']

        assert actual == expected

    def test_get_unknown_words_with_frequency(self):
        text = 'been done took been done took been done took been done'
        known_words = []

        actual = get_unknown_words(text, known_words)
        expected = ['be', 'do', 'take', 'be', 'do', 'take', 'be', 'do', 'take', 'be', 'do']

        assert actual == expected

        actual = get_words_frequency(actual)
        expected = {
            'be': 4,
            'do': 4,
            'take': 3,
        }

        assert actual == expected
