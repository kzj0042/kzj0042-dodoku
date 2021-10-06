import dodoku.create as create 

def _insert(parms):
    grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,3,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]                                
                                 
    result = {'grid':grid, 'integrity': calculateHash(grid), 'status':'ok'}
    
    return result

def calculateHash(grid):  
    print("here")
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
    hashobj = hashlib.sha256(("".join(value for value in stringDictionary.values())).encode())
    randomNumber = random.randrange(len(hashobj.hexdigest())-7)
    return hashobj