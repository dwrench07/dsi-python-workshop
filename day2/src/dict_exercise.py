#!/usr/bin/env python
"""Exercises to attain mastery of Python dictionaries."""


def dict_to_str(input_dict):
    """Return a str containing each key and value in dict d.

    Keys and values are separated by a colon and a space.
    Each key-value pair is separated by a new line.

    Parameters
    ----------
    input_dict : dict

    Returns
    -------
    output_text : str
    """
    return "\n".join("{}: {}".format(k, v) for (k, v) in input_dict.items())


input_dict = {"something": 4, "other": "pie"}
print(dict_to_str(input_dict))
assert dict_to_str(input_dict) == "something: 4\nother: pie"


def dict_to_str_sorted(d):
    import operator
    """Return an ordered str containing each key and value in dict d.

    This is sorted version of dict_to_str().

    Keys and values are separated by a colon and a space.
    Each key-value pair is sorted in ascending order by key.

    Note: This one is also doable in one line!

    Parameters
    ----------
    input_dict : dict

    Returns
    -------
    output_text : str
    """
    """
    It is not possible to sort a dict, only to get a representation of a dict that is sorted. 
    Dicts are inherently orderless, but other types, such as lists and tuples, are not. 
    So you need a sorted representation, which will be a list—probably a list of tuples.
    """
    sorted_d = sorted(d.items(), key=operator.itemgetter(1))
    return sorted_d
    # sorted_d will be a list of tuples sorted by the second element in each tuple. dict(sorted_d) == x.
    """Or...
    >>>sorted(d.items(), key=lambda x: x[1])
    This will sort the dictionary by the values of each entry within the dictionary from smallest to largest.
    """
    """
    And for those wishing to sort on keys instead of values:
    >>>import operator
    x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    sorted_x = sorted(x.items(), key=operator.itemgetter(0))
    """


# d = {"something": 4, "other": 7}
# print(dict_to_str_sorted(d))
# assert dict_to_str_sorted(d) == "other: 7\nsomething: 4"


def dict_difference(d1, d2):
    """Combine two dictionaries according to a specified set of rules.

    Combine the two dictionaries, d1 and d2, as follows:
        1. The keys are the union of the keys from each dictionary.
        2. If a key is in both dictionaries, then the value for that
           key should be the absolute value of the difference between
           the two values for that key.
        3. If a key is only in one dictionary, the value should be the
           absolute value of that value for that key.

    Parameters
    ----------
    d1 : dict
    d2 : dict

    Returns
    -------
    dict
    """
    diff = set(d1).difference(set(d2))
    return diff


d1 = {"something": 4, "something else": 78, "other": 17}
d2 = {"something": 4, "other": 7}
print(dict_difference(d1, d2))
assert dict_difference(d1, d2) == {"something else"}
