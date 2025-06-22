"""
Selective Copy
Write a program that walks through a folder tree and searches for files with a certain file extension (such as .pdf or .jpg). 
Copy these files from whatever location they are in to a new folder.
"""
from pathlib import Path
import os,re,shutil

folderToWalkThrough = 'E:\\python\\Automatewithpython\\automate_online-materials'
filePattern = re.compile(r'.[pdf|jpg]$')                                                  #reegex for the pdfg and jpg files

newFileName = input("Please enter the new file name:  ")
Path(f'E:\\python\\Automatewithpython\\{newFileName}').mkdir()                            # new file creation 
newFilePath = f'E:\\python\\Automatewithpython\\{newFileName}'

print(f"\n Started moving the files in {newFilePath}")

for foldername, subfolders, filenames in os.walk(folderToWalkThrough):                    # ppulating the new folder
    for fileName in filenames:
        found = filePattern.search(fileName)

        if found == None:
            continue
        filepath = os.path.join(os.path.abspath(foldername), fileName)
        shutil.copy(filepath,newFilePath)
        print(f'Copied {filepath} to {newFilePath}')
print("\n Copy is completed!")