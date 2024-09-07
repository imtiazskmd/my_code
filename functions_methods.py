# creating a function using def keyword if takes snake casing (lowercase and underscores between the words)
print('\nPassing Hello Jose & calling a function:')
def my_first_function(name):
    print('Hello',name)
my_first_function('Jose')

# Let us use return keyword to send back the result to the function instead of just printing it.
print('\nUsing return keyword to assign the outcome to a variable:')
def my_function(num1,num2):
    return (num1*num2)
result=my_function(2,4)    # return keyword helps to assign the action to a variable which can be called
print(result)


# We can also pass an argument while creating a function so as to avoid an error when you forget to pass an argument while calling a function
print('\nPassing an argument while creating a function:')
def say_hello(name='John'):
    print(f'Hello {name}')
say_hello()


#Logic with Python functions
print('\nReturn True if the number in even:')
def check_even(num):
    return num%2==0
print(check_even(5))

# Return all even numbers in the list using for loop
print('\nPrinting even numbers from the list:')
def even_list(my_list):
    even_num=[]
    for num in my_list:
        if num%2==0:
            even_num.append(num)
        else:
            pass
    return even_num
print(even_list([1,2,3,4,5]))

