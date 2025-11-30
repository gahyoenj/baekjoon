def solution(n):
    answer = 0
    s = ''
    while n > 0:
        p = n % 3
        n //= 3
        s += str(p)
    answer = int(s,3)
    return answer