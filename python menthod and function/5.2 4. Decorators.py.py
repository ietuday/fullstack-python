######################## Decorator #################################
 
# Decorator functions are software design patterns. They dynamically alter the functionality of a function, method, or
# class without having to directly use subclasses or change the source code of the decorated function. When used
# correctly, decorators can become powerful tools in the development process. This topic covers implementation and
# applications of decorator functions in Python.


# This simplest decorator does nothing to the function being decorated. Such
# minimal decorators can occasionally be used as a kind of code markers.
def super_secret_function(f):
    return f
@super_secret_function    #  <--- is the same as ---->  my_function = super_secret_function(my_function)
def my_function():
    print("This is my secret function.")

#It is important to bear this in mind in order to understand how the decorators work. This "unsugared" syntax makes
#it clear why the decorator function takes a function as an argument, and why it should return another function. It
#also demonstrates what would happen if you don't return a function


#This is the decorator
def print_args(func):
    def inner_func(*args, **kwargs):
        print(args)
        print(kwargs)
        return func(*args, **kwargs) #Call the original function with its arguments

    return inner_func
@print_args
def multiply(num_a, num_b):
    return num_a * num_b
print(multiply(3, 5))
#Output:
# (3,5) - This is actually the 'args' that the function receives.
# {} - This is the 'kwargs', empty because we didn't specify keyword arguments.
# 15 - The result of the function.


#Decorator class          

class Decorator(object):
    """Simple decorator class."""

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Before the function call.')  
        res = self.func(*args, **kwargs)
        print('After the function call.')
        return res

@Decorator
def testfunc():
    print('Inside the function.')

testfunc()
# Before the function call.
# Inside the function.
# After the function call.


#Decorator with arguments
def decoratorfactory(message):
    def decorator(func):
        def wrapped_func(*args, **kwargs):
            print('The decorator wants to tell you: {}'.format(message))
            return func(*args, **kwargs)
        return wrapped_func
    return decorator
@decoratorfactory('Hello World')
def test():
    pass
test()


#Chain of function decorators
def make_bold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def make_italic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

def make_underline(fn):
    def wrapped():
        return "<u>" + fn() + "</u>"
    return wrapped
@make_bold
@make_italic
@make_underline
def hello():
    return "hello world"
print(hello()) ## returns "<b><i><u>hello world</u></i></b>"










































import sys


def my_range(n: int):
    print("my_range starts")
    start = 0
    while start < n:
        print("my_range is returning {}".format(start))
        yield start
        start += 1

big_range = range(5)
# big_range = my_range(5)
# _ = input("line 14")

print("big_range is {} bytes".format(sys.getsizeof(big_range)))

# create a list containing all the values in big_range
big_list = []

# _ = input("line 22")
for val in big_range:
    #    _ = input("line 24 - inside loop")
    big_list.append(val)

print("big_list is {} bytes".format(sys.getsizeof(big_list)))
print(big_range)
print(big_list)

print("looping again ... or not")
for i in big_range:
    print("i is {}".format(i))
