import hashlib
import random
#
# str = "080050200200300004010090060090000605103000007000000030000402000027040401008000000506050670000609000020000060100000905407000030010040090600900003095080001" 
#
# hashobj = hashlib.sha256(b"080050200200300004010090060090000605103000007000000030000402000027040401008000000506050670000609000020000060100000905407000030010040090600900003095080001")
#
# if(hashobj.hexdigest() == "5a3f0c31993d46bcb2ab5f3e8318e734231ee8bdb26cba545fadd7b1732888cd"):
#     print("true")

# grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,0,-6,0,0,-3,0,0,0,0,-4,0,-5,-7,0,0,0,0,0,0,-6,-2,0,0,-7,0,-9,0,-5,0,-4,0,0,0,-6,0]     
# strColOrder = ""
# for i in range(0, len(grid)-18, 9):
#     strColOrder+=str(grid[i])                           
#
# print("")
#
# for i in range(1, len(grid)-18, 9):
#     strColOrder+=str(grid[i])                           
#
# print("")
#
# for i in range(2, len(grid)-18, 9):
#     strColOrder+=str(grid[i])                           
#
# print("")
#
# for i in range(3, len(grid)-18, 9):
#     strColOrder+=str(grid[i])          
#
# print("")
#
# for i in range(4, len(grid)-18, 9):
#     strColOrder+=str(grid[i])                     
#
# print("")
#
# for i in range(5, len(grid)-18, 9):
#     strColOrder+=str(grid[i])    
#
# print("")
#
# for i in range(6, len(grid)-18, 9):
#     strColOrder+=str(grid[i]) 
#
#
#
# print(strColOrder)

def calculateHash(str):
    if str == '2':
        hashobj = hashlib.sha256(b"0-900000-80-6-30-50-800-900000-10-400-4000-20000-80-100-70000-70-600-1000-300000000-500-6-500-4-900000-7-800-1-900-600000000-2000-700-40-10000-500-10-90000-9000-800-60-500000-500-30-90-6-70-200000-10")
    elif str == '3':
        hashobj = hashlib.sha256(b"0000-90000000-50-800000-9-20-3-1000-4-70-50-2-60-600-70-400-50-9-50-20-8-4000-1-80-70000-20000000-90-2000-90-40000000-40000-80-3-7000-8-10-70-3-40-300-50-800-60-7-60-10-5-2000-3-10-6-900000-20-50000000-30000")
    else:                                                                
        hashobj = hashlib.sha256(b"0-800-50-200-200-30000-40-100-900-600-90000-60-5-10-300000-70000000-30000-40-20000-2-70-40-40-100-8000000-50-60-50-6-70000-60-90000-200000-60-100000-90-5-40-70000-300-100-400-90-600-90000-30-9-50-8000-1")
    randomNumber = random.randrange(len(hashobj.hexdigest())-8)
    return hashobj.hexdigest()[randomNumber:randomNumber+8]

diction = {}
i = 0

for i in range(0, 5700):
    value = calculateHash('1')
    if value not in diction:
        diction[value] = 1
    else:
        diction[value]+=1
    
print(value)
        
for key, value in diction.items():
    print("Key: " + str(key) + ":"+"Value: "+str(value/5700))
print(len(diction))