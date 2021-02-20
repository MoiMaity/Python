"""
Write a program in Python which converts the case of one file into another.
"""

f1 = open("file1.txt", "r")
f2 = open("file5.txt", "w")
c = f1.read(1)

while c != "":
    if c.lower(): f2.write(c.upper())
    else: f2.write(c.lower())
    c = f1.read(1)

f2.close()
