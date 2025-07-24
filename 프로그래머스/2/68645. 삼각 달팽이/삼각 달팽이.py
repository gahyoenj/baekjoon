def solution(n):
    answer = []
    
    num = [0] * (n+1)
    
    num[1] = 1
    
    for i in range(2,n+1):
        num[i] = i + num[i-1]
    
    maxV = num[-1]
    

    
    arr = [[0]*n for _ in range(n)]
    
    currN = 1
    
    row = 0
    col = 0
    
    direction = [(1,0),(0,1),(-1,-1)]
    
    current = 0
    
    while True:
        if currN > maxV:
            break
        
        arr[row][col] = currN
        currN += 1
        
        newR = row + direction[current][0]
        newC = col + direction[current][1]
        
        if not(0<=newR< n and 0<= newC < n and not arr[newR][newC]):
            current = (current+1) % 3
            newR = row + direction[current][0]
            newC = col + direction[current][1]
        
        row = newR
        col = newC
        
    
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                answer.append(arr[i][j])
        
    return answer