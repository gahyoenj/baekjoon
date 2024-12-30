def bfs(row,col,maps):
    visited = [[0]*m for _ in range(n)]
    q = []
    q.append((row,col))
    visited[row][col] = 1
    
    while q:
        vr,vc = q.pop(0)

        if vr == n-1 and vc == m-1:
            return visited[vr][vc]
        
        for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            newR = vr + dr
            newC = vc + dc
            
            if 0<= newR<n and 0<=newC<m and not visited[newR][newC] and maps[newR][newC] == 1:
                q.append((newR,newC))
                visited[newR][newC] += visited[vr][vc] + 1
                

def solution(maps):
    answer = 0
    global n
    global m
    n = len(maps)
    m = len(maps[0])
    answer = bfs(0,0,maps)
    if not answer:
        answer = -1

    return answer