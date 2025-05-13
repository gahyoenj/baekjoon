def solution(n, s):
    answer = []
    if n > s:
        answer = [-1]
        
    else:
        while n > 0:
            m = s // n
            answer.append(m)
            s -= m
            n -= 1
    answer.sort()
    return answer