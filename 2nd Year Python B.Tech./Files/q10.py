"""
Write a program in Python to copy the content of one file into another character by character.
"""

f1 = open("file1.txt", "r")
f2 = open("file4.txt", "w")
c = f1.read(1)

while c != "":
    f2.write(c)
    c = f1.read(1)

f2.close()
    
