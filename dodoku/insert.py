import dodoku.utilities as utilities

def _insert(parms):
    if 'cell' not in parms:
        result = {'status':'error: missing cell reference'}
        return result

    if 'grid' not in parms:
        result = {'status':'error: invalid grid'}
        
    if 'integrity' not in parms:
        result = {'status':'error: integrity mismatch'}

    grid = parms['grid']
    
    if not isinstance(grid, list):
        grid = grid.replace('[', '')
        grid = grid.replace(']', '')
        grid = grid.split(',')
        try:
            grid = list(map(int, grid))
        except ValueError:
            result = {'status':'error: invalid grid'}
            return result             
        
    if not all(isinstance(value, int) for value in grid):
        result = {'status':'error: invalid grid'}
        return result
                   
    integrity = parms['integrity'].replace("'", "")
      
    if str(integrity) not in str(utilities.calculateHash(grid)):
        result = {'status':'error: integrity mismatch'}
        return result
    
    rowColNum = parms['cell'].lower()
    rowColSplit = rowColNum.split('c')
    rowNum = int(rowColSplit[0][1:])
    colNum = int(rowColSplit[1])
    status = 'ok'

    if rowNum>15 or colNum>15 or (rowNum<7 and colNum>9) or (rowNum>9 and colNum<7):
        result = {'status':'error: invalid cell reference'}
        return result
    
    if 'value' not in parms:
        value = 0
    else:
        try:
            value = int(parms['value'])
            if value < 1 or value>9:
                result = {'status':'error: invalid value'}
                return result
        except ValueError:
            result = {'status':'error: invalid value'}
            return result
    
    colMajorOrder = utilities.convertToColMajorOrder(grid)
    if str(value) in colMajorOrder[colNum-1] and value > 0:
        status = 'warning' 

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
    
        
    if value>0:
        subGraphs = utilities.createSubGraphs(rows)
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
        
    if rowNum <=9:
        if rows[rowNum-1][colNum-1]<0:
            result = {'status':'error: attempt to change fixed hint'}
            return result
        elif value in map(abs,rows[rowNum-1]) and value>0:
            status = 'warning'
        rows[rowNum-1][colNum-1] = value
    else:
        if rows[rowNum-1][colNum-7]<0:
            result = {'status':'error: attempt to change fixed hint'}
            return result
        elif value in map(abs, rows[rowNum-1]) and value>0:
            status = 'warning'
        rows[rowNum-1][colNum-7] = value
        
    grid = []
    for row in rows:
        for col in row:
            grid.append(col)
               
    result = {'grid':grid, 'integrity': utilities.getEightCharactersOfHash(utilities.calculateHash(grid)), 'status':status}

    return result