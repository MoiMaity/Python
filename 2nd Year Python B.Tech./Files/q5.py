"""
Count the number of lines in a file.
"""

f = open("file1.txt", "r")

lines = f.readlines()

print(len(lines))
