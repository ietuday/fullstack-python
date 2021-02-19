#1	list.append(obj)
#Appends object obj to list

#2	list.count(obj)
#Returns count of how many times obj occurs in list

#3	list.extend(seq)
#Appends the contents of seq to list
# https://stackoverflow.com/questions/252703/difference-between-append-vs-extend-list-methods-in-python

#4	list.index(obj)
#Returns the lowest index in list that obj appears

#5	list.insert(index, obj)
#Inserts object obj into list at offset index

#6	list.pop(obj=list[-1])
#Removes and returns last object or obj from list

#7	list.remove(obj)
#Removes object obj from list

#8	list.reverse()
#Reverses objects of list in place

#9	list.sort([func])
#Sorts objects of list, use compare func if given


#1	list.append(obj)
cat_list = ["not eating", "not playing", "on a bed", "is sleeping"]

cat_list.append("A Mongolian Cat")

for state in cat_list:
    print("This cat is " + state)

print(cat_list)    





even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
numbers_in_order = sorted(numbers)

print(numbers)
print(numbers_in_order)

if numbers == numbers_in_order:
    print("The lists are equal")
else:
    print("The lists are not equal")

if numbers_in_order == sorted(numbers):
    print("The lists are equal")
else:
    print("The lists are not equal")


#2	list.count(obj)
aList = [123, 'xyz', 'zara', 'abc', 123]
print ("Count for 123 : ", aList.count(123))
print ("Count for zara : ", aList.count('zara'))

#3	list.extend(seq)
aList = [123, 'xyz', 'zara', 'abc', 123]
bList = [2009, 'manni']
aList.extend(bList)
print("Extended List : ", aList) 

#4	list.index(obj)
aList = [123, 'xyz', 'zara', 'abc', 'xyz']
print("Index for xyz : ", aList.index( 'xyz' )) 
print("Index for zara : ", aList.index( 'zara' )) 

#5	list.insert(index, obj)
aList = [123, 'xyz', 'zara', 'abc']
aList.insert( 3, 2009)
print("Final List : ", aList)

#6	list.pop(obj=list[-1])
aList = [123, 'xyz', 'zara', 'abc']
print("A List : ", aList.pop(1))
print("B List : ", aList.pop(2))
print(aList)
