def solution(rows, columns, queries):
    answer = []
    d = [(0,1),(1,0),(0,-1),(-1,0)]
    
    arr = []
    
    for i in range(1,rows*columns+1,columns):
        a = []
        for num in range(i,i+columns):
            a.append(num)
        
        arr.append(a)
    # print(arr)
    
    idx = 0
    
    for x1,y1,x2,y2 in queries:
        current = arr[x1-1][y1-1]
        
        row = x1-1
        col = y1-1
        
        minV = current
        
        
        while True:
            newR = row + d[idx][0]
            newC = col + d[idx][1]
            
            if not(x1-1<=newR<x2 and y1-1<=newC<y2):
                idx  = (idx+1) %4
                continue
                
            t = arr[newR][newC]
            arr[newR][newC] = current
            current = t
            
            if current < minV:
                minV = current
            
            row = newR
            col = newC
            
            if row == x1-1 and col == y1-1:
                break
    
        
        answer.append(minV) 
    
    return answer