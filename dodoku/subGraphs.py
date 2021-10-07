def createSubGraphs(rows):
    graph = []
    graph2 = []
    graph3 = []
    graph4 = []
    graph5 = []
    subGraphs = []
    
    for i in range(0, 3):
        for j in range(0, 3):
            graph.append(rows[i][j])
        for j in range(3, 6):
            graph2.append(rows[i][j])
        for j in range(6, 9):
            graph3. append(rows[i][j])
    subGraphs.append(graph)
    subGraphs.append(graph2)
    subGraphs.append(graph3)
    
    graph = []
    graph2 = []
    graph3 = []
    
    for i in range(3, 6):
        for j in range(0, 3):
            graph.append(rows[i][j])
        for j in range(3, 6):
            graph2.append(rows[i][j])
        for j in range(6, 9):
            graph3.append(rows[i][j])
    subGraphs.append(graph)
    subGraphs.append(graph2)
    subGraphs.append(graph3)
    
    graph = []
    graph2 = []
    graph3 = []
    
    for i in range(6, 9):
        for j in range(0, 3):
            graph.append(rows[i][j])
        for j in range(3, 6):
            graph2.append(rows[i][j])
        for j in range(6, 9):
            graph3.append(rows[i][j])
        for j in range(9, 12):
            graph4.append(rows[i][j])
        for j in range(12, 15):
            graph5.append(rows[i][j])
    subGraphs.append(graph)
    subGraphs.append(graph2)
    subGraphs.append(graph3)
    subGraphs.append(graph4)
    subGraphs.append(graph5)
    
    graph = []
    graph2 = []
    graph3 = []
    
    for i in range(9, 12):
        for j in range(0, 3):
            graph.append(rows[i][j])
        for j in range(3, 6):
            graph2.append(rows[i][j])
        for j in range(6, 9):
            graph3.append(rows[i][j])
    subGraphs.append(graph)
    subGraphs.append(graph2)
    subGraphs.append(graph3)
    
    graph = []
    graph2 = []
    graph3 = []
    
    for i in range(12, 15):
        for j in range(0, 3):
            graph.append(rows[i][j])
        for j in range(3, 6):
            graph2.append(rows[i][j])
        for j in range(6, 9):
            graph3.append(rows[i][j])
    subGraphs.append(graph)
    subGraphs.append(graph2)
    subGraphs.append(graph3)
        
    return subGraphs

def checkValidSubgraph(rows, rowNum, colNum, value):
    subGraphs = createSubGraphs(rows)
    status = 'ok'
    if rowNum<=3:
        if colNum<=3:
            if value in map(abs, subGraphs[0]):
                status = 'warning'
        elif colNum<=6:
            if value in map(abs, subGraphs[1]):
                status = 'warning'
        elif colNum<=9:
            if value in map(abs, subGraphs[2]):
                status = 'warning'
                
    elif rowNum<=6:
        if colNum<=3:
            if value in map(abs, subGraphs[3]):
                status = 'warning'
        elif colNum<=6:
            if value in map(abs, subGraphs[4]):
                status = 'warning'
        elif colNum<=9:
            if value in map(abs, subGraphs[5]):
                status = 'warning'
    
    elif rowNum<=9:
        if colNum<=3:
            if value in map(abs, subGraphs[6]):
                status = 'warning'
        elif colNum<=6:
            if value in map(abs, subGraphs[7]):
                status = 'warning'
        elif colNum<=9:
            if value in map(abs, subGraphs[8]):
                status = 'warning'
        elif colNum<=12:
            if value in map(abs, subGraphs[9]):
                status = 'warning'
        elif colNum<=15:
            if value in map(abs, subGraphs[10]):
                status = 'warning'
                
    elif rowNum<=12:
        if colNum<=9:
            if value in map(abs, subGraphs[11]):
                status = 'warning'
        elif colNum<=12:
            if value in map(abs, subGraphs[12]):
                status = 'warning'
        elif colNum<=15:
            if value in map(abs, subGraphs[13]):
                status = 'warning'  
                  
    else:
        if colNum<=9:
            if value in map(abs, subGraphs[14]):
                status = 'warning'
        elif colNum<=12:
            if value in map(abs, subGraphs[15]):
                status = 'warning'
        elif colNum<=15:
            if value in map(abs, subGraphs[16]):
                status = 'warning'   
    return status         