"""
Blank Row Inserter
Create a program blankRowInserter.py that takes two integers and a filename string as command line arguments. 
Let’s call the first integer N and the second integer M. 
Starting at row N, the program should insert M blank rows into the spreadsheet.
For example, when the program is run like this:
python blankRowInserter.py 3 2 myProduce.xlsx
"""

import sys, openpyxl

# Check if the script was called with the correct argument
if len(sys.argv) != 4:
    print("Usage: py blankRowInserter.py <insert_at> <num_rows> <file_to_edit>")
    sys.exit(1)

#get details from the command line
file_to_edit = sys.argv[3]
insert_at = int(sys.argv[1])
row_num = int(sys.argv[2])

#load the workbook
workbook = openpyxl.load_workbook(file_to_edit)
ws = workbook.active

#inserting the blank rows
ws.insert_rows(insert_at,row_num)

#save the file with changes
workbook.save(file_to_edit)