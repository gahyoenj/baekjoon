def solution(board):
    answer = 0
    n = len(board)
    visited = [[[2e10]*4 for _ in range(n)] for _ in range(n)]
    q = []
    for d in range(4):
        visited[0][0][d] = 0
        q.append((0,0,d,0))
    
    
    
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    
    while q:
        vr,vc,d,cost = q.pop(0)
        
        for nd in range(4):
            dr = directions[nd][0]
            dc = directions[nd][1]
            newR = vr + dr
            newC = vc + dc
            
            if 0<=newR <n and 0<=newC < n and board[newR][newC] == 0:
                new_cost = cost + 100
                if d != nd:
                    new_cost += 500
                
                if new_cost < visited[newR][newC][nd]:
                    visited[newR][newC][nd] = new_cost
                    q.append((newR,newC,nd,new_cost))
                
    answer = min(visited[n-1][n-1])
    return answer