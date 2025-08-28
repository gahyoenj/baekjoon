def solution(n):
    answer = ''
    char = '수박'
    
    for i in range(n):
        answer += char[i%2]
    
    return answer