def solution(food):
    answer = ''
    
    for i,cnt in enumerate(food[1:]):
        food = i+1
        
        num = cnt // 2

        
        if num >= 1:            
            answer += str(food) * num
    
    answer += ('0' + answer[::-1])
    
    return answer