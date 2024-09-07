#Using random and shuffle methods

from random import shuffle

mylist = [1, 2, 3, 4, 5]
shuffle(
    mylist)  #this suffles the elements in the list everytime we execute it. We cannot assign shuffle() to any variable as it will not return anything
print('Example of shuffle method:', mylist)

# using randit method to randomly return a number from certain range of numbers

from random import randint
mynum=randint(0,100)   #we are passing min & max parameter in the randint function and assigning a variable (mynum) to be called from print
print('Random number:',mynum)    # this will pick a random number everytime we execute the code.

# List comprehension in Python [If you find yourself using a for loop along with append() to create a list, then List Comprehensions are a good alternative!]

mystring='Hello'
newlist=[]
for item in mystring:
    newlist.append(item)
print('Assigning a string to a list:', newlist)

# Alternative way to use for loop in place of append() method for adding a list
alt_list=[item for item in mystring]    # element for element in mystring (this is a variable name)
print('Alternate way to using append() in for loop:', alt_list)


# We can pass a string inside the for loop to assign a list
m_list=[item for item in 'Hello']
print('Another way:',m_list)

# Performing the operations inside the list & use for loop as below
n_list=[item for item in range(1,7)]
print('Using Range inside of for loop:', n_list)

e_list=[num*2 for num in range(1,5)]
print('Doubling each num in range of numbers:', e_list)

even_list=[num for num in range(1,6) if num%2==0]
print('Printing even numbers from the range of numbers:', even_list)

squares_list=[num**2 for num in range(1,6) if num%2==0]
print('Performing squares of the even numbers from the range of numbers:', squares_list)
