import dodoku.changeMajorOrder as changeMajorOrder
import dodoku.calculateHash as calculateHash
import dodoku.subGraphs as subGraphs

def _insert(parms):
    if 'cell' not in parms:
        result = {'status':'error: missing cell reference'}
    elif 'grid' not in parms:
        result = {'status':'error: invalid grid'}
    elif 'integrity' not in parms:
        result = {'status':'error: integrity mismatch'}
    elif len(parms['cell']) < 4 or not parms['cell'].lower().startswith('r') or (parms['cell'].lower()[2]!='c' and parms['cell'].lower()[3]!='c'):
        result = {'status': 'error: missing cell reference'}
    else:
        grid = parms['grid']
        integrity = parms['integrity'].replace("'", "")
        
        if not isinstance(grid, list):
            grid = grid.replace('[', '')
            grid = grid.replace(']', '')
            grid = grid.split(',')
            try:
                grid = list(map(int, grid))
            except ValueError:
                result = {'status':'error: invalid grid'}
                return result             
            
        if not all(isinstance(value, int) for value in grid) or not all((value<10 and value>-10) for value in grid):
            result = {'status':'error: invalid grid'}
            return result
                             
        if str(integrity) not in str(calculateHash.calculateHash(grid)):
            result = {'status':'error: integrity mismatch'}
            return result
        
        rowColNum = parms['cell'].lower()
        rowColSplit = rowColNum.split('c')
        rowNum = int(rowColSplit[0][1:])
        colNum = int(rowColSplit[1])
        status = 'ok'
        
        if rowNum>15 or colNum>15 or rowNum < 1 or colNum<1 or (rowNum<7 and colNum>9) or (rowNum>9 and colNum<7):
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
        
        colMajorOrder = changeMajorOrder.convertToColMajorOrder(grid)
        if str(value) in colMajorOrder[colNum-1] and value > 0:
            status = 'warning' 
    
        rows = changeMajorOrder.convertToColMajorOrderList(grid)         
            
        if value>0 and status!='warning':
            status = subGraphs.checkValidSubgraph(rows, rowNum, colNum, value)
            
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
            
        grid = changeMajorOrder.convertToRowMajorOrder(rows)
    
        result = {'grid':grid, 'integrity': calculateHash.getEightCharactersOfHash(calculateHash.calculateHash(grid)), 'status':status}
    
    return result