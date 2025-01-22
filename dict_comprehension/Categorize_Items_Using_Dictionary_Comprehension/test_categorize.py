import unittest

from categorize import Categorize


class TestCategorize(unittest.TestCase):
    categorize = Categorize()

    def test_categorize_items_from_lists(self):
        fruit_categories = ["fruit", "fruit", "vegetable", "fruit"]
        fruit_items = ["apple", "banana", "carrot", "orange"]
        fruit_dic = {'vegetable': ['carrot'], 'fruit': ['apple', 'banana', 'orange']}
        numbers_categories = ["even", "odd", "even", "odd"]
        number_items = ["4", "3", "16", "15"]
        number_dic = {'even': ['4', '16'], 'odd': ['3', '15']}

        self.assertEqual(self.categorize.categorize_items_from_lists(fruit_categories, fruit_items), fruit_dic)
        self.assertEqual(self.categorize.categorize_items_from_lists(numbers_categories, number_items), number_dic)

    def test_categorize_items_from_tuple(self):
        categorize_items1 = (["fruit", "fruit", "vegetable", "fruit"],
                             ["apple", "banana", "carrot", "orange"])
        fruit_dic = {'vegetable': ['carrot'], 'fruit': ['apple', 'banana', 'orange']}
        categorize_items2 = (["even", "odd", "even", "odd"],
                             ["4", "3", "16", "15"])
        number_dic = {'even': ['4', '16'], 'odd': ['3', '15']}

        self.assertEqual(self.categorize.categorize_items_from_tuple(categorize_items1), fruit_dic)
        self.assertEqual(self.categorize.categorize_items_from_tuple(categorize_items2), number_dic)


if __name__ == "__main__":
    unittest.main()
