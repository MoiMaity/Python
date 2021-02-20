"""
Print the words written in the first line of a file. Access each word using a loop.
"""

f = open("file1.txt",'r')

words = f.readline().split()

for word in words:
    print(word)
