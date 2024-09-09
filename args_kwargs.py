#Example of *args
def arg_func(*args):
    return sum(args)*0.05
print(arg_func(10,20,30))   # *args is passed in the function parameter so we can pass any number of arguments while calling the function as per the need.

#Another example of *args
print("\nAnother example of *args:")
def arg_fun(*mywish):   #You can give any name to arg but it should start with *
    for item in mywish:
        print(item)
arg_fun(10,20,30)

#Example of **kwargs [keyword arguments]. This will create dictionary of key value pairs
print("\n Example of **Kwargs:")
def kwarg_func(**kwargs):
    print(kwargs)   #This prints the dictionary that we have passed while calling the function
    if 'fruit' in kwargs:
        print ("My fruit of choice is {}".format(kwargs['fruit']))
    else:
        print ("I did not find any fruit here")
print(kwarg_func(fruit='Apple',veggie='cabbage'))


#Example of *args & **kwargs together
print("\nUsing *args & *kwards together:")
def my_combfunc(*args,**kwargs):
    print (f"These are args",args)
    print (f"These are kwargs",kwargs)
    print ("I would like {} {}".format(args[0],kwargs['food']))
print(my_combfunc(10,20,30, fruit='Orange',food='Eggs', Animal='Dog'))


