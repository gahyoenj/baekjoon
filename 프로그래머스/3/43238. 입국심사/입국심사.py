def solution(n, times):
    answer = 0
    left = 1
    right = max(times) * n
    
    while left <= right:
        mid = (left+right) // 2
        
        complete = 0
        
        for time in times:
            complete += mid // time
            
            if complete >= n:
                break
        
        if complete >= n:
            answer = mid
            right = mid -1
        
        else:
            left = mid + 1
        
    return answer