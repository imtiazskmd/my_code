#Lambda Expressions, Map & Filter functions
#Lambda expressions are used to create small (one expression) functions without a name.

def square(num):
    return num**2
num=[1,2,3,4,5]
for item in map(square,num):    # map applies every number of the list (num) to the function which it being called explicitly and passing value
    print(item)


print("\nAnother example of Maps:")
def splicer(mystring):
    if len(mystring)%2==0:
        return 'EVEN'
    else:
        return mystring[0]
mylist=['Mary','Lilly','Joy']
for item in map(splicer,mylist):
    print(item)

#Usage of Filter
print("\nExample of Filter:")
def check_even(num):
    return num%2==0
mynums=[1,2,3,4,5,6]
print(list(filter(check_even,mynums)))  #use list to transform the filter from memory to list OR use a for loop

#usage of Filter
print("\nAnother example of filter using for loop:")
def check_odd(num):
    return num%2!=0
odd_num=[1,2,3,4,5,6]
for item in filter(check_odd,odd_num):
    print(item)


#Example of Lambda Expression
print("\nExample of Lambda Expression:")
# we can combine 2 lines into one expression in Python as below
# def sqr(num): return num**2
# So the simplest expression to run this is lambda expression
sqr=lambda num:num**2
print(sqr(3))

print("\nAnother example of Lambda expression using maps:")
my_num=[1,2,3,4,5,6]
print(list(map((lambda num:num**2),my_num)))

print("\nAnother example of Lambda using filter:")
print(list(filter((lambda num:num%2==0),my_num)))




