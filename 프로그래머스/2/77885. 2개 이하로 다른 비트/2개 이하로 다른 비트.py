def solution(numbers):
    answer = []
    
    for num in numbers:
        result = ((num ^ (num+1)) >> 2) + num +1
        
        answer.append(result)
        
    
    return answer