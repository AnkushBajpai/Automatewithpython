"""
Filling in the Gaps
Write a program that finds all files with a given prefix, 
such as spam001.txt, spam002.txt, and so on, in a single folder and locates any gaps in the numbering 
(such as if there is a spam001.txt and spam003.txt but no spam002.txt). 
Have the program rename all the later files to close this gap.

As an added challenge, write another program that can insert gaps into numbered files so that a new file can be added.
"""

import re, os
import shutil

filePattern = r"^(spam)(\d{3})(\.txt)$$"

folderToCheck = 'E:\\python\\Automatewithpython\\filesForFillingInTheGaps'
count = 1

# The below code chunch is to name the file from 1 to n, and remove all the gaps from the file names

for filename in os.listdir(folderToCheck):
    #print(filenames)
    file = re.match(filePattern, filename)
    print(file)
    max_length  = len(file.group(1)+file.group(2))
    print(file.group(2))
    if count != int(file.group(2)):
        newFileName = file.group(1) + '0'*(max_length-len(str(file.group(1))+str(count))) + str(count) + file.group(3)
        print(newFileName)
        print(f'filename changed from {filename} to {newFileName}\n')
        shutil.move(os.path.join(folderToCheck,filename), os.path.join(folderToCheck,newFileName))
    count = count + 1



# below code is to add the gap in the file names in ord3er to accomodate one more file

"""
for filename in os.listdir(folderToCheck):
    #print(filename)
    file = re.match(filePattern, filename)
    if file:
        count = count + 1

filename = f'spam00{count-1}.txt'
newFileName = f'spam00{count}.txt'
print(f'filename changed from {filename} to {newFileName}\n')
shutil.move(os.path.join(folderToCheck,filename), os.path.join(folderToCheck,newFileName))
"""