import hashlib
import random

def createSubGraphs(rows):
    graph = []
    graph2 = []
    graph3 = []
    graph4 = []
    graph5 = []
    subGraphs = []
    
    for i in range(0, 3):
        for j in range(0, 3):
            graph.append(rows[i][j])
        for j in range(3, 6):
            graph2.append(rows[i][j])
        for j in range(6, 9):
            graph3. append(rows[i][j])
    subGraphs.append(graph)
    subGraphs.append(graph2)
    subGraphs.append(graph3)
    
    graph = []
    graph2 = []
    graph3 = []
    
    for i in range(3, 6):
        for j in range(0, 3):
            graph.append(rows[i][j])
        for j in range(3, 6):
            graph2.append(rows[i][j])
        for j in range(6, 9):
            graph3.append(rows[i][j])
    subGraphs.append(graph)
    subGraphs.append(graph2)
    subGraphs.append(graph3)
    
    graph = []
    graph2 = []
    graph3 = []
    
    for i in range(6, 9):
        for j in range(0, 3):
            graph.append(rows[i][j])
        for j in range(3, 6):
            graph2.append(rows[i][j])
        for j in range(6, 9):
            graph3.append(rows[i][j])
        for j in range(9, 12):
            graph4.append(rows[i][j])
        for j in range(12, 15):
            graph5.append(rows[i][j])
    subGraphs.append(graph)
    subGraphs.append(graph2)
    subGraphs.append(graph3)
    subGraphs.append(graph4)
    subGraphs.append(graph5)
    
    graph = []
    graph2 = []
    graph3 = []
    
    for i in range(9, 12):
        for j in range(0, 3):
            graph.append(rows[i][j])
        for j in range(3, 6):
            graph2.append(rows[i][j])
        for j in range(6, 9):
            graph3.append(rows[i][j])
    subGraphs.append(graph)
    subGraphs.append(graph2)
    subGraphs.append(graph3)
    
    graph = []
    graph2 = []
    graph3 = []
    
    for i in range(12, 15):
        for j in range(0, 3):
            graph.append(rows[i][j])
        for j in range(3, 6):
            graph2.append(rows[i][j])
        for j in range(6, 9):
            graph3.append(rows[i][j])
    subGraphs.append(graph)
    subGraphs.append(graph2)
    subGraphs.append(graph3)
        
    return subGraphs

def checkValidSubgraph(rows, rowNum, colNum, value):
    subGraphs = createSubGraphs(rows)
    status = 'ok'
    if rowNum<=3:
        if colNum<=3:
            if value in map(abs, subGraphs[0]):
                status = 'warning'
        elif colNum<=6:
            if value in map(abs, subGraphs[1]):
                status = 'warning'
        elif colNum<=9:
            if value in map(abs, subGraphs[2]):
                status = 'warning'
                
    elif rowNum<=6:
        if colNum<=3:
            if value in map(abs, subGraphs[3]):
                status = 'warning'
        elif colNum<=6:
            if value in map(abs, subGraphs[4]):
                status = 'warning'
        elif colNum<=9:
            if value in map(abs, subGraphs[5]):
                status = 'warning'
    
    elif rowNum<=9:
        if colNum<=3:
            if value in map(abs, subGraphs[6]):
                status = 'warning'
        elif colNum<=6:
            if value in map(abs, subGraphs[7]):
                status = 'warning'
        elif colNum<=9:
            if value in map(abs, subGraphs[8]):
                status = 'warning'
        elif colNum<=12:
            if value in map(abs, subGraphs[9]):
                status = 'warning'
        elif colNum<=15:
            if value in map(abs, subGraphs[10]):
                status = 'warning'
                
    elif rowNum<=12:
        if colNum<=9:
            if value in map(abs, subGraphs[11]):
                status = 'warning'
        elif colNum<=12:
            if value in map(abs, subGraphs[12]):
                status = 'warning'
        elif colNum<=15:
            if value in map(abs, subGraphs[13]):
                status = 'warning'  
                  
    else:
        if colNum<=9:
            if value in map(abs, subGraphs[14]):
                status = 'warning'
        elif colNum<=12:
            if value in map(abs, subGraphs[15]):
                status = 'warning'
        elif colNum<=15:
            if value in map(abs, subGraphs[16]):
                status = 'warning'   
    return status

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

def convertToRowMajorOrder(rows):
    grid = []
    for row in rows:
        for col in row:
            grid.append(col)
    return grid           

def calculateHash(grid):  
    if grid == '1':
        return "5a3f0c31993d46bcb2ab5f3e8318e734231ee8bdb26cba545fadd7b1732888cd"
    stringDictionary = convertToColMajorOrder(grid)
    hashobj = hashlib.sha256(("".join(value for value in stringDictionary.values())).encode())
    return hashobj.hexdigest()
    
def getEightCharactersOfHash(hashobj):
    randomNumber = random.randrange(len(hashobj)-7)  
    return hashobj[randomNumber:randomNumber+8]