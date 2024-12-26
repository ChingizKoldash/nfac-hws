import unittest

import hw

class TestFunctions(unittest.TestCase):
    def test_missing_elements(self):
        self.assertEqual(hw.missing_elements([1, 2, 4, 6, 7]), [3, 5])
        self.assertEqual(hw.missing_elements([]), [])
        self.assertEqual(hw.missing_elements([1, 2, 3]), [])
        self.assertEqual(hw.missing_elements([1] + [2, 3] + [10**6]), list(range(4, 10**6)))
        self.assertEqual(hw.missing_elements(list(range(1, 10**6+2))), [])

    def test_count_occurrences(self):
        self.assertEqual(hw.count_occurrences([1, 2, 3, 1, 2, 4, 5, 4]), {1: 2, 2: 2, 3: 1, 4: 2, 5: 1})
        self.assertEqual(hw.count_occurrences([]), {})
        self.assertEqual(hw.count_occurrences([1]*10**6 + [2]*10**6), {1: 10**6, 2: 10**6})
        self.assertEqual(hw.count_occurrences([1, 1, 2, 2, 3, 3]), {1: 2, 2: 2, 3: 2})
        self.assertEqual(hw.count_occurrences([1]), {1: 1})

    def test_common_elements(self):
        self.assertEqual(hw.common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]), [3, 4, 5])
        self.assertEqual(hw.common_elements([1, 2, 3], [4, 5, 6]), [])
        self.assertEqual(hw.common_elements([], [1, 2, 3]), [])
        self.assertEqual(hw.common_elements(list(range(1, 10**6+1)), list(range(500000, 10**6+2))), list(range(500000, 10**6+1)))
        self.assertEqual(hw.common_elements([1, 2, 3], [1, 2, 3]), [1, 2, 3])

    def test_char_frequency(self):
        self.assertEqual(hw.char_frequency('hello world'), {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
        self.assertEqual(hw.char_frequency(''), {})
        self.assertEqual(hw.char_frequency('a'*10**6 + 'b' + 'a'*10**6), {'a': 2*10**6, 'b': 1})
        self.assertEqual(hw.char_frequency('abcabc'), {'a': 2, 'b': 2, 'c': 2})
        self.assertEqual(hw.char_frequency('abcdefg'), {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1})

    def test_unique_words(self):
        self.assertEqual(hw.unique_words('hello world hello'), 2)
        self.assertEqual(hw.unique_words(''), 0)
        self.assertEqual(hw.unique_words('a '*10**6), 1)
        self.assertEqual(hw.unique_words('hello hello world world'), 2)
        self.assertEqual(hw.unique_words('hello world hello world'), 2)

    def test_word_frequency(self):
        self.assertEqual(hw.word_frequency('hello world hello'), {'hello': 2, 'world': 1})
        self.assertEqual(hw.word_frequency(''), {})
        self.assertEqual(hw.word_frequency('a '*10**6), {'a': 10**6})
        self.assertEqual(hw.word_frequency('hello hello world world'), {'hello': 2, 'world': 2})
        self.assertEqual(hw.word_frequency('hello world hello world'), {'hello': 2, 'world': 2})

    def test_count_in_range(self):
        self.assertEqual(hw.count_in_range([1, 2, 3, 4, 5, 4, 3, 2, 1], 2, 4), 3)
        self.assertEqual(hw.count_in_range([], 2, 4), 0)
        self.assertEqual(hw.count_in_range(list(range(1, 10**6+1)), 2, 4), 3)
        self.assertEqual(hw.count_in_range(list(range(1, 10**6+1)), 500000, 10**6), 500001)
        self.assertEqual(hw.count_in_range([1, 2, 3, 4, 5], 6, 10), 0)

    def test_swap_dict(self):
        self.assertEqual(hw.swap_dict({1: 'a', 2: 'b', 3: 'c'}), {'a': 1, 'b': 2, 'c': 3})
        self.assertEqual(hw.swap_dict({}), {})
        self.assertEqual(hw.swap_dict({i: str(i) for i in range(1, 10**6+1)}), {str(i): i for i in range(1, 10**6+1)})
        self.assertEqual(hw.swap_dict({'a': 1, 'b': 1}), {1: 'a'})
        self.assertEqual(hw.swap_dict({'a': 1, 'b': 2, 'c': 3}), {1: 'a', 2: 'b', 3: 'c'})

    def test_is_subset(self):
        self.assertEqual(hw.is_subset({1, 2, 3, 4, 5}, {3, 4, 5}), True)
        self.assertEqual(hw.is_subset({1, 2, 3}, {4, 5, 6}), False)
        self.assertEqual(hw.is_subset(set(), {1, 2, 3}), False)
        self.assertEqual(hw.is_subset({i for i in range(1, 10**6+1)}, {i for i in range(500000, 10**6+1)}), True)
        self.assertEqual(hw.is_subset({1, 2, 3}, {1, 2, 3}), True)

    def test_list_intersection(self):
        self.assertEqual(hw.list_intersection([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]), [3, 4, 5])
        self.assertEqual(hw.list_intersection([1, 2, 3], [4, 5, 6]), [])
        self.assertEqual(hw.list_intersection([], [1, 2, 3]), [])
        self.assertEqual(hw.list_intersection(list(range(1, 10**6+1)), list(range(500000, 10**6+2))), list(range(500000, 10**6+1)))
        self.assertEqual(hw.list_intersection([1, 2, 3], [1, 2, 3]), [1, 2, 3])

    def test_list_union(self):
        self.assertEqual(hw.list_union([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]), [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(hw.list_union([1, 2, 3], []), [1, 2, 3])
        self.assertEqual(hw.list_union([], [1, 2, 3]), [1, 2, 3])
        self.assertEqual(hw.list_union(list(range(1, 10**6+1)), list(range(500000, 10**6+2))), list(range(1, 10**6+2)))
        self.assertEqual(hw.list_union([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])

    def test_most_frequent(self):
        self.assertEqual(hw.most_frequent([1, 2, 3, 1, 2, 4, 5, 4, 1]), 1)
        self.assertEqual(hw.most_frequent([1, 2, 3]), 1)  # in case of tie, return the one that appears first
        self.assertEqual(hw.most_frequent([1]*10**6 + [2]*10**6 + [3]), 1)
        self.assertEqual(hw.most_frequent([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]*10**5 + [11]), 1)
        self.assertEqual(hw.most_frequent([1]), 1)

    def test_least_frequent(self):
        self.assertEqual(hw.least_frequent([1, 2, 3, 1, 2, 4, 5, 4, 1]), 3)
        self.assertEqual(hw.least_frequent([1, 2, 3]), 1)  # in case of tie, return the one that appears first
        self.assertEqual(hw.least_frequent([1]*10**6 + [2]*10**6 + [3]), 3)
        self.assertEqual(hw.least_frequent([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]*10**5 + [11]), 11)
        self.assertEqual(hw.least_frequent([1]), 1)

if __name__ == "__main__":
    unittest.main()