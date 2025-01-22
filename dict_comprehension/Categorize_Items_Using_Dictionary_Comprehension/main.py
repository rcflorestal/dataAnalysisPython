from categorize import Categorize

# Example of usage:
categorize = Categorize()

# Using lists
categories = ["fruit", "fruit", "vegetable", "fruit"]
items = ["apple", "banana", "carrot", "orange"]
dic_from_lists = categorize.categorize_items_from_lists(categories, items)
print(dic_from_lists)

# Using tuple
categorize_items = (["fruit", "fruit", "vegetable", "fruit"],
                    ["apple", "banana", "carrot", "orange"])
dic_from_tuple = categorize.categorize_items_from_tuple(categorize_items)
print(dic_from_tuple)
