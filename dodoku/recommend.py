import dodoku.insert as insert
import dodoku.calculateHash as calculateHash
 
def _recommend(parms):
    if 'cell' not in parms:
        result = {'status':'error: invalid cell'}
        return result 
    elif 'grid' not in parms:
        result = {'status':'error: invalid grid'}
        return result
    elif 'integrity' not in parms:
        result = {'status':'error: invalid integrity'}
        return result
    recommend = []
    status = "ok"
    grid = parms['grid']
    if len(grid)!=153:
        result = {'status':'error: invalid grid'}
        return result
    cell = str(parms['cell'])
    
    if "'" in parms['integrity']:
        integrity = parms['integrity'].replace("'", "")
    else:
        integrity = parms['integrity'].replace('"', '')
    
    for i in range(1, 10):
        parms = {'op':'insert', 'cell':cell, 'value':str(i), 'grid':grid, 'integrity':integrity}
        parms = insert._insert(parms)
        if parms['status'] == 'ok':
            recommend.append(int(i))
        elif "error:" in parms['status'] and "attempt to change fixed hint" not in parms['status']:
            result = {'status':parms['status']}
            return result
        
    result = {"recommendation":recommend, "status":status}
    return result
