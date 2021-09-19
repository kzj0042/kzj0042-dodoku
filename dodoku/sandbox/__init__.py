import hashlib

str = "080050200200300004010090060090000605103000007000000030000402000027040401008000000506050670000609000020000060100000905407000030010040090600900003095080001" 

hashobj = hashlib.sha256(b"080050200200300004010090060090000605103000007000000030000402000027040401008000000506050670000609000020000060100000905407000030010040090600900003095080001")

if(hashobj.hexdigest() == "5a3f0c31993d46bcb2ab5f3e8318e734231ee8bdb26cba545fadd7b1732888cd"):
    print("true")

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