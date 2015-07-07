## Python Practice

Today we're going to be practicing working with functions.

We're also going to be playing with lists and strings.

#### Interpretting test output

1. Run the test suite. You can do this by running `nosetests test_practice.py` in the terminal (`iTerm`).

    You should get something that looks like this:

    ```
    FFFF
    ======================================================================
    FAIL: test_practice.test_sum_ints
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "/Users/giovanna/anaconda/lib/python2.7/site-packages/nose/case.py", line 197, in runTest
        self.test(*self.arg)
      File "/Users/giovanna/github/python-bootcamp/day1/code/test_practice.py", line 11, in test_sum_ints
        n.assert_equal(result, expected, get_message(result, expected))
    AssertionError: Incorrect result. You returned None instead of 7.

    ...
    ```

2. Look for the part of the output that looks like this: `FFFFFF`.

    Notice that there are 6 `F`'s. This is because there are 6 problems and you have failed all of them (because you haven't written any code yet!).

    If you pass a test, instead of an `F`, you will have a `.`. If your code produces an error, it will be replaced with an `E`.

3. Take a look at this example output: `.FE.` This means:
    * Q1: correct!
    * Q2: fail (incorrect result)
    * Q3: error (code doesn't execute properly)
    * Q4: correct!

4. For each question that's not correct, there will be some more details. Note that they won't necessarily be in the same order since `nose` first shows the errors, then the failed tests.

5. For failed tests, look for the line which says: `AssertionError:`. Here you will see your output and the expected output.

#### Write some functions

You are going to be writing the functions that will make the tests in `test_practice.py` pass!

1. Fill in the functions according to their docstrings in `practice.py`. If you are unsure how a function is called, check the example in `test_practice.py`.

2. Once you complete them, have an instructor review your code.
