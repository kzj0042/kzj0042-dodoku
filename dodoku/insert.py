"""
    Created on October 21, 2021
    
    @author: Kyle Julien
"""
import dodoku.changeMajorOrder as changeMajorOrder
import dodoku.calculateHash as calculateHash
import dodoku.subGraphs as subGraphs
import re

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
        if "'" in parms['integrity']:
            integrity = parms['integrity'].replace("'", "")
        else:
            integrity = parms['integrity'].replace('"', '')
        if not isinstance(grid, list):
            grid = grid.replace('[', '')
            grid = grid.replace(']', '')
            grid = grid.split(',')
            try:
                grid = list(map(int, grid))
            except ValueError:
                result = {'status':'error: invalid grid'}
                return result             

        if len(grid)!=153 or not all((isinstance(value, int) and value<10 and value>-10)  for value in grid):
            result = {'status':'error: invalid grid'}
            return result
                             
        if len(integrity) != 8 or str(integrity) not in str(calculateHash.calculateHash(grid)):
            result = {'status':'error: integrity mismatch'}
            return result
        
        rowColNum = parms['cell'].lower()
        rowColSplit = rowColNum.split('c')
        try:
            rowNum = int(rowColSplit[0][1:])
            colNum = int(rowColSplit[1])
        except ValueError:
            result = {'status':'error: invalid cell reference'}
            return result
        status = 'ok'
        
        if rowNum>15 or colNum>15 or rowNum < 1 or colNum<1 or (rowNum<7 and colNum>9) or (rowNum>9 and colNum<7):
            result = {'status':'error: invalid cell reference'}
            return result
        
        if 'value' not in parms or parms['value'] == "":
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
        
        rows = changeMajorOrder.convertToColMajorOrderList(grid)
        if rowNum <=9:
            if rows[rowNum-1][colNum-1]<0:
                result = {'status':'error: attempt to change fixed hint'}
                return result
            rows[rowNum-1][colNum-1] = 0
        else:
            if rows[rowNum-1][colNum-7]<0:
                result = {'status':'error: attempt to change fixed hint'}
                return result
            rows[rowNum-1][colNum-7] = 0         
            
        grid = changeMajorOrder.convertToRowMajorOrder(rows)
        
        colMajorOrder = changeMajorOrder.convertToColMajorOrder(grid)
        if colNum>6 and colNum<10 and value>0:
            if rowNum<=6:
                colList = re.findall(r'-?\d|[a-z]|\W?', colMajorOrder[colNum-1])[0:9]
                if str(value) in str(colList):
                    status = 'warning'
            elif rowNum>9:
                colList = re.findall(r'-?\d|[a-z]|\W?', colMajorOrder[colNum-1])[6:15]
                if str(value) in str(colList):
                    status = 'warning'
            else: 
                print(str(colMajorOrder[colNum-1]))
                if str(value) in str(colMajorOrder[colNum-1]) and value > 0:
                    status = 'warning' 
        else:
            if str(value) in str(colMajorOrder[colNum-1]) and value>0:
                status = 'warning'            
    
        if rowNum>6 and rowNum<10 and value>0:
            if colNum<=6:
                rowList = rows[rowNum-1][0:9]
                if value in map(abs, rowList):
                    status='warning'
            elif colNum>9:
                rowList = rows[rowNum-1][6:15]
                if value in map(abs, rowList):
                    status = 'warning'
            else:
                if value in map(abs, rows[rowNum-1]):
                    status = 'warning'
        else:
            if value in map(abs,rows[rowNum-1]) and value>0:
                status = 'warning'
    
        if value>0 and status!='warning':
            status = subGraphs.checkValidSubgraph(rows, rowNum, colNum, value)
        
        if rowNum <=9:
            rows[rowNum-1][colNum-1] = value
        else:
            rows[rowNum-1][colNum-7] = value
            
        grid = changeMajorOrder.convertToRowMajorOrder(rows)
    
        result = {'grid':grid, 'integrity': calculateHash.getEightCharactersOfHash(calculateHash.calculateHash(grid)), 'status':status}
    
    return result