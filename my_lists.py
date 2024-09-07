#use lists if you have a collection of data that does not need random access.
# It is simple, iterable collection and can be modified frequently

# Using some of the common methods of Lists

#Two ways of sorting the list, either use mylist.sort() or sorted(mylist)
mylist=[1,4,3,2,7,5,6]
newlist=[0,3,1,2]
mylist.sort()     # this expression does not return in notebook and we need to call the mylist to be able to view the sorted list
sorted(newlist)   # this expression is returning the sorted list in notebook but this will not run in the pycharm IDE
print(f'Sorted mylist {mylist}')
print(f'sorted newlist {newlist}')  # this is an example of sorted method does not work in pycharm
print(f'sorted method works in print function {sorted(newlist)}')   # sorted method works in the print function

#Using pop, remove, append. I am using another list with name mixedlist
mixedlist=['John',5,'Mary',6,'Mark',7]
mixedlist.pop()         # we are removing last element of the list which is 7
print(mixedlist)
mixedlist.remove(mixedlist[0])   # we are removing John which is at index 0
print(mixedlist)
mixedlist.append(7)         # we have added an element 7 to the list
print(mixedlist)

#Reassign ‘hello’ in this nested list to say ‘Hi’. I am using a new list called as list3
list3= [1,2,[3,4,'hello']]
list3[2][2]='Hi'        # I am calling the hello element by using the indexing value
print(list3)

