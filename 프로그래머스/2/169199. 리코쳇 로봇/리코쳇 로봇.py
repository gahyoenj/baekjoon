def bfs(sr,sc,er,ec,board):
    visited = [[-1]*len(board[0]) for _ in range(len(board))]
    q = [(sr,sc)]
    visited[sr][sc] = 0
    
    while q:
        r,c = q.pop(0)
        
        if r == er and c == ec:
            return visited[r][c]
        
        for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            nr = r 
            nc = c 
            
            while True:
                newR = nr + dr
                newC = nc + dc
                
                if 0<=newR<len(board) and 0<= newC < len(board[0]) and board[newR][newC] != 'D':
                    nr,nc = newR,newC
                
                else:
                    break
            
            # print(nr,nc)
                
            if visited[nr][nc] == -1:
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr,nc))
                
    return -1
            
                    
            
            
        


def solution(board):
    answer = 0
    
    sr,sc = 0,0
    er,ec = 0,0
    
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 'R':
                sr,sc = row,col
                
            if board[row][col] == 'G':
                er,ec = row,col
    
    answer = bfs(sr,sc,er,ec,board)
            
    return answer