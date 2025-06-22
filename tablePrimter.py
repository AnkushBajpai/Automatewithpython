"""
program to print tableData as
   apples Alice  dogs
  oranges   Bob  cats
 cherries Carol moose
   banana David goose
"""

def printTable(tableData):
    # to get the column width for each column
    colwidth = [0] * len(tableData)            
    for row in range(len(tableData)):
        for item in tableData[row]:
            if colwidth[row] < len(item):
                colwidth[row]=len(item)
    
    # printing the table in the requested format
    '''method 1:
    for col in range(len(tableData[0])):
        print(tableData[0][col].rjust(colwidth[0]),end=' ')
        print(tableData[1][col].rjust(colwidth[1]),end=' ')
        print(tableData[2][col].rjust(colwidth[2]),end=' ')
        print()
    '''

    # method 2 : -- here we are roating the list we were having while printing it
    for col in range(len(tableData[0])):
        for row in range(len(tableData)):
            print(tableData[row][col].rjust(colwidth[row]),end=' ')
        print()




tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)