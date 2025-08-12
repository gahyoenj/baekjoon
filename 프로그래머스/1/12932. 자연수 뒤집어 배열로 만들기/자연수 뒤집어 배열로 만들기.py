def solution(n):
    answer = []
    n = str(n)[::-1]
    
    for c in n:
        answer.append(int(c))
    return answer