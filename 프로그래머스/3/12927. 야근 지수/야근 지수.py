def solution(n, works):
    answer = 0
    while n > 0:
        maxV = max(works)
        if maxV == 0:
            break
        for i in range(len(works)):
            if works[i] == maxV:
                works[i] -= 1
                n -= 1
                if n == 0:
                    break
    for time in works:
        answer += time * time
    return answer
