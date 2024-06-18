import unittest
import src.utilityFunctions as uf
import os
import itertools
import fnmatch
from src.utilityFunctions import pathJoiner, loadConfig


def findFile(word, path):

    result = []
    pattern = f'{word}.*'
    number_pattern = f'{word}[0-9].*'

    for root, _, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern) or fnmatch.fnmatch(name, number_pattern):
                result.append(pathJoiner(root, name))
    return result

class TestpathJoiner(unittest.TestCase):
    def testpathJoinerSlashes(self):
        root = ["resources/media/images", "resources/media/images/", "resources\\media\\images", "resources\\media\\images"]

        # itertools.product iterating through string elements rather than list when file1 and file2 in list together, separated due to lack of desire to solve problem.
        file1 = ["ciao.jpg"]
        file2 = ["nextpath/ciao.jpg"]

        # combine file1 and file2 into separate lists of all their combinations with root.
        file1PathCombinations = itertools.product(root, file1)
        file2PathCombinations = itertools.product(root, file2)

        for combo in file1PathCombinations:
            result = uf.pathJoiner(*combo)
            self.assertEqual(result, os.path.normpath('resources\\media\\images\\ciao.jpg'))

        for combo in file2PathCombinations:
            result = uf.pathJoiner(*combo)
            self.assertEqual(result, os.path.normpath('resources\\media\\images\\nextpath\\ciao.jpg'))

class TestFindFile(unittest.TestCase):

    def testExpectedValues(self):
        path = pathJoiner('tests/testdata', 'mediadir')
        word = 'accogliere'
        expected_result = [
                        pathJoiner(path, 'accogliere.jpg'),
                        pathJoiner(path, 'accogliere2.jpg')
                        ]

        result = findFile(word, path)

        self.assertEqual(result, expected_result)





if __name__ == '__main__':
    unittest.main()