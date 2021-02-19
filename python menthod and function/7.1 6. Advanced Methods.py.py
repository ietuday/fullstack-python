#User Defined Methods


#instance methods
class Animal:
    #Animal class"""
    def __init__(self, name):
	    #Initialize animal special method
        self.name = name
    def animal_name(self):
	    #Return animal name instance method
        return "This is a {}".format(self.name)

Animal.animal_name #unbound method 
Animal.animal_name()

animal = Animal('dog')
animal.animal_name  #bound method 
animal.animal_name()
Animal.animal_name(Animal('cat')) #new instance


#our example from previous Method Lecture
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




#@staticmethod
#Static methods are a special case of methods. 
# Sometimes, you'll write code that belongs to a class, but that doesn't use the object itself at all.

class Animal:  #Animal class
    def __init__(self, name): # Initialize Animal
        self.name = name
    def animal_name(self):
        return "This is a {}".format(self.name)  #Return animal name  
    @staticmethod
    def message():  #Return message
        return "Love animals!"

Animal.message()
a = Animal('dog')
Animal.message


class Pizza(object):
    @staticmethod
    def mix_ingredients(x, y):
        return x + y

    def cook(self):
        return self.mix_ingredients(self.cheese, self.vegetables)
Pizza().cook is Pizza().cook
Pizza().mix_ingredients is Pizza.mix_ingredients
Pizza().mix_ingredients is Pizza().mix_ingredients


#Class Methods AKA Alternate Constructors
class Animal: #   Animal Class
    animal = 'dog'
    @classmethod
    def change_animal(cls, new_animal):  #Change animal for class
	    return cls.animal == new_animal
    def print_animal(self):  #Return animal
        return self.animal

Animal.animal
Animal.change_animal #<bound method classobj.change_nimal of <class __main__.Animal at 0x7f63aefca9a8>>
Animal.change_animal('bird')
Animal.animal



#User-Defined Methods
class A(object):
    # func: A user-defined function object
    #
    # Note that func is a function object when it's defined,
    # and an unbound method object when it's retrieved.
    def func(self):
        pass
    # classMethod: A class method
    @classmethod
    def classMethod(self):
        pass
class B(object):
    # unboundMeth: A unbound user-defined method object
    #
    # Parent.func is an unbound user-defined method object here,
    # because it's retrieved.
    unboundMeth = A.func

a = A()
b = B()

print(A.func)
# output: <unbound method A.func>
print(a.func)
# output: <bound method A.func of <__main__.A object at 0x10e9ab910>>
print(B.unboundMeth)
# output: <unbound method A.func>
print(b.unboundMeth)
# output: <unbound method A.func>
print(A.classMethod)
# output: <bound method type.classMethod of <class '__main__.A'>>
print a.classMethod
# output: <bound method type.classMethod of <class '__main__.A'>>


import turtle, time, random #tell python we need 3 different modules
turtle.speed(0) #set draw speed to the fastest
turtle.colormode(255) #special colormode
turtle.pensize(4) #size of the lines that will be drawn
def triangle(size): #This is our own function, in the parenthesis is a variable we have defined that
    #will be used in THIS FUNCTION ONLY. This function creates a right triangle
    turtle.forward(size) #to begin this function we go forward, the amount to go forward by is the variable size
    turtle.right(90) #turn right by 90 degree
    turtle.forward(size) #go forward, again with variable
    turtle.right(135) #turn right again
    turtle.forward(size * 1.5) #close the triangle. thanks to the Pythagorean theorem we know that
#this line must be 1.5 times longer than the other two(if they are equal)
while(1): #INFINITE LOOP
    turtle.setpos(random.randint(-200, 200), random.randint(-200, 200)) #set the draw point to a random (x,y) position
    turtle.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
#randomize the RGB color
    triangle(random.randint(5, 55)) #use our function, because it has only one variable we can
        #simply put a value in the parenthesis. The value that will be sent will be random between 5 - 55, end
        #the end it really just changes ow big the triangle is.
    turtle.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))


class Laptop(object):
    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


apple = Laptop("apple", 1400)
print(apple.make)
print(apple.price)

apple.price = 1800
print(apple.price)

vaio = Laptop("vaio", 2150)

print("Models: {} = {}, {} = {}".format(apple.make, apple.price, vaio.make, vaio.price))

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(apple, vaio))

"""
Class: template for creating objects. All objects created using the same class will have the same characteristics.
Object: an instance of a class.
Instantiate: create an instance of a class.
Method: a function defined in a class.
Attribute: a variable bound to an instance of a class.
"""

print(vaio.on)
vaio.switch_on()
print(vaio.on)

Laptop.switch_on(apple)
print(apple.on)
apple.switch_on()

print("*" * 80)

apple.power = 1.5
print (apple.power)
# print(vaio.power)

print("Switch to battery power")
Laptop.power_source = "battery"
print(Laptop.power_source)
print("Switch apple to battery")
apple.power_source = "battery"
print(apple.power_source)
print(vaio.power_source)
print(Laptop.__dict__)
print(apple.__dict__)
print(vaio.__dict__)
