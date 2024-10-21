import unittest
from lesson_06.homework_06_4 import sum_all_even
from lesson_07.homework_07 import count_words_with_uppercase, mid_num_list, longest_word

# File: lesson_07/homework_07.py
# Function: count_words_with_uppercase
class TestCountWordsWithUppercase(unittest.TestCase):
    def test_count_uppercase_words(self):
        text = "This is a Test to Count Uppercase Words"
        self.assertEqual(count_words_with_uppercase(text), 5)

    def test_no_uppercase_words(self):
        text = "this is a test"
        self.assertEqual(count_words_with_uppercase(text), 0)

    def test_empty_text(self):
        self.assertEqual(count_words_with_uppercase(""), 0)

# File: lesson_07/homework_07.py
# Function: mid_num_list
class TestMidNumList(unittest.TestCase):
    def test_average(self):
        self.assertAlmostEqual(mid_num_list([6, 9, 82, 67, 8, 0, 112, 1, 34, 5, 6, 90]), 35.0)

    def test_single_int_list(self):
        self.assertEqual(mid_num_list([1]), 1)

# File: lesson_07/homework_07.py
# Function: longest_word
class TestLongestWord(unittest.TestCase):
    def test_longest_word(self):
        words = ['cat', 'apple', 'automobile', 'Planetenverteidigungskanonenkommandant', 'car', 'grape', 'butterfly']
        self.assertEqual(longest_word(words), 'Planetenverteidigungskanonenkommandant')

    def test_equal_list(self):
        self.assertEqual(longest_word(['cat', 'app', 'aut']), 'cat')

# File: lesson_06/homework_06_4.py
# Function: sum_all_even
class TestSumAllEven(unittest.TestCase):
    def test_sum_even_numbers(self):
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_sum = 30
        self.assertEqual(sum_all_even(lst), expected_sum)

    def test_empty_list(self):
        self.assertEqual(sum_all_even([]), 0)

    def test_no_even_numbers(self):
        self.assertEqual(sum_all_even([1, 3, 5, 7]), 0)

    def test_all_even_numbers(self):
        self.assertEqual(sum_all_even([2, 4, 6, 8]), 20)

if __name__ == '__main__':
    unittest.main()
