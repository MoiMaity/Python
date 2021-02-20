"""
Check whether a file exists or not. Delete it.
"""

import os

if os.path.exists("file2.txt"):
    os.remove("file2.txt")

else:
    print("the file does not exist.")
