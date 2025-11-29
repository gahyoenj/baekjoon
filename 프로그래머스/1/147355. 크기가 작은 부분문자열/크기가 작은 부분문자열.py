def solution(t, p):
    answer = 0
    pl = len(p)
    p = int(p)
    for i in range(0,len(t)-pl+1):
        num = t[i:i+pl]
        if int(num) <= p:
            answer += 1
    return answer