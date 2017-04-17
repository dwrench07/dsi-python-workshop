import unittest
import new_examples as examples
from collections import Counter

class TestExamples(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Run before testing begins."""
        pass

    def setUp(self):
        """Run before each test."""
        pass

    def tearDown(self):
        """Run after each test."""
        pass

    @classmethod
    def tearDownClass(cls):
        """Run after all tests are complete."""
        pass

    def test_read_input(self):
        actual = examples.get_word_frequencies_Counter('and',
                                                      'fav_novel_chaper13.txt')
        expected = 48
        self.assertEqual(expected, actual)

    def test_unique_word_from_string(self):
        actual = examples.get_unique_words_from_string('and And blah foobar')
        expected = set(['and', 'blah', 'foobar'])
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
