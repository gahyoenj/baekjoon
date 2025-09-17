def solution(stones, k):
    answer = 0
    left = 1
    right = max(stones)
    
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        can = True
        
        for stone in stones:
            if stone < mid:
                cnt += 1
            
                if cnt >= k:
                    can = False
                    break
            else:
                cnt = 0
        
        if can:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return answer