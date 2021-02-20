"""
Write a program in Python to merge the content of two files (one after another).
"""

f1 = open("file1.txt", "r")
f2 = open("file3.txt", "r")
f3 = open("file6.txt", "w")

f3.write(f1.read())
f3.write("\n")
f3.write(f2.read())
