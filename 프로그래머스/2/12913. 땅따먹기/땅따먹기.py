def solution(land):
    answer = 0
    
    for i in range(1,len(land)):
        for j in range(4):
            maxV = land[i][j]
            for k in range(4):
                if k != j and land[i][j]+land[i-1][k] > maxV:
                    maxV = land[i][j] + land[i-1][k]
            
            land[i][j] = maxV
                    
    
    answer = max(land[-1])
    return answer