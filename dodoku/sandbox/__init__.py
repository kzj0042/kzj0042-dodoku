import dodoku.insert as insert
import dodoku.calculateHash as calculteHash

grid = [3,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]
print(calculteHash.calculateHash(grid))

truth = ['ok', 'warning', 'ok', 'warning', 'warning', 'warning', 'warning', 'warning' ,'warning']
truth1 = ['ok', 'warning', 'ok', 'ok', 'warning', 'warning', 'warning', 'ok', 'warning']
truth2 = ['warning', 'ok', 'warning', 'warning', 'warning', 'warning', 'warning', 'ok', 'warning']
truth3 = ['warning', 'warning', 'ok', 'warning', 'warning', 'warning', 'warning', 'ok', 'warning']
truth4= ['warning', 'warning', 'warning', 'ok', 'ok', 'warning', 'ok', 'warning', 'warning']


truth5 = ['warning', 'warning', 'ok', 'warning', 'ok', 'warning', 'ok', 'ok', 'warning']
truth6 = ['warning', 'warning', 'warning', 'warning', 'ok', 'ok', 'warning', 'ok', 'warning']
truth7= ['warning', 'ok', 'ok', 'warning', 'warning', 'ok', 'warning', 'warning', 'warning']
truth8 = ['ok', 'warning', 'ok', 'warning', 'warning', 'ok', 'warning', 'ok', 'ok']
parms = {'op':'insert', 'cell':'r5c7', 'value':'3', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
actualResult = insert._insert(parms)  

for i in range(1, 10):
    parms = {'op':'insert', 'cell':'r9c7', 'value':str(i), 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
    actualResult = insert._insert(parms)
    if actualResult['status'] != truth8[i-1]:
        print("false at: "+str(i))
    
print(" ")

# for i in range(1, 16):
#     for j in range(1, 16):
#         cell = "r"+str(i)+"c"+str(j)
#         parms = {'op':'insert', 'cell':cell, 'value':'9', 'grid':grid, 'integrity':calculteHash.getEightCharactersOfHash(calculteHash.calculateHash(grid))}
#         actualResult = insert._insert(parms)
#         print(cell + ": " + actualResult['status'])
        
