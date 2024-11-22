def solution(a, b):
    answer = 0
    afirst = str(a) + str(b)
    multi = 2 * a * b
    answer = max(multi, int(afirst))
    return answer