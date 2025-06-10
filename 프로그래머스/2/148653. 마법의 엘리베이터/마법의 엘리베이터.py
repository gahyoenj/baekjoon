def solution(storey):
    answer = 0
    
    while storey > 0:
        r = storey % 10
        
        if r > 5:
            answer += (10 - r)
            storey += 10
        
        elif r < 5:
            answer += r
        
        else:
            nr = (storey//10) % 10
            
            if nr >= 5:
                answer += 5
                storey += 10
            
            else:
                answer += 5
        
        storey //= 10
    
    return answer