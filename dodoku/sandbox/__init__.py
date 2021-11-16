import dodoku.insert as insert
import dodoku.calculateHash as calculteHash

grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,0]


print(calculteHash.calculateHash(grid))


# for i in range(1, 16):
#     for j in range(1, 16):
#         cell = "r"+str(i)+"c"+str(j)
#         parms = {'op':'insert', 'cell':cell, 'value':'9', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
#         actualResult = insert._insert(parms)
#         print(cell + ": " + actualResult['status'])
        
