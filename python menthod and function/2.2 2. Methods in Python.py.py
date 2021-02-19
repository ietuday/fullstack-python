# #Methods
# 
#  Methods are essentially functions built into objects.   Methods are things that an object can do.
# 
# We will create our own objects and methods using Object Oriented Programming (OOP) and classes.
# 
# Methods will perform specific actions on the object and can also take arguments.  Methods are basically functions


#Usually, a method is called right after it is bound 
#
# 
#     object.method(arg1,arg2,etc...)
#     
#
# 
# Lets take a quick look at what an example of the various methods a list has:

# In[2]:

#instance methods
class Pizza(object):
    def __init__(self, size):
        self.size = size
    def get_size(self):
        return self.size

Pizza.get_size
Pizza.get_size(Pizza(24))
m = Pizza(24).get_size
m()
m.__self__
m == m.__self__.get_size

# CLASS METHODS
# The class is made up of attributes (data) and methods (functions).  
# Python has class methods and static methods – special kinds of methods. Class methods work the same
# way as regular methods, except that when invoked on an object they bind to the class of the object instead of to the
# object. Thus m.__self__ = type(a). When you call such bound method, it passes the class of a as the first
# argument. Static methods are even simpler: they don't bind anything at all, and simply return the underlying
# function without any transformations.

class D(object):
    multiplier = 2
    
    @classmethod
    def f(cls, x):
        return cls.multiplier * x

    @staticmethod
    def g(name):
        print("Hello, %s" % name)

D.f
D.f(12)
D.g
D.g('World')


# Create an object with class methods

class Shape(object):
    # this is an abstract class that is primarily used for inheritance defaults
    # here is where you would define classmethods that can be overridden by inherited classes
    @classmethod
    def from_square(cls, square):
        # return a default instance of cls
        return cls()

class Square(Shape):
    def __init__(self, side=10):
        self.side = side

    @classmethod
    def from_square(cls, square):
        return cls(side=square.side)


class Rectangle(Shape):
    def __init__(self, length=10, width=10):
        self.length = length
        self.width = width

    @classmethod
    def from_square(cls, square):
        return cls(length=square.side, width=square.side)


class RightTriangle(Shape):
    def __init(self, a=10, b=10):
        self.a = a
        self.b = b
        self.c = ((a*a) + (b*b))**(.5)

    @classmethod
    def from_square(cls, square):
        return cls(a=square.length, b=square.width)


class Circle(Shape):
    def __init__(self, radius=10):
        self.radius = radius

    @classmethod
    def from_square(cls, square):
        return cls(radius=square.length/2)

# Create a simple list
l = [1,2,3,4,5]


# Fortunately, with iPython and the Jupyter Notebook we can quickly see all the possible methods using the tab key. The methods for a list are:
# 
# * append
# * count
# * extend
# * insert
# * pop
# * remove
# * reverse
# * sort
# 
# Let's try out a few of them:

# append() allows us to add elements to the end of a list:

# In[3]:


l.append(6)


# In[4]:


l


# Great! Now how about count()? The count() method will count the number of occurrences of an element in a list.

# In[7]:


# Check how many times 2 shows up in the list
l.count(2)


# You can always use Shift+Tab in the Jupyter Notebook to get more help about the method. In general Python you can use the help() function: 

# In[17]:


help(l.count)


# Feel free to play around with the rest of the methods for a list. Later on in this section your quiz will involve using help and Google searching for methods of different types of objects!

# Great! By this lecture you should feel comfortable calling methods of objects in Python!\

#Methods may call other methods by using method attributes of the self argument:

class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
