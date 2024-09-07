#Example of *args
def arg_func(*args):
    return sum(args)*0.05
print(arg_func(10,20,30))   # *args is passed in the function parameter so we can pass any number of arguments while calling the function as per the need.


