import unittest
import re
from faspell.spell_checker import SpellChecker


class Test(unittest.TestCase):
    def test_correct(self):
        with open('dictionary', 'r') as dictionary:
            checker = SpellChecker(train(words(dictionary.read())))

            # proper persian input
            self.assertEqual(checker.correct('شلام'),
                             [{'suggestions': ['آلام', 'سلام', 'شالم', 'شام', 'شلاق', 'شلاقم', 'شلغم', 'شلهم', 'غلام',
                                               'لام', 'کلام'], 'word': 'شلام', 'ud': False}])
            # inappropriate persian input
            self.assertEqual(checker.correct('سلام'), [])
            # english input
            self.assertEqual(checker.correct('hello'), [{'suggestions': [], 'word': 'hello', 'ud': False}])
            # character input
            self.assertEqual(checker.correct('%$#%$#^#'), [{'word': '%$#%$#^#', 'suggestions': [], 'ud': False}])


def words(database):
    return re.split('\n', database)


def train(features):
    model = dict.fromkeys(features, 1)
    return model

if __name__ == '__main__':
    unittest.main()