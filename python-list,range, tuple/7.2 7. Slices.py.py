# Indexing and slicing lists, ranges and tuples
# When manipulating sequences, it's very common to have to access them at one
# precise position (indexing), or to get a subsequence out of them (slicing). When
# dealing with immutable sequences, both operations are read-only.
# While indexing comes in one form, a zero-based access to any position within the
# sequence, slicing comes in different forms. When you get a slice of a sequence, you
# can specify the start and stop positions, and the step. They are separated with a
# colon (:) like this: my_sequence[start:stop:step]. All the arguments are optional,
# start is inclusive, stop is exclusive. It's


a[start:end] # items start through end-1
a[start:]    # items start through the rest of the array
a[:end]      # items from the beginning through end-1
a[:]         # a copy of the whole array

a[start:end:step] # start through not past end, by step

a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items

a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed




# Lists allow to use slice notation as lst[start:end:step]. The output of the slice notation is a new list containing
# elements from index start to end-1. If options are omitted start defaults to beginning of list, end to end of list and
# step to 1:


lst = [1, 2, 3, 4]
lst[1:] # [2, 3, 4]
lst[:3] # [1, 2, 3]
lst[::2] # [1, 3]
lst[::-1] # [4, 3, 2, 1]
lst[-1:0:-1] # [4, 3, 2]
lst[5:8] # [] since starting index is greater than length of lst, returns empty list
lst[1:10] # [2, 3, 4] same as omitting ending index



# Element deletion – it is possible to delete multiple elements in the list using the del keyword and slice
# notation:
lyst = ['a', 'b', 'c', 'd' , 'e']
a= lyst
print(a)
del a[::4]
print(a)


#Advanced slicing
#When lists are sliced the __getitem__() method of the list object is called, 
#with a slice object. Python has a built-in
#slice method to generate slice objects. We can use this to store a slice and 
#reuse it later like so,

data = 'Eden Hazard 24 2018' #assuming data fields of fixed length
name_slice = slice(0,11)
age_slice = slice(12,14)
year_slice = slice(15,None)
#now we can have more readable slices
print(data[name_slice]) #Eden  Hazard
print(data[age_slice]) #'21'
print(data[year_slice]) #'2018'


L[::-1]


a = range(3)
a

a[1:3] = [4, 5, 6]
a

my_list = list(range(10))
print(my_list)

even = list(range(0, 1000, 2))
odd = list(range(1, 1000, 2))

print(even)
print(odd)

my_string = "abcdefghijklmnopqrstuvwxyz"
print(my_string.index('e'))
print(my_string[4])

small_decimals = range(0, 10)
print(small_decimals)
my_range = small_decimals[::2]
print(my_range)

print(small_decimals.index(3))

odd = range(1, 10000, 2)
print(odd)

print(odd[985])



print(small_decimals)

my_range = small_decimals[::2]
print(my_range)
print(my_range.index(4))
decimals = range(0, 100)
print(decimals)

my_range = decimals[3:40:3]
print(my_range)

for i in my_range:
    print(i)

print('=' * 40)

for i in range(3, 40, 3):
    print(i)

print(my_range == range(3, 40, 3))


#islice – slicing any iterable
#When working with the itertools functions, you might notice that you cannot
#slice these objects. That is because they are generators.  Luckily, the
#itertools library has a function for slicing these objects as well—islice.
#Let's take itertools.counter from before as an example:


import itertools
def gen():
    n = 1
    while n < 1000:
        n += n
        yield n
for part in itertools.islice(gen(), 8):
    print(part)

# Note that like a regular slice, you can also use start, stop and step arguments:
# itertools.islice(iterable, 1, 30, 3)