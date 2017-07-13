
def sum_ints(lst):
    """
    INPUT: list
    OUTPUT: int

    The input list contains a mixture of integers, floats and strings. Sum up
    only the ints.
    Hint: Use the isinstance function.
    """
    sum_of_ints = 0
    for item in lst:
        if isinstance(item, int):
            sum_of_ints += item
    print(f"sum_ints() = {sum_of_ints}")
    return sum_of_ints


assert sum_ints(['foo', 4, 'bar', 5]) == 9


def min_and_max(lst):
    """
    INPUT: list
    OUTPUT: tuple of two ints/floats

    Given a list of ints and/or floats, return a 2-tuple containing the values
    of the items with the smallest and largest absolute values.

    In the case of an empty list, return None.
    """
    if not lst:
        return None
    else:
        abs_lst = [abs(item) for item in lst]
        print("Min = {}, Max = {}".format(min(abs_lst), max(abs_lst)))
        return min(abs_lst), max(abs_lst)


assert min_and_max([1.2, 4, -3.6, 5]) == (1.2, 5)


def are_palindromes(words):
    """
    INPUT: list
    OUTPUT: bool

    Given a list of strings, return whether ALL of the elements are
    palindromes.

    Hint: use the is_palindrome function that has been imported at
    the top of this file
    """
    palindromes = 0
    for word in words:
        # if list(word) == list(reversed(list(word))):
        if word == word[::-1]:
            palindromes += 1
        else:
            print("Not all words were palindromes.")
            return False

    if palindromes == len(words):
        print("Palindromes: {}".format(palindromes))
        return True


assert are_palindromes(['level', 'abba', 'racecar']) == True
assert are_palindromes(['dad', 'abc']) == False


def substring(words, substrings):
    """
    INPUT: list, list
    OUTPUT: list

    Given two lists of strings, return the list of strings from the second list
    that are a substring of a string in the first list.

    The strings in the substrings list are all 3 characters long.
    """
    matches = []

    for sub in substrings:
        for word in words:
            if sub in word:
                matches.append(sub)
    print(matches)
    # return [sub for sub in substrings for word in words if sub in word]
    return matches


assert substring(['beautiful', 'world'], ['if', 'c', 'be']) == ['if', 'be']
