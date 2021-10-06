import dodoku.create as create 

def _insert(parms):
    grid = parms['grid']
    rowColNum = parms['cell'].lower()
    rowColSplit = rowColNum.split('c')
    rowNum = int(rowColSplit[0][1:])
    colNum = int(rowColSplit[1])
    status = 'ok'
    
    value = int(parms['value'])
    
    colMajorOrder = create.convertToColMajorOrder(grid)
    if str(value) in colMajorOrder[colNum-1]:
        status = 'warning' 
    
    rows = []
    for i in range(0, 6):
        row = []
        for j in range(0, 9):
            row.append(grid[i*9+j])
        rows.append(row)
    
    for i in range(1):
        row = []
        for j in range(15):
            row.append(grid[54+j])
        rows.append(row)
    
    for i in range(1):
        row = []
        for j in range(15):
            row.append(grid[69+j])
        rows.append(row)
    
    for i in range(1):
        row = []
        for j in range(15):
            row.append(grid[84+j])
        rows.append(row)
    
    for i in range(11, 17):
        row = []
        for j in range(0, 9):
            row.append(grid[i*9+j])
        rows.append(row)
    
    subGraphs = createSubGraphs(rows)
    print(subGraphs)
        
    if rowNum <=9:
        if value in map(abs,rows[rowNum-1]):
            status = 'warning'
        rows[rowNum-1][colNum-1] = value
    else:
        if value in map(abs, rows[rowNum-1]):
            status = 'warning'
        rows[rowNum-1][colNum-7] = value
        
    grid = []
    for row in rows:
        for col in row:
            grid.append(col)
               
    result = {'grid':grid, 'integrity': create.calculateHash(grid), 'status':status}
    return result

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
    print(subGraphs)
    return subGraphs