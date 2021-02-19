###############################################  EXERCISE 1  #################################################


# The Exercise is the following: given the sequence 0 1 1 2 3 5 8 13 21 ... write
# a function that would return the terms of this sequence up to some limit N.
# If you haven't recognized it, that is the Fibonacci sequence, which is defined as
# F(0) = 0, F(1) = 1 and, for any n > 1, F(n) = F(n-1) + F(n-2). This sequence is 
# excellent to test knowledge about recursion.  We use this formula when examining databases
# for patterns, determining resistance points for AI based trading algorithms, and more.
# You basically make a list of numbers, starting at 1, for n + previous fibonacci number.



def fibonacci(N):
    """Return all fibonacci numbers up to N. """
    result = [0]
    next_n = 1
    while next_n <= N:
        result.append(next_n)
        next_n = sum(result[-2:])
    return result
print(fibonacci(0)) # [0]
print(fibonacci(1)) # [0, 1, 1]
print(fibonacci(55)) # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


###############################################  EXERCISE 2  #################################################

# Given the tuple below that represents the Taylor Swift album Reputation, write
# code to print the album details, followed by a listing of all the tracks in the album.
#
# Indent the tracks by a single tab stop when printing them (remember that you can pass
# more than one item to the print function, separating them with a comma).

# reputation = 'Reputation', 'Taylor Swift', 2017, (
#     (1, 'Ready for It?'), (2, 'End Game'), (3, 'I Did Something Bad'), (4, "Don't Blame Me"), 
#     (5, 'Delicate'), (6, 'Look What You Made Me Do'), (7, 'So It Goes'), 
#     (8, 'Gorgeous'), (9, 'Getaway Car'), (10, 'King of My Heart'), 
#     (11, 'Dancing with Our Hands Tied'), (12, 'Dress'), 
#     (13, "This Is Why We Can't Have Nice Things"), (14, 'Call It What You Want'), 
#     (15, "New Year's Day"))
#
#     Then append the last song 16, "All For You" and Add song 17. "I Dont Want to Live Forever"



# print(reputation)
#
# title, artist, year, tracks = reputation
# print(title)
# print(artist)
# print(year)
# for song in tracks:
#     track, title = song
#     print("\tTrack number {}, Title: {}".format(track, title))
#

reputation = "Reputation", "Taylor Swift", 2017, (
    [(1, "Ready for It?"), (2, "End Game"), (3, "I Did Something Bad"), (4, "Don't Blame Me"),
    (5, "Delicate"), (6, "Look What You Made Me Do"), (7, "So It Goes"),
    (8, "Gorgeous"), (9, "Getaway Car"),  (10, "King of My Heart"), (11, "Dancing with Our Hands Tied"),
     (12, "Dress"), (13, "This Is Why We Can't Have Nice Things"),  (14, "Call It What You Want"),
      (15, "New Year's Day")])

print(reputation)

reputation[3].append((16, "All For You"))
print(reputation)

title, artist, year, tracks = reputation
tracks.append((17, "I Don't Want to Live Forever"))
print(title)
print(artist)
print(year)
for song in tracks:
    track, title = song
    print("\tTrack number {}, Title: {}".format(track, title))