def solution(s):
    answer = ''
    n = len(s)
    if n % 2 != 0:
        answer = s[n//2]
    else:
        idx = n // 2
        answer = s[idx-1:idx+1]
    return answer