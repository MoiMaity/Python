"""
Find the maximum length words in a file.
"""
words = 0
with open("file1.txt", "r") as f:
    for line in f:
        w = line.split()
        words = len(w)
        max_len = len(max(w, key=len))
print(words)
