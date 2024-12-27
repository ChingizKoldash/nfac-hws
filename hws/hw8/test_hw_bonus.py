import unittest
from hw_bonus import *


class TestFunctions(unittest.TestCase):
    """
    💎 Test exercise-1
    """

    def test_longest_consecutive(self):
        self.assertEqual(longest_consecutive([100, 4, 200, 1, 3, 2]), 4)
        self.assertEqual(longest_consecutive([1, 2, 3, 4, 5]), 5)
        self.assertEqual(longest_consecutive([1, 2, 2, 2, 3]), 3)
        self.assertEqual(longest_consecutive([]), 0)

    """
    💎 Test exercise-2
    """

    def test_find_missing(self):
        self.assertEqual(find_missing([1, 2, 4]), 3)
        self.assertEqual(find_missing([1, 3, 4, 5]), 2)
        self.assertEqual(find_missing([2, 3, 4, 5]), 1)
        self.assertEqual(find_missing([1]), None)

    """
    💎 Test exercise-3
    """

    def test_find_duplicate(self):
        self.assertEqual(find_duplicate([1, 3, 4, 2, 2]), 2)
        self.assertEqual(find_duplicate([3, 1, 3, 4, 2]), 3)
        self.assertEqual(find_duplicate([1, 1]), 1)

    """
    💎 Test exercise-4
    """

    def test_group_anagrams(self):
        self.assertEqual(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
                         [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])
        self.assertEqual(group_anagrams([""]), [[""]])
        self.assertEqual(group_anagrams(["a"]), [["a"]])


if __name__ == '__main__':
    unittest.main()
