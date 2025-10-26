def solution(k, ranges):
    answer = []
    g = [k]
    while k > 1:
        if k % 2 == 0:
            k = k // 2
        else:
            k = k*3 + 1
        g.append(k)
    
    section = []
    for idx in range(len(g)-1):
        size = 0
        s = min(g[idx],g[idx+1])
        t = max(g[idx],g[idx+1]) - s
        size = s + t / 2
        # print(size)
        section.append(size)
    n = len(g)
    for a,b in ranges:
        x1 = a
        x2 = n + b

        if x1 >= x2:
            answer.append(-1.0)
        else:
            answer.append(float(sum(section[x1:x2-1])))
    
    return answer