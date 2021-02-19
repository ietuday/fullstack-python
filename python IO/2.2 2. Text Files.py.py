#######################TEXT---BASIC INPUT OUTPUT ##############################

#Printing takes place in the form of a function

print("This string will be displayed in the output")
# This string will be displayed in the output

print("You can print \n escape characters too.")
# You can print escape characters too.

#Input from a File
#Input can also be read from files. Files can be opened using the 
# built-in function open. Using a with <command> as <name> syntax 
# (called a 'Context Manager') makes using open and getting a handle for the file super easy:

with open('somefile.txt', 'r') as fileobj:

#To open an existing file for reading only use r. If you want to read that file as 
# bytes use rb. To append data to an existing file use a. Use
# w to create a file or overwrite any existing files of the same name. You can use 
# r+ to open a file for both reading and writing. The first argument of open() is the 
# filename, the second is the mode. If mode is left blank, it will default to
#r.

# let's create an example file:
with open('shoppinglist.txt', 'w') as fileobj:
    fileobj.write('tomato\npasta\ngarlic')

with open('shoppinglist.txt', 'r') as fileobj:
# this method makes a list where each line
# of the file is an element in the list
    lines = fileobj.readlines()

print(lines)
# ['tomato\n', 'pasta\n', 'garlic']
with open('shoppinglist.txt', 'r') as fileobj:

# here we read the whole content into one string:
    content = fileobj.read()

# get a list of lines, just like int the previous example:
    lines = content.split('\n')

print(lines)
# ['tomato', 'pasta', 'garlic']


with open('shoppinglist.txt', 'r') as fileobj:
    # this method reads line by line:
    lines = []
    for line in fileobj:
        lines.append(line.strip())


fileobj = open('shoppinglist.txt', 'r')
pos = fileobj.tell()
print('We are at %u.' % pos) # We are at 0.

content = fileobj.read()
end = fileobj.tell()
print('This file was %u characters long.' % end)
# This file was 22 characters long.
fileobj.close()

fileobj = open('shoppinglist.txt', 'r')
fileobj.seek(7)
pos = fileobj.tell()
print('We are at character #%u.' % pos)


# reads the next 4 characters
# starting at the current position
next4 = fileobj.read(4)
# what we got?
print(next4) # ' pas'
# where we are now?
pos = fileobj.tell()
print('We are at %u.' % pos) # We are at 11, as we was at 7, and read 4 chars.
fileobj.close()

#Printing a string without a newline at the end
print("Hello, ", end="\n")
print("World!")

print("Hello, ", end="")
print("World!")
# Hello, World!

print("Hello, ", end="<br>")
print("World!")
# Hello, <br>World!

print("Hello, ", end="newstring")
print("World!")
# Hello, BREAKWorld!



#Displaying text from an imported file

song = open("sample.txt",'r')

with open("C:\\Users\\user\\Desktop\\fullstack\\15. Python Input and Output\\sample.txt", 'r') as song:
    lines = song.readlines()
print(lines)

for line in lines[::-1]:
    print(line, end='')



#CAN be run on pycharm because it asks for user input

import sys

def write():
    print('Creating new text file') 

    name = input('Enter name of text file: ')+'.txt'  # Name of text file coerced with +.txt

    try:
        file = open(name,'a')   # Trying to create a new file or open one
        file.close()

    except:
        print('Something went wrong! Can\'t tell what?')
        sys.exit(0) # quit Python

write()
