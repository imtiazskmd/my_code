# Sets are unordered collections of unique elements and while printing it changes the order everytime
# Only one representative of the same object.
# We cannot add same element again, even if we add, it will not be added.
# it does not allow indexing or slicing
# Membership testing and the elimination of duplicate entries
# Use when you need uniqueness for the elements.

myset=set()
print(myset)    # here myset is empty. We can assign only one argument in the set.
myset.add(1)    # 1 element is added in an empty set
print(myset)
myset.add('name')   # 'name' is added to the set which already has 1
print(myset)
myset.add('age')    # 'age' is added to the set
print(myset)
myset.remove(1)     # 1 element is removed from the set
print(myset)

# we can check the unique elements in the list by using set funtion, as below
mylist=[1,2,2,3,2,3,4,5,4]
print(set(mylist))

# we can even check the unique elements in a string, as below
print(set('Parallel'))