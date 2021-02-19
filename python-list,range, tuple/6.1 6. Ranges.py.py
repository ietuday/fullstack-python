# Experiment with different ranges and slices to get a feel for how they work.
# Remember that you can print the range as well as iterating through it to print
# its values, to check that your ranges are what you expected.
# You may also want to include things like.
# https://www.pythoncentral.io/pythons-range-function-explained/
o = range(0, 100, 4)
print(o)
p = o[::2]
print(p)
for i in p:
    print(i)

# and see if you can work out what will be printed before running the program. If you are unsure, use a
# for loop to print out the values of o to see why p returns what it does.

# Sometimes we need to iterate over a range of numbers, and it would be quite
# unpleasant to have to do so by hardcoding the list somewhere. In such cases,
# the range function comes to the rescue. Let's see the equivalent of the previous
# snippet of code:

for number in range(5):
    print(number)

# The range function is used extensively in Python programs when it comes to creating
# sequences: you can call it by passing one value, which acts as stop (counting from 0),
# or you can pass two values (start and stop), or even three (start, stop, and step).
# Check out the following example:
list(range(10)) # one value: from 0 to value (excluded)

list(range(3, 8)) # two values: from start to stop (excluded)

list(range(-20, 20, 4)) # three values: step is added

list(range(20, -20, -4)) # three values: step is added



# Nested Comprehensions : very common when dealing with algorithms
# to have to iterate on a sequence using two placeholders. The first one runs through
# the whole sequence, left to right. The second one as well, but it starts from the first
# one, instead of 0. The concept is that of testing all pairs without duplication. Let's see
# the classical for loop equivalent.

items = 'ABCDE'
pairs = []
for a in range(len(items)):
    for b in range(a, len(items)):
        pairs.append((items[a], items[b]))
print(pairs)

#Same output but Nested Comprehensions
items = 'ABCDE'
pairs = [(items[a], items[b])
    for a in range(len(items)) for b in range(a, len(items))]
print(pairs)




#Write a Python function to check whether a number is in a given range.


def test_range(n):
    if n in range(3,9):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
test_range(6)