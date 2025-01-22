class Categorize:
    def __init__(self):
        self.input_tuple = None
        self.item_list = None
        self.category_list = None

    def categorize_items_from_lists(self, category_list, item_list):
        """
        Categorize items based on separate lists for categories and items.

        :param category_list: List of categories.
        :param item_list: List of items corresponding to categories.
        :return: Dictionary with categories as keys and lists of items as values.
        """
        if len(category_list) != len(item_list):
            raise ValueError("category_list and item_list must have the same length.")

        self.category_list = category_list
        self.item_list = item_list

        categorized_dic = {
            category: [item for i, item in enumerate(self.item_list) if category == self.category_list[i]]
            for category in set(self.category_list)
        }

        return categorized_dic

    def categorize_items_from_tuple(self, input_tuple):
        """
        Categorize items based on a tuple of two lists (categories and items).

        :param input_tuple: Tuple containing two lists - (categories, items).
        :return: Dictionary with categories as keys and lists of items as values.
        """
        if len(input_tuple) != 2 or len(input_tuple[0]) != len(input_tuple[1]):
            raise ValueError("Input tuple must contain two lists of equal length.")

        self.input_tuple = input_tuple
        categorized_dic = {
            category: [item for i, item in enumerate(self.input_tuple[1]) if category == self.input_tuple[0][i]]
            for category in set(self.input_tuple[0])
        }

        return categorized_dic
