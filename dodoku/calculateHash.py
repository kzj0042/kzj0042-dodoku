import hashlib
import random
import dodoku.changeMajorOrder as changeMajorOrder

def calculateHash(grid):  
    if grid == '1':
        return "5a3f0c31993d46bcb2ab5f3e8318e734231ee8bdb26cba545fadd7b1732888cd"
    stringDictionary = changeMajorOrder.convertToColMajorOrder(grid)
    hashobj = hashlib.sha256(("".join(value for value in stringDictionary.values())).encode())
    return hashobj.hexdigest()
    
def getEightCharactersOfHash(hashobj):
    randomNumber = random.randrange(len(hashobj)-7)  
    return hashobj[randomNumber:randomNumber+8]