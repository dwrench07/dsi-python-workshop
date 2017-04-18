#!/usr/bin/env python
"""Exercises to practice improving the efficiency of existing Python code."""


from string import punctuation


def find_invalid_words(valid_words, document_filename):
    """Return a list of invalid words found in the specified file.

    Parameters
    ----------
    valid_words : list
    document_filename : str

    Returns
    -------
    invalid_words : list

    Given a list of all the valid words and a document filename, return a list
    of words from the document that are not valid words.
    """
    with open(document_filename) as doc:
        invalid_words = []
        for line in doc:
            words = line.strip().split()
            for word in words:
                if word.lower().strip(punctuation) not in valid_words:
                    invalid_words.append(word)
        return invalid_words


def find_common_characters(input_string, num):
    """Return a list of characters appearing frequently in input_string.

    Parameters
    ----------
    input_string : str
    num : int

    Returns
    -------
    common_characters : list
        List of characters appearing more than num times in input_string.
    """
    common_characters = []
    for char in input_string:
        if input_string.count(char) > num:
            if char not in common_characters:
                common_characters.append(char)
    return common_characters


def sum_to_zero(lst):
    """Return a tuple of two values from the input list that sum to zero.

    If no such pair of values exists, return None.

    Parameters
    ----------
    lst: list
        List of ints.

    Returns
    -------
    value_pair: tuple
        Two integers.
    """
    for i, item1 in enumerate(lst):
        for item2 in lst[i + 1:]:
            if item1 + item2 == 0:
                return item1, item2
