from collections import deque
def fork(s,req):
    global cnt,n,m
    take = []
    for row in range(n):
        for col in range(m):
            if s[row][col] != req: 
                continue
                
            queue = deque()
            queue.append((row, col))
            visited = set()
            visited.add((row, col))
            flag = False
            
            while queue:
                r, c = queue.popleft()
                
                for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                    newR = r + dr
                    newC = c + dc
                    
                    if not (0 <= newR < n and 0 <= newC < m):
                        flag = True  
                        continue
                        
                    if s[newR][newC] == 0 and (newR, newC) not in visited:
                        queue.append((newR, newC))
                        visited.add((newR, newC))
                
            
            if flag:
                take.append((row,col))
    
    print(take)
    
    for r,c in take:
        s[r][c] = 0
        cnt -= 1

def crane(s,req):
    global n,m,cnt
    take = []
    
    for row in range(n):
        for col in range(m):
            if s[row][col] == req:
                take.append((row,col))
    
    for r,c in take:
        s[r][c] = 0
        cnt -= 1


def solution(storage, requests):
    answer = 0
    
    s = []
    
    global n,m,cnt
    
    n = len(storage)
    m = len(storage[0])
    cnt = n*m
    
    
    
    for st in storage:
        lst = []
        for box in st:
            lst.append(box)
        s.append(lst)
    
    for req in requests:
        if len(req) == 1:
            fork(s,req)
        
        if len(req) == 2:
            crane(s,req[0])
            
    answer = cnt
    return answer