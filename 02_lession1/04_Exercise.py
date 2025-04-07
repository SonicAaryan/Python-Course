# Write a py pg to print the contents of a dir using the os module. search online for the function which does that.

import os

# Specify the directory path
directory_path = '.'  # Current directory

# List all entries in the specified directory
entries = os.listdir(directory_path)

# Print each entry
for entry in entries:
    print(entry)
