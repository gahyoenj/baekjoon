def solution(ineq, eq, n, m):
    answer = 0
    if n<m:
        if ineq == '<':
            answer = 1
        else:
            answer = 0
    elif n >m:
        if ineq == '>':
            answer = 1
        else:
            answer = 0
    else:
        if eq == '=':
            answer = 1
        else:
            answer = 0
            
    return answer