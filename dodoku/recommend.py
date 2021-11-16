import dodoku.insert as insert
import dodoku.calculateHash as calculateHash
 
def _recommend(parms):
    recommend = []
    status = "ok"
    grid = parms['grid']
    cell = str(parms['cell'])
    for i in range(1, 10):
        parms = {'op':'insert', 'cell':cell, 'value':str(i), 'grid':grid, 'integrity':calculateHash.getEightCharactersOfHash(calculateHash.calculateHash(grid))}
        parms = insert(parms)
        if parms['status'] == 'ok':
            recommend.append(int(i))
    
    result = {"recommendation":recommend, "status":status}
    return result
