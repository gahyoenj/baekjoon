def find(r,c,visited,cnt,maps):
    q = [(r,c)]
    visited[r][c] = True
    
    while q:
        br,bc = q.pop(0)
    
        
        for dr,dc in [(1,0),(0,1),(0,-1),(-1,0)]:
            newR = br + dr
            newC = bc + dc
        
            if 0<=newR<row and 0<=newC<col and not visited[newR][newC] and maps[newR][newC] != 'X':
                cnt += int(maps[newR][newC])
                q.append((newR,newC))
                visited[newR][newC] = True
        
    return cnt
                
            
        

def solution(maps):
    answer = []
    global row, col
    row = len(maps)
    col = len(maps[0])
    
    visited= [[False]*col for _ in range(row)]
    
    for i in range(row):
        for j in range(col):
            cnt = 0
            if maps[i][j] != 'X' and not visited[i][j]:
                cnt += int(maps[i][j])
                result = find(i,j,visited,cnt,maps)
                answer.append(result)
    
    if answer:
        answer.sort()
    else:
        answer = [-1]
    return answer