import hashlib
import random
#
# str = "080050200200300004010090060090000605103000007000000030000402000027040401008000000506050670000609000020000060100000905407000030010040090600900003095080001" 
#
# hashobj = hashlib.sha256(b"080050200200300004010090060090000605103000007000000030000402000027040401008000000506050670000609000020000060100000905407000030010040090600900003095080001")
#
# if(hashobj.hexdigest() == "5a3f0c31993d46bcb2ab5f3e8318e734231ee8bdb26cba545fadd7b1732888cd"):
#     print("true")

# grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-
# 9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-
# 5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]    
# truth = "0-800-50-200-200-30000-40-100-900-600-90000-60-5-10-300000-70000000-30000-40-20000-2-70-40-40-100-8000000-50-60-50-6-70000-60-90000-200000-60-100000-90-5-40-70000-300-100-400-90-600-90000-30-9-50-8000-1"                                
#
#
# strColOrder = ""
# # for i in range(0, len(grid)-74, 9):
# #     strColOrder+=str(grid[i])      
# #
# # for i in range(1, len(grid)-18, 9):
# #     strColOrder+=str(grid[i])                     
#
# for i in range(0, 54, 9):
#     strColOrder+=str(grid[i])
#
# strColOrder+=str(grid[54])
# strColOrder+=str(grid[69])
# strColOrder+=str(grid[84])
#
# for i in range(1, 54, 9):
#     strColOrder+=str(grid[i])
#
# strColOrder+=str(grid[55])
# strColOrder+=str(grid[70])
# strColOrder+=str(grid[85])
#
# for i in range(2, 54, 9):
#     strColOrder+=str(grid[i])
#
# strColOrder+=str(grid[56])
# strColOrder+=str(grid[71])
# strColOrder+=str(grid[86])
#
# for i in range(3, 54, 9):
#     strColOrder+=str(grid[i])
#
# strColOrder+=str(grid[57])
# strColOrder+=str(grid[72])
# strColOrder+=str(grid[87])
#
# for i in range(4, 54, 9):
#     strColOrder+=str(grid[i])
#
# strColOrder+=str(grid[58])
# strColOrder+=str(grid[73])
# strColOrder+=str(grid[88])
#
# for i in range(5, 54, 9):
#     strColOrder+=str(grid[i])  
#
# strColOrder+=str(grid[59])
# strColOrder+=str(grid[74])
# strColOrder+=str(grid[89])  
#
# for i in range(6, 54, 9):
#     strColOrder+=str(grid[i])
#
# strColOrder+=str(grid[60])
# strColOrder+=str(grid[75])
# strColOrder+=str(grid[90])
# strColOrder+=str(grid[99])
# strColOrder+=str(grid[108])
# strColOrder+=str(grid[117])
# strColOrder+=str(grid[126])
# strColOrder+=str(grid[135])
# strColOrder+=str(grid[144])
#
# for i in range(7, 54, 9):
#     strColOrder+=str(grid[i])
#
# strColOrder+=str(grid[61])
# strColOrder+=str(grid[76])
# strColOrder+=str(grid[91])
# strColOrder+=str(grid[100])
# strColOrder+=str(grid[109])
# strColOrder+=str(grid[118])
# strColOrder+=str(grid[127])
# strColOrder+=str(grid[136])
# strColOrder+=str(grid[145])
#
# for i in range(8, 54, 9):
#     strColOrder+=str(grid[i])
#
# strColOrder+=str(grid[62])
# strColOrder+=str(grid[77])
# strColOrder+=str(grid[92])
# strColOrder+=str(grid[101])
# strColOrder+=str(grid[110])
# strColOrder+=str(grid[119])
# strColOrder+=str(grid[128])
# strColOrder+=str(grid[137])
# strColOrder+=str(grid[146])
#
# for i in range(63, 108, 15):
#     strColOrder+=str(grid[i])
#
# for i in range(102, 156, 9):
#     strColOrder+=str(grid[i])
#
# for i in range(64, 108, 15):
#     strColOrder+=str(grid[i])
#
# for i in range(103, 156, 9):
#     strColOrder+=str(grid[i])    
#
# for i in range(65, 108, 15):
#     strColOrder+=str(grid[i])
#
# for i in range(104, 156, 9):
#     strColOrder+=str(grid[i]) 
#
# for i in range(66, 108, 15):
#     strColOrder+=str(grid[i])
#
# for i in range(105, 156, 9):
#     strColOrder+=str(grid[i])
#
# for i in range(67, 108, 15):
#     strColOrder+=str(grid[i])
#
# for i in range(106, 156, 9):
#     strColOrder+=str(grid[i])
#
# for i in range(68, 108, 15):
#     strColOrder+=str(grid[i])
#
# for i in range(107, 156, 9):
#     strColOrder+=str(grid[i])  
#
# hashobj = hashlib.sha256(strColOrder.encode())
# print(hashobj.hexdigest())

def calchash2(grid):
    
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
    col = 10
    for i in range(0, len(stringDictionary)):
        print(stringDictionary[col-1])
    hashobj = hashlib.sha256(("".join(value for value in stringDictionary.values())).encode())
    print(("".join(value for value in stringDictionary.values())))
    randomNumber = random.randrange(len(hashobj.hexdigest())-7)
    return hashobj

def calculateHash(grid):
    strColOrder = ""                    
                        
    for i in range(0, 54, 9):
        strColOrder+=str(grid[i])
    
    strColOrder+=str(grid[54])
    strColOrder+=str(grid[69])
    strColOrder+=str(grid[84])
    
    for i in range(1, 54, 9):
        strColOrder+=str(grid[i])
        
    strColOrder+=str(grid[55])
    strColOrder+=str(grid[70])
    strColOrder+=str(grid[85])
    
    for i in range(2, 54, 9):
        strColOrder+=str(grid[i])
    
    strColOrder+=str(grid[56])
    strColOrder+=str(grid[71])
    strColOrder+=str(grid[86])
    
    for i in range(3, 54, 9):
        strColOrder+=str(grid[i])
    
    strColOrder+=str(grid[57])
    strColOrder+=str(grid[72])
    strColOrder+=str(grid[87])
    
    for i in range(4, 54, 9):
        strColOrder+=str(grid[i])
        
    strColOrder+=str(grid[58])
    strColOrder+=str(grid[73])
    strColOrder+=str(grid[88])
    
    for i in range(5, 54, 9):
        strColOrder+=str(grid[i])  
    
    strColOrder+=str(grid[59])
    strColOrder+=str(grid[74])
    strColOrder+=str(grid[89])  
    
    for i in range(6, 54, 9):
        strColOrder+=str(grid[i])
    
    strColOrder+=str(grid[60])
    strColOrder+=str(grid[75])
    strColOrder+=str(grid[90])
    strColOrder+=str(grid[99])
    strColOrder+=str(grid[108])
    strColOrder+=str(grid[117])
    strColOrder+=str(grid[126])
    strColOrder+=str(grid[135])
    strColOrder+=str(grid[144])
    
    for i in range(7, 54, 9):
        strColOrder+=str(grid[i])
    
    strColOrder+=str(grid[61])
    strColOrder+=str(grid[76])
    strColOrder+=str(grid[91])
    strColOrder+=str(grid[100])
    strColOrder+=str(grid[109])
    strColOrder+=str(grid[118])
    strColOrder+=str(grid[127])
    strColOrder+=str(grid[136])
    strColOrder+=str(grid[145])
    
    for i in range(8, 54, 9):
        strColOrder+=str(grid[i])
    
    strColOrder+=str(grid[62])
    strColOrder+=str(grid[77])
    strColOrder+=str(grid[92])
    strColOrder+=str(grid[101])
    strColOrder+=str(grid[110])
    strColOrder+=str(grid[119])
    strColOrder+=str(grid[128])
    strColOrder+=str(grid[137])
    strColOrder+=str(grid[146])
    
    for i in range(63, 108, 15):
        strColOrder+=str(grid[i])
    
    for i in range(102, 156, 9):
        strColOrder+=str(grid[i])
        
    for i in range(64, 108, 15):
        strColOrder+=str(grid[i])
    
    for i in range(103, 156, 9):
        strColOrder+=str(grid[i])    
        
    for i in range(65, 108, 15):
        strColOrder+=str(grid[i])
    
    for i in range(104, 156, 9):
        strColOrder+=str(grid[i]) 
        
    for i in range(66, 108, 15):
        strColOrder+=str(grid[i])
    
    for i in range(105, 156, 9):
        strColOrder+=str(grid[i])
        
    for i in range(67, 108, 15):
        strColOrder+=str(grid[i])
    
    for i in range(106, 156, 9):
        strColOrder+=str(grid[i])
    for i in range(68, 108, 15):
        strColOrder+=str(grid[i])
    for i in range(107, 156, 9):
        strColOrder+=str(grid[i])  
    hashobj = hashlib.sha256(strColOrder.encode())
    randomNumber = random.randrange(len(hashobj.hexdigest())-7)
    return hashobj


    
grid = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,-1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,-2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,
                    2,-6,0,0,0,-6,0,0,-3,0,0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,-6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,-5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]

hashobj = calchash2(grid)
print(hashobj.hexdigest())
# if hashobj.hexdigest() == "5a3f0c31993d46bcb2ab5f3e8318e734231ee8bdb26cba545fadd7b1732888cd":
#     print("true1")
# grid = [0,-6,0,0,0,0,0,-5,-9,-9,-3,0,-4,-8,0,0,0,0,0,0,0,0,0,-7,-3,0,0,0,-5,0,0,-1,0,0,-4,-6,0,0,0,0,0,-
# 6,0,-9,0,0,-8,-1,-2,0,0,0,0,0,0,0,0,0,-7,0,0,0,0,0,0,0,0,-5,0,-8,0,-4,0,0,-1,0,0,0,-7,0,0,-6,0,-2,0,-
# 9,0,0,0,0,0,0,0,0,-5,0,0,0,0,0,0,0,0,0,-9,-5,-3,0,0,-7,0,-4,0,0,0,0,0,-5,-8,0,0,-1,0,0,-9,0,0,0,-2,-
# 1,0,0,0,0,0,0,0,0,0,-9,-8,0,-6,-1,-6,-1,0,0,0,0,0,-7,0]
#
# if calchash2(grid).hexdigest() == "6fcd71ef7722e7573d2f607a35cfa48f72b03c4cea135ac31f7ef73a58e50a8a":
#     print("true2")
#
# grid = [0,0,0,0,-6,0,0,0,0,0,0,0,-4,0,-9,0,0,0,0,0,-9,-7,0,-5,-1,0,0,0,-5,-2,0,-7,0,-8,-9,0,-9,0,0,-
# 5,0,-2,0,0,-4,0,-8,-3,0,-4,0,-7,-2,0,0,0,-1,-2,0,-8,0,0,0,0,-3,0,0,0,0,0,0,0,-6,0,-4,0,0,0,-8,0,-
# 7,0,0,0,0,0,0,0,-5,0,0,0,0,-1,0,-6,-3,0,0,0,-9,-8,0,-5,0,-1,-2,0,-2,0,0,-7,0,-1,0,0,-3,0,-4,-3,0,-8,0,-
# 6,-5,0,0,0,-7,-3,0,-5,-9,0,0,0,0,0,-4,0,-2,0,0,0,0,0,0,0,-6,0,0,0,0]
#
# if calchash2(grid).hexdigest() == "eb572835ffe2015c731057f94d46fa77430ad6fd332abb0d7dd39d5f2ccadea9":
#     print("true3")
