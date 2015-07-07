import nose.tools as n
import dict_exercise


def test_dict_to_str():
    d = {'a': 1, 'b': 2}
    expected1 = 'a: 1\nb: 2'
    expected2 = 'b: 2\na: 1'
    actual = dict_exercise.dict_to_str(d)
    n.assert_equal(type(actual), str, 'Need to return a string.')
    n.assert_in(actual, (expected1, expected2), 'Incorrect output.')


def test_dict_to_str_sorted():
    d = {'c': 3, 'a': 1, 'd': 4, 'b': 2}
    expected = 'a: 1\nb: 2\nc: 3\nd: 4'
    actual = dict_exercise.dict_to_str_sorted(d)
    n.assert_equal(type(actual), str, 'Need to return a string.')
    n.assert_equal(expected, actual, 'Incorrect output.')


def test_dict_difference():
    d1 = {'a': 1, 'b': 2, 'c': 3}
    d2 = {'b': 1, 'c': 10, 'd': -4}
    expected = {'a': 1, 'b': 1, 'c': 7, 'd': 4}
    actual = dict_exercise.dict_difference(d1, d2)
    n.assert_equal(type(actual), dict, 'Need to return a dictionary.')
