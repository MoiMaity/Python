"""
Count the number of words in a file.
"""

f = open("file1.txt", "r")

words = f.read().split()

print(len(words))
