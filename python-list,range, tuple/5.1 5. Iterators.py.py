# Iterable: An object is said to be iterable if it's capable of returning its
# members one at a time, such as lists, tuples strings or dictionaries.
# objects that define either of __iter__ or __getitem__ methods are also
# iterables.

# Iterator: An object is said to be an iterator if it represents a stream of data. A
# custom iterator is required to provide an implementation for __iter__ that
# returns the object itself, and an implementation for __next__, which returns
# the next item of the data stream until the stream is exhausted, at which point
# all successive calls to __next__ simply raise the StopIteration exception.
# Built-in functions such as iter and next are mapped to call __iter__ and
# __next__ on an object, behind the scenes

#lets print out the names and ages of everyone on this list together, in order
people = ['Jonas', 'Julio', 'Mike', 'Paul']
ages = [25, 30, 31, 39]
for position in range(len(people)):
    person = people[position]
    age = ages[position]
    print(person, age)


#Previous code was inefficient and not pythonic.  So this is Pythonic and efficient!
people = ['Jonas', 'Julio', 'Mike', 'Paul']
ages = [25, 30, 31, 39]
for person, age in zip(people, ages):
    print(person, age)

#In the follwing code, we added the nationalities
people = ['Jonas', 'Julio', 'Mike', 'Paul']
ages = [25, 30, 31, 39]
nationalities = ['Belgium', 'Spain', 'England', 'Bangladesh']
for person, age, nationality in zip(people, ages, nationalities):
    print(person, age, nationality)



# itertools module.
# instead of newline, comma and space
# infinite iterator
from itertools import count
for n in count(5, 3):
    if n > 20:
        break
    print(n, end=', ')



my_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

my_iterator = iter(my_list)

for i in range(0, len(my_list)):
    next_item = next(my_iterator)
    print(next_item)

for i in my_list:
    print(i)
