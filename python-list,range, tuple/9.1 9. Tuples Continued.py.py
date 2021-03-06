###########TUPPLES NOTES#######################################################################
###############################################################################################

# A tuple is a immutable list of values. Tuples are one of Python's simplest and most common 
# collection types, and can be created with the comma operator (value = 1, 2, 3).
t = "a", "b", "c"
print(t)
type(t)
t = ("a", "b", "c")
print(t)
type(t)
print("a", "b", "c")
print(("a", "b", "c"))
print(t)

# A comma is needed also if you use parentheses
a = (1,) # a is the tuple (1,)
type(a)
a = (1) # a is the value 1 and not a tuple
type(a)

#tupples are indexed
t = ('a', 'b', 'c', 'd', 'e')
t0 = ()
t[3]

t = tuple('TUPLES')
print(t)
t = tuple(range(3))
print(t)

# Tuples are immutable
# One of the main differences between lists and tuples in Python is that tuples are immutable, that is, one cannot
# add or modify items once the tuple is initialized. For example look at this ERROR CODE:
t = (1, 4, 9)
t[0] = 2  

# Similarly, tuples don't have .append and .extend methods as list does. Using += is possible, but it changes the
# binding of the variable, and not the tuple itself:

# Tuples are immutable
# One of the main differences between lists and tuples in Python is that tuples are immutable, that is, one cannot
# add or modify items once the tuple is initialized. For example:
t = (1, 4, 9)
t[0] = 2

# Similarly, tuples don't have .append and .extend methods as list does. Using += is possible, but it changes the
# binding of the variable, and not the tuple itself:

t = (1, 2)
q = t
t += (3, 4)
t
q

#you can unpack multiple tuples together
t,q

#Be careful when placing mutable objects, such as lists, inside tuples. 
# This may lead to very confusing outcomes when changing them. For example:

t = (1, 2, 3, [1, 2, 3])
print(t)

t[3] += [4, 5]

################################Built-in Tuple Functions####################################

#Length
#finds the length of your tupple
tuple1 = ('a', 'b', 'c', 'd', 'e')
tuple2 = ('1','2','3')
tuple3 = ('5', 'b', 'c', 'd', '1')
len(tuple1)

#Maximum value
#Finds the max value within a tupple
max(tuple1)
max(tuple2)
max(tuple3)

#Minumum
min(tuple1)
min(tuple2)
min(tuple3)

#Convert a list into tuple
#The built-in function tuple converts a list into a tuple.
list = [1,2,3,4,5]
tuple(list)

#Slicing tupples
tuple1 = ('a', 'b', 'c', 'd', 'e')
tuple2 = ('1','2','3')
tuple3 = ('5', 'b', 'c', 'd', '1')
tuple1[1:3]
tuple2[1:2]
tuple3[4:1:-1]

#reverse
#you can reverse the elements in the tuple. Gives an iterable abject which is converted to a tupple
colors = "red", "green", "blue"
rev = colors[::-1]
print(colors)

colors = rev
print(colors)
rev = tuple(reversed(colors))
print(rev)


# Hashing is the process of converting some large amount of data into 
# a much smaller amount (typically a single integer) in a repeatable 
# way so that it can be looked up in a table in constant-time (O(1)), 
# which is important for high-performance algorithms and data structures.
# An object is hashable if it has a hash value which never changes during its lifetime 
# (it needs a __hash__() method), and can be compared to other objects 
# (it needs an __eq__() or __cmp__() method). Hashable objects which compare equal 
# must have the same hash value.

#Hashability makes an object usable as a dictionary key and a set member, 
#because these data structures use the hash value internally.

#All of Python’s immutable built-in objects are hashable, 
#while no mutable containers (such as lists or dictionaries) are. Objects 
#which are instances of user-defined classes are hashable by default; they 
#all compare unequal, and their hash value is their id().

hash( (1, 2) ) # ok
hash( (1, 3) ) # ok

a, b = 1, 2
c = a # we need three lines and a temporary var c
a = b
b = c
a, b # a and b have been swapped
type(a)


#Tuples and Dictionaries - Tuples can be used as keys for dictionaries (we'll see
#this shortly). The dict objects need keys to be immutable because if they could
#change, then the value they reference wouldn't be found any more (because the
#path to it depends on the key). 