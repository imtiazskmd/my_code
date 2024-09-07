# let us use if elif and else in the below program
age=5
if age<2:
    print('Infant')
elif age>=2 and age<=10:
    print('Kid')
elif age>10 and age<18:
    print('Minor')
else:
    print('Major')

#Let us use For loop along with if statement to print even numbers from a list
myitem=[1,2,3,4,5,6,7]
print('\nPrinting even numbers from a list:')
for item in myitem:
    if item%2==0:
        print(item)

#let us do sum of numbers in the list by using the same list as above
list_sum=0
for item in myitem:
    list_sum=list_sum+item
print(f'\nSum of the items in list is: {list_sum}')


#Passing tuples in the list and executing in for loop

t_list =[(1,2),(3,4),(5,6),(7,8)]
print("\nTuples are being called inside the list")
for item in t_list:
    print(item)

# Unpacking tuples from a list
print('\nUnpacking tuples from a list:')
for (a,b) in t_list:
    print(a)
    print(b)

# Using dictionaries in for loop
dict={'k1':1,'k2':2,'k3':3}

print('\nPrinting items from a dictionary')
for item in dict.items():
    print(item)

print('\nPrinting keys from a dictionary')
for item in dict.keys():   # instead of dict.keys() we can even write for item in dict:
    print(item)

print('\nPrinting values from a dictionary')
for item in dict.values():
    print(item)

# let us use While loops: it will continue to execute a block of code while some condition remains True.
x=0
print("\nUsing a simple while block:")
while x<5:
    print(f'The current value of x is {x}')
    x=x+1
else:
    print ('Exiting the loop as the value is x is greater than 5')


# Let us use break (breaks out of loop) continue (goes to the top of the closest enclosing loop) and pass (does nothing) keyword to add additional funtionality
# one usage for pass keyword is, incase if you do not write any code/action inside for loop then it will throw an error, instead if we use pass keyword it will do nothing means it does not throw an error.

print('\nAn example of continue keyword:')
mystring='Hello World'
for item in mystring:
    if item=='o':   # the moment item sees o, the below keyword continue will go back to the for loop and skips printing o
        continue
    print(item)

print('\nAn example of break keyword:')
for item in mystring:
    if item=='o':   # the moment item sees o, the below keyword break will prompt to come out of the for loop
        break
    print(item)

#Let us write a program to print each letter of string using for loop

print('\nPrinting each letter of string using loop')
index_count=0
for letter in 'Hello':
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count=index_count+1

#Using enumerate method to count the items & display in the form of Tuples:

print('\nExample of enumerate method:')
word='abcde'
for item in enumerate(word):
    print(item)

print('\nAnother example of enumerate method:')
for index,char in enumerate(word):
    print(index,char)

#using zip method to zip two lists in tuples
print('\nZip method to combine two lists as tuples')
mylist1=[1,2,3,4]
mylist2=['a','b','c','d','e']
mylist3=[10,20,30]
for item in zip(mylist1,mylist2,mylist3):
    print(item)  # zip will only combine the shortest similar items in each list and ignore extra items.


