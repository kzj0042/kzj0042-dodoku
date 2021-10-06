import dodoku.create as create 

def _insert(parms):
    grid = parms['grid']
    rowColNum = parms['cell'].lower()
    rowColSplit = rowColNum.split('c')
    rowNum = int(rowColSplit[0][1:])
    colNum = int(rowColSplit[1])
    status = 'ok'
    
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
    
    value = int(parms['value'])
    
    if rowNum <=9:
        if value in rows[rowNum-1]:
            status = 'warning'
        rows[rowNum-1][colNum-1] = value
    else:
        if value in rows[rowNum-1]:
            status = 'warning'
        rows[rowNum-1][colNum-7] = value
            
    grid = []
    for row in rows:
        for col in row:
            grid.append(col)
    
    colMajorOrder = create.convertToColMajorOrder(grid)
    if str(value) in colMajorOrder[colNum-1]:
        print(str(value))
        status = 'warning'   
        
    result = {'grid':grid, 'integrity': create.calculateHash(grid), 'status':status}
    return result
