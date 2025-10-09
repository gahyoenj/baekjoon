def solution(X, Y):
    answer = ''
    x = [0] * 10
    y = [0] * 10
    mate = []
    for num in range(10):
        cntX = X.count(str(num))
        x[num] = cntX
        cntY = Y.count(str(num))
        y[num] = cntY
    
    for n in range(10):
        if x[n] and y[n]:
            cnt = min(x[n],y[n])
            for _ in range(cnt):
                mate.append(n)
    mate.sort(reverse=True)
    
    if not mate:
        return '-1'
        
    if mate[0] == 0:
        return '0'
        
    for number in mate:
        answer += str(number)  
    
    return answer