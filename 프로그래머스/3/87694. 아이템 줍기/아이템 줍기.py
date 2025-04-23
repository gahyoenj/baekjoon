import copy
def bfs(cx,cy,ix,iy,visited,N,arr):
    cnt = 0
    q = [(cy,cx)]
    visited[cy][cx] = 1
    
    while q:
        vy,vx = q.pop(0)
        

        if vy == iy and vx == ix:
            return (visited[vy][vx] -1) // 2
            break
            

        for nr,nc in [(0,1),(1,0),(0,-1),(-1,0)]:
            newR = vy + nr
            newC = vx + nc
            if 0<= newR<N+2 and 0<= newC < N+2 and not visited[newR][newC]:
                if arr[newR][newC] == 1: 
                    q.append((newR,newC))
                    visited[newR][newC] = visited[vy][vx] + 1

                
    

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    maxV = max([max(row) for row in rectangle])
    # print(maxV)
    
    arr = [[0]*(maxV*2+2) for _ in range(maxV*2+2)]

    for lx,ly,rx,ry in rectangle:
        lx,ly,rx,ry = 2*lx,2*ly,2*rx,2*ry
        for y in range(ly,ry+1):
            for x in range(lx,rx+1):
                if arr[y][x] == 0:
                    arr[y][x] = 1

    
    for lx, ly, rx, ry in rectangle:
        lx, ly, rx, ry = 2 * lx, 2 * ly, 2 * rx, 2 * ry
        for y in range(ly + 1, ry):
            for x in range(lx + 1, rx):
                arr[y][x] = 0

                    
    visited = [[0] * (maxV*2 +2) for _ in range(maxV*2 +2)]
    answer = bfs(characterX*2,characterY*2,itemX*2,itemY*2,visited,maxV*2,arr)
    return answer