from collections import deque

def bfs():
    while q:
        vr,vc,cnt = q.popleft()
        if (vr == 0 or vr == R-1 or vc == 0 or vc == C-1) and arr[vr][vc] == 'J':
            return cnt
        for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
            newR = vr + dr
            newC = vc + dc
            if arr[vr][vc] == 'F':
                if 0<=newR<R and 0<=newC<C and not visited_f[newR][newC] and arr[newR][newC] != '#':
                    arr[newR][newC] = 'F'
                    q.append((newR,newC,cnt))
                    visited_f[newR][newC] = visited_f[vr][vc] + 1
            elif arr[vr][vc] == 'J':
                if 0 <= newR < R and 0 <= newC < C and visited_f[newR][newC] < visited_j[vr][vc] + 1 and arr[newR][newC] != '#':
                    if arr[newR][newC] == '.':
                        arr[newR][newC] = 'J'
                        q.append((newR,newC,cnt+1))
                        visited_j[newR][newC] = visited_j[vr][vc] + 1
    return 0
R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
q = deque()
visited_f = [[0] * C for _ in range(R)]
visited_j = [[0] * C for _ in range(R)]
for row in range(R):
    for col in range(C):
        if arr[row][col] == 'F':
            q.append((row,col,1))
            visited_f[row][col] = 1
        if arr[row][col] == 'J':
            q.appendleft((row,col,1))
            visited_j[row][col] = 1

result = bfs()

if result:
    print(result)
else:
    print('IMPOSSIBLE')