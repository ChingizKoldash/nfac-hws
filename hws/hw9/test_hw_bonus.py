import unittest

import hw_bonus

class TestFunctions(unittest.TestCase): 
    def test_two_sum(self):
        self.assertEqual(hw_bonus.two_sum([2, 7, 11, 15], 9), (0, 1))
        self.assertEqual(hw_bonus.two_sum([3, 2, 4], 6), (1, 2))
        self.assertEqual(hw_bonus.two_sum([1]*10**6 + [2, 3], 5), (10**6, 10**6 + 1))
        self.assertEqual(hw_bonus.two_sum([2, 7, 11, 15]*10**5 + [5, 7], 12), (400000, 400001))
        self.assertEqual(hw_bonus.two_sum([1, 3], 4), (0, 1))

    def test_is_isomorphic(self):
        self.assertEqual(hw_bonus.is_isomorphic('egg', 'add'), True)
        self.assertEqual(hw_bonus.is_isomorphic('foo', 'bar'), False)
        self.assertEqual(hw_bonus.is_isomorphic('ab'*10**5, 'cd'*10**5), True)
        self.assertEqual(hw_bonus.is_isomorphic('aa'*10**5, 'ab'*10**5), False)
        self.assertEqual(hw_bonus.is_isomorphic('abcd', 'dcba'), False)

    def test_is_alien_sorted(self):
        self.assertEqual(hw_bonus.is_alien_sorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"), True)
        self.assertEqual(hw_bonus.is_alien_sorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"), False)
        self.assertEqual(hw_bonus.is_alien_sorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz"), False)
        self.assertEqual(hw_bonus.is_alien_sorted(["apple","app"]*10**5, "abcdefghijklmnopqrstuvwxyz"), False)
        self.assertEqual(hw_bonus.is_alien_sorted(["a", "b", "c"], "abcdefghijklmnopqrstuvwxyz"), True)

    def test_length_of_longest_substring(self):
        self.assertEqual(hw_bonus.length_of_longest_substring('abcabcbb'), 3)
        self.assertEqual(hw_bonus.length_of_longest_substring('bbbbbb'), 1)
        self.assertEqual(hw_bonus.length_of_longest_substring('pwwkew'), 3)
        self.assertEqual(hw_bonus.length_of_longest_substring('a'*10**6), 1)
        self.assertEqual(hw_bonus.length_of_longest_substring('abc'*10**5), 3)

    def test_group_shifted(self):
        self.assertEqual(hw_bonus.group_shifted(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]), [["abc","bcd"],["acef"],["xyz"],["az","ba"],["a","z"]])
        self.assertEqual(hw_bonus.group_shifted(["abc", "bcd", "acef"]), [["abc","bcd"],["acef"]])
        self.assertEqual(hw_bonus.group_shifted(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]), [["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]])
        self.assertEqual(hw_bonus.group_shifted(["abc"]*10**5), [["abc"]*10**5])
        self.assertEqual(hw_bonus.group_shifted(["abc", "bcd", "cde", "def", "efg", "fgh", "ghi", "hij", "ijk", "jkl", "klm", "lmn", "mno", "nop", "opq", "pqr", "qrs", "rst", "stu", "tuv", "uvw", "vwx", "wxy", "xyz"]), [["abc", "bcd", "cde", "def", "efg", "fgh", "ghi", "hij", "ijk", "jkl", "klm", "lmn", "mno", "nop", "opq", "pqr", "qrs", "rst", "stu", "tuv", "uvw", "vwx", "wxy", "xyz"]])

if __name__ == "__main__":
    unittest.main()