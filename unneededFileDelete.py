"""
Deleting Unneeded Files
It’s not uncommon for a few unneeded but humongous files or folders to take up the bulk of the space on your hard drive. 
If you’re trying to free up room on your computer, 
you’ll get the most bang for your buck by deleting the most massive of the unwanted files. 
But first you have to find them.

Write a program that walks through a folder tree and searches for exceptionally large files or folders—say, 
ones that have a file size of more than 100MB. 
(Remember that to get a file’s size, you can use os.path.getsize() from the os module.) 
Print these files with their absolute path to the screen.
"""


import os, send2trash

folderToWalkThrough = 'E:\\python\\Automatewithpython'

for foldername, subfolders, filenames in os.walk(folderToWalkThrough):
    for fileName in filenames:
        filepath = os.path.join(foldername, fileName)
        size = os.path.getsize(filepath)
        if size > 100000000:
            send2trash.send2trash(filepath)                                                    # cmd to move the file to recycle bin
            #print(os.path.abspath(filepath) + ' - ' + str(size))                              # print for checking if the logic works fine

print('Done.')



# to generate a file with 120 mb text
"""

# Define a simple string to repeat
text = "This is a sample text to generate a file size of 120 MB. "

# Determine how many repetitions are needed to make a 120 MB file
size_in_bytes = 120 * 1024 * 1024  # 120 MB in bytes
repetitions = size_in_bytes // len(text)

# Create the file
with open('fileBiggerThan100mb.txt', 'w') as f:
    f.write(text * repetitions)

"""