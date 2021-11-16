import dodoku.insert as insert
import dodoku.calculateHash as calculateHash
 
def _recommend(parms):
    rowColNum = parms['cell'].lower()
    rowColSplit = rowColNum.split('c')
    try:
        rowNum = int(rowColSplit[0][1:])
        colNum = int(rowColSplit[1])
    except ValueError:
        result = {'status':'error: invalid cell'}
        return result
    
    if rowNum>15 or colNum>15 or rowNum < 1 or colNum<1 or (rowNum<7 and colNum>9) or (rowNum>9 and colNum<7):
        result = {'status':'error: invalid cell'}
        return result
    
    recommend = []
    status = "ok"
    grid = parms['grid']
    if not all((value<10 and value>-10)  for value in grid):
        result = {'status':'error: invalid grid'}
        return result
    
    cell = str(parms['cell'])
    for i in range(1, 10):
        parms = {'op':'insert', 'cell':cell, 'value':str(i), 'grid':grid, 'integrity':calculateHash.getEightCharactersOfHash(calculateHash.calculateHash(grid))}
        parms = insert._insert(parms)
        if parms['status'] == 'ok':
            recommend.append(int(i))
    
    result = {"recommendation":recommend, "status":status}
    return result
