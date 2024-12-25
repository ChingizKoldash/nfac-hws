import unittest
import hw


class TestExercises(unittest.TestCase):
    def test_count_unique_elements(self):
        self.assertEqual(hw.count_unique_elements([1, 2, 3, 1, 2, 4, 5, 4]), 5)
        self.assertEqual(hw.count_unique_elements([]), 0)
        self.assertEqual(hw.count_unique_elements([1, 1, 1, 1]), 1)
        self.assertEqual(hw.count_unique_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10)
        self.assertEqual(hw.count_unique_elements([1, 1, 2, 2, 3, 3, 4, 4]), 4)

    def test_remove_duplicates(self):
        self.assertEqual(hw.remove_duplicates([1, 2, 3, 1, 2, 4, 5, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(hw.remove_duplicates([]), [])
        self.assertEqual(hw.remove_duplicates([1, 1, 1, 1]), [1])
        self.assertEqual(hw.remove_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(hw.remove_duplicates([1, 1, 2, 2, 3, 3, 4, 4]), [1, 2, 3, 4])

    def test_reverse_list(self):
        self.assertEqual(hw.reverse_list([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])
        self.assertEqual(hw.reverse_list([]), [])
        self.assertEqual(hw.reverse_list([1]), [1])
        self.assertEqual(hw.reverse_list([1, 2]), [2, 1])
        self.assertEqual(hw.reverse_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

    def test_max_value(self):
        self.assertEqual(hw.max_value([1, 2, 3, 4, 5]), 5)
        self.assertEqual(hw.max_value([1]), 1)
        self.assertEqual(hw.max_value([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(hw.max_value([1, 1, 1, 1]), 1)
        self.assertEqual(hw.max_value([10**6]*10), 10**6)

    def test_min_value(self):
        self.assertEqual(hw.min_value([1, 2, 3, 4, 5]), 1)
        self.assertEqual(hw.min_value([1]), 1)
        self.assertEqual(hw.min_value([-1, -2, -3, -4, -5]), -5)

    def test_sum_values(self):
        self.assertEqual(hw.sum_values([1, 2, 3, 4, 5]), 15)
        self.assertEqual(hw.sum_values([1]), 1)
        self.assertEqual(hw.sum_values([-1, -2, -3, -4, -5]), -15)
        self.assertEqual(hw.sum_values([1, 1, 1, 1]), 4)
        self.assertEqual(hw.sum_values([10**6]*10**6), 10**12)

    def test_average(self):
        self.assertEqual(hw.average([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(hw.average([1]), 1.0)
        self.assertEqual(hw.average([-1, -2, -3, -4, -5]), -3.0)
        self.assertEqual(hw.average([1, 1, 1, 1]), 1.0)
        self.assertEqual(hw.average([10**6]*10**6), 10**6)

    def test_find_index(self):
        self.assertEqual(hw.find_index([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(hw.find_index([1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(hw.find_index([], 1), -1)
        self.assertEqual(hw.find_index([1, 1, 1, 1], 1), 0)
        self.assertEqual(hw.find_index([1, 2, 3, 4, 5], 1), 0)

    def test_is_sorted(self):
        self.assertTrue(hw.is_sorted([1, 2, 3, 4, 5]))
        self.assertFalse(hw.is_sorted([1, 3, 2, 4, 5]))
        self.assertTrue(hw.is_sorted([]))
        self.assertTrue(hw.is_sorted([1]))
        self.assertTrue(hw.is_sorted([-1, -1, 0, 1, 2]))

    def test_count_frequency(self):
        self.assertEqual(hw.count_frequency([1, 2, 3, 4, 5, 1, 2, 3], 3), 2)
        self.assertEqual(hw.count_frequency([1, 2, 3, 4, 5], 6), 0)
        self.assertEqual(hw.count_frequency([], 1), 0)
        self.assertEqual(hw.count_frequency([1, 1, 1, 1], 1), 4)
        self.assertEqual(hw.count_frequency([1, 2, 3, 4, 5], 1), 1)

    def test_find_mode(self):
        self.assertEqual(hw.find_mode([1, 2, 3, 4, 5, 1, 2, 2, 3]), 2)
        self.assertEqual(hw.find_mode([1]), 1)
        self.assertEqual(hw.find_mode([]), None)
        self.assertEqual(hw.find_mode([1, 2, 3]), 1)
        self.assertEqual(hw.find_mode([1, 1, 1, 2, 2]), 1)

    def test_remove_all(self):
        self.assertEqual(hw.remove_all([1, 2, 3, 4, 5, 1, 2, 3], 3), [1, 2, 4, 5, 1, 2])
        self.assertEqual(hw.remove_all([], 1), [])
        self.assertEqual(hw.remove_all([1, 1, 1, 1], 1), [])
        self.assertEqual(hw.remove_all([1, 2, 3], 4), [1, 2, 3])

    def test_rotate_left(self):
        self.assertEqual(hw.rotate_left([1, 2, 3, 4, 5], 2), [3, 4, 5, 1, 2])
        self.assertEqual(hw.rotate_left([], 1), [])
        self.assertEqual(hw.rotate_left([1], 1), [1])
        self.assertEqual(hw.rotate_left([1, 2], 1), [2, 1])
        self.assertEqual(hw.rotate_left([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])

    def test_rotate_right(self):
        self.assertEqual(hw.rotate_right([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3])
        self.assertEqual(hw.rotate_right([], 1), [])
        self.assertEqual(hw.rotate_right([1], 1), [1])
        self.assertEqual(hw.rotate_right([1, 2], 1), [2, 1])
        self.assertEqual(hw.rotate_right([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])

    def test_find_intersection(self):
        self.assertEqual(hw.find_intersection([1, 2, 3, 4], [3, 4, 5, 6]), [3, 4])
        self.assertEqual(hw.find_intersection([], []), [])
        self.assertEqual(hw.find_intersection([1], [2]), [])
        self.assertEqual(hw.find_intersection([1, 2, 3], [3, 4, 5]), [3])
        self.assertEqual(hw.find_intersection([1, 1, 1, 1], [1, 1, 1, 1]), [1])

    def test_find_union(self):
        self.assertEqual(hw.find_union([1, 2, 3, 4], [3, 4, 5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(hw.find_union([], []), [])
        self.assertEqual(hw.find_union([1], [2]), [1, 2])
        self.assertEqual(hw.find_union([1, 2, 3], [3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(hw.find_union([1, 1, 1, 1], [1, 1, 1, 1]), [1])

    def test_find_difference(self):
        self.assertEqual(hw.find_difference([1, 2, 3, 4], [3, 4, 5, 6]), [1, 2])
        self.assertEqual(hw.find_difference([], []), [])
        self.assertEqual(hw.find_difference([1], [2]), [1])
        self.assertEqual(hw.find_difference([1, 2, 3], [3, 4, 5]), [1, 2])


if __name__ == '__main__':
    unittest.main()
