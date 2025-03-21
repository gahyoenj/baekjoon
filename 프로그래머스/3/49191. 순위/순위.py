def bfs(node,result,g):
    q = [node]
    result[node-1][node-1] = 2
    while q:
        p = q.pop(0)
        
        for next in g[p]:
            if not result[node-1][next-1]:
                result[node-1][next-1] = 1
                result[next-1][node-1] = -1
                q.append(next)

def solution(n, results):
    answer = 0
    result = [[False]*n for _ in range(n)]
    g = [[] * (n+1) for _ in range(n+1)]
    for win,lose in results:
        g[win].append(lose)
    print(g)
    for i in range(1,n+1):
        bfs(i,result,g)
    answer = n
    # print(result)
    for i in range(n):
        if False in result[i]:
            print(result[i])
            answer -= 1
    return answer