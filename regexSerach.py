#regex search
# provide the absolute path to the directory
# search the directory of any .txt files
# Open each file
# Search for lines that match the user-supplied regex
# print the matching result
import re
from pathlib import Path

directoryPath = Path('E:\\python\\Automatewithpython')
filePaths = directoryPath.glob('*.txt')
checkRegex = re.compile(input('Enter your Regex expression :'), re.IGNORECASE)
for filePath in filePaths:
    file = open(filePath)
    content = file.read()
    searchedText = checkRegex.search(content)
    #print(searchedText.group())
    if searchedText:
        print(f"Match found in {filePath}: {searchedText.group()}")
    else:
        print(f"No match found in {filePath}")

