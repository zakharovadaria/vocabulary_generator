Vocabulary Generator
====================

.. image:: https://coveralls.io/repos/github/zakharovadaria/vocabulary_generator/badge.svg?branch=master
    :target: https://coveralls.io/github/zakharovadaria/vocabulary_generator?branch=master

.. image:: https://travis-ci.org/zakharovadaria/vocabulary_generator.svg?branch=master
    :target: https://travis-ci.org/zakharovadaria/vocabulary_generator

.. image:: https://badge.fury.io/py/vocabulary_generator.svg
    :target: https://badge.fury.io/py/vocabulary_generator

This generator helps you to know about unknown words for you in your text

Installing
----------

Install and update using pip:

.. code-block:: text

    pip install vocabulary_generator

Usage
-----
If you want to know only unknown words in your text use:

.. code-block:: python

    >>> from vocabulary_generator import get_unknown_words
    >>> text = "Hello, my dear friend! How are you? Are you good?"
    >>> known_words = ["hello", "friend", "how"]
    >>> get_unknown_words(text, known_words)
    ["my", "dear", "be", "you", "good"]


If you want to know unknown words frequency you can use:

.. code-block:: python

    >>> from vocabulary_generator import get_words_frequency
    >>> text = "Hello, my dear friend! How are you? Are you good?"
    >>> known_words = ["hello", "friend", "how"]
    >>> get_words_frequency(text, known_words)
    {"be": 2, "you": 2, "my": 1, "dear": 1, "good": 1}


Workflow
--------

.. image:: https://user-images.githubusercontent.com/10631818/73606694-29772b80-45be-11ea-8aca-a654e7e3703f.png
  :width: 400