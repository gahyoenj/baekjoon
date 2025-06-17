def solution(order):
    answer = 0
    extra = []
    num = 1
    idx = 0
    
    while num <= len(order):
        if num == order[idx]:
            answer += 1
            num += 1
            idx += 1
        
        elif extra and extra[-1] == order[idx]:
            extra.pop()
            idx += 1
            answer += 1
        
        else:
            extra.append(num)
            num += 1
    
    
    while extra and extra[-1] == order[idx]:
        extra.pop()
        idx += 1
        answer += 1
        
    
    return answer