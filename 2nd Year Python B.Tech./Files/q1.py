"""
1) Write a file. Read the file and print its content. Read first two lines. Read first 5 characters. Read
the file using loop.
"""

f = open("file1.txt", "r")

print(f.read())

f.seek(0)

print(f.readline())
print(f.readline())

f.seek(0)

print(f.read(5))

f.close()
