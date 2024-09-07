# Tuples are similar to lists but these are immutable.
# Once an element is inside the tuple, we cannot reassign it.
# Tuples does not allow duplicate items and even if we pass duplicate items it will only take the first duplicate item as the index value
# Tuples have only two methods count and index
# Use tuples when your data cannot change.
# Tuples are useful in combination with dictionary where you want tuples to represent a key because its immutable.

tup=('a','b','c','e','e',9)
print(tup)
print(tup.count('e'))
print(tup.index(9))