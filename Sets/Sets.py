# Sets get rid of duplicate values
# One difference between a set and a list is that the items in a set have no specific order. Even though you may define the set with the items in a certain order, 
# none of the items get index numbers to identify their position.

sample_set = {1.98, 98.9, 74.95, 2.5, 1, 16.3}

sample_set.add(11.23)

# Sets are similar to lists and tuples in a few ways. You can use len() to determine how many items are in a set. Use in to determine whether an item is in a set. But you can’t get an item in a set based on its index number. Nor can you change an item already in the set. You can’t change the order of items in a set either. So you can’t use .sort() to sort the set or .reverse() to reverse its order.
