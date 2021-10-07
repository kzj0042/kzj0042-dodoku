import hashlib
import random

def createSubGraphs(rows):
    graph = []
    subGraphs = []
    for i in range(0, 3):
        for j in range(0, 3):
            graph.append(rows[i][j])
    subGraphs.append(graph)
    graph = []
    for i in range(0, 3):
        for j in range(3, 6):
            graph.append(rows[i][j])
    subGraphs.append(graph)
    graph = []
    for i in range(0, 3):
        for j in range(6, 9):
            graph.append(rows[i][j])
    subGraphs.append(graph)
    graph = []
    
    for i in range(3, 6):
        for j in range(0, 3):
            graph.append(rows[i][j])
    subGraphs.append(graph)
    graph = []
    for i in range(3, 6):
        for j in range(3, 6):
            graph.append(rows[i][j])
    subGraphs.append(graph)
    graph = []
    for i in range(3, 6):
        for j in range(6, 9):
            graph.append(rows[i][j])
    subGraphs.append(graph)
    graph = []
    
    graph = []
    
    for i in range(6, 9):
        for j in range(0, 3):
            graph.append(rows[i][j])
    subGraphs.append(graph)
    graph = []
    for i in range(6, 9):
        for j in range(3, 6):
            graph.append(rows[i][j])
    subGraphs.append(graph)
    graph = []
    for i in range(6, 9):
        for j in range(6, 9):
            graph.append(rows[i][j])
    subGraphs.append(graph)
    graph = []
    for i in range(6, 9):
        for j in range(9, 12):
            graph.append(rows[i][j])
    subGraphs.append(graph)
    graph = []
    for i in range(6, 9):
        for j in range(12, 15):
            graph.append(rows[i][j])
    subGraphs.append(graph)
    graph = []
    
    for i in range(9, 12):
        for j in range(0, 3):
            graph.append(rows[i][j])
    subGraphs.append(graph)
    graph = []
    for i in range(9, 12):
        for j in range(3, 6):
            graph.append(rows[i][j])
    subGraphs.append(graph)
    graph = []
    for i in range(9, 12):
        for j in range(6, 9):
            graph.append(rows[i][j])
    subGraphs.append(graph)
    graph = []
    
    
    for i in range(12, 15):
        for j in range(0, 3):
            graph.append(rows[i][j])
    subGraphs.append(graph)
    graph = []
    for i in range(12, 15):
        for j in range(3, 6):
            graph.append(rows[i][j])
    subGraphs.append(graph)
    graph = []
    for i in range(12, 15):
        for j in range(6, 9):
            graph.append(rows[i][j])
    subGraphs.append(graph)
    return subGraphs

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

def calculateHash(grid):  
    stringDictionary = convertToColMajorOrder(grid)
    hashobj = hashlib.sha256(("".join(value for value in stringDictionary.values())).encode())
    return hashobj.hexdigest()
    
def getEightCharactersOfHash(hashobj):
    randomNumber = random.randrange(len(hashobj)-7)  
    return hashobj[randomNumber:randomNumber+8]