def solution(a, b):
    answer = 0
    a = str(a)
    b = str(b)
    afirst = a + b
    bfrist = b + a
    answer = max(afirst, bfrist)
    answer = int(answer)
    return answer