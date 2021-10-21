"""
    Created on October 21, 2021
    
    @author: Kyle Julien
"""
def convertToColMajorOrder(grid):
    if not isinstance(grid, list):
        grid = grid.replace('[', '')
        grid = grid.replace(']', '')
        grid = grid.split(',')
        grid = list(map(int, grid))
        
    stringDictionary = {new_list: "" for new_list in range(15)}
    j=0
    i=0
    while i<54:
        stringDictionary[j]+=str(grid[i])
        j+=1
        i+=1
        if j==9:
            j=0
    j=0
    while i<93:
        stringDictionary[j]+=str(grid[i])
        j+=1
        i+=1
        if i == 63:
            i=69
        elif i == 78:
            i=84
        if j==9:
            j=0
    i=99
    j=6
    while i<147:
        stringDictionary[j]+=str(grid[i])
        i+=1
        j+=1
        if i%3 == 0:
            i+=6
        if j == 9:
            j=6
    i=63
    j=9
    while i<99:
        stringDictionary[j]+=str(grid[i])
        i+=1
        j+=1
        if i == 69:
            i=78
        elif i == 84:
            i=93
        if j==15:
            j=9
    i=102
    j=9
    while i<153:
        stringDictionary[j]+=str(grid[i])
        i+=1
        j+=1
        if i==108:
            i=111
        elif i==117:
            i=120
        elif i==126:
            i=129
        elif i==135:
            i=138
        elif i==144:
            i=147
        if j==15:
            j=9
    return stringDictionary

def convertToColMajorOrderList(grid):
    rows = []
    for i in range(0, 17):
        row = []
        if i<6 or i>=11:
            for j in range(0, 9):
                row.append(grid[i*9+j])
            rows.append(row)
        elif i==6:
            for j in range(15):
                row.append(grid[54+j])
            rows.append(row)   
        elif i==7:
            for j in range(15):
                row.append(grid[69+j])
            rows.append(row)                     
        elif i==8:
            for j in range(15):
                row.append(grid[84+j])
            rows.append(row)  
    return rows

def convertToRowMajorOrder(rows):
    grid = []
    for row in rows:
        for col in row:
            grid.append(col)
    return grid  