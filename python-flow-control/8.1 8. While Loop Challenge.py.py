# Create a the program that will allow you as many guesses to pick 
# a number between 1 and 1000. 
# Use a while loop to
# allow as many guesses as necessary.
# Lookup "import random" and use that to generate the number.
# http://www.pythonforbeginners.com/random/how-to-use-the-random-module-in-python
# https://docs.python.org/2/library/random.html
# The program should let the player know whether to
# guess higher or lower, and should print a message
# when the guess is correct. A correct guess will
# terminate the program.
#
# As an optional extra, allow the player to quit by entering
# 0 (zero) for their guess. 

import random

highest = 1000
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))
guess = 0   # initialize to any number outside of the valid range
while guess != answer:
    guess = int(input())
    if guess == 0:
        break
    if guess < answer:
        print("Please guess higher")
    elif guess > answer:  # guess must be greater than number
        print("Please guess lower")
    else:
        print("Well done, you guessed it")