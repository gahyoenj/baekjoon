def solution(n, s, a, b, fares):
    answer = 0
    G = [[2e10]*(n+1) for _ in range(n+1)]
    
    for v1,v2,cost in fares:
        G[v1][v2] = cost
        G[v2][v1] = cost
    # print(G)
    
    for i in range(1,n+1):
        G[i][i] = 0
    
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if G[i][j] > G[i][k] + G[k][j]:
                    G[i][j] = G[i][k] + G[k][j]
    
    
    result = G[s][a] + G[s][b]
    for k in range(1,n+1):
        total = G[s][k] + G[k][a] + G[k][b]
        result = min(result,total)
    answer = result
    return answer