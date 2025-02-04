from collections import deque

def solution(maps):
    def bfs(start, target):
        q = deque([start])
        visited = [[-1] * m for _ in range(n)] 
        visited[start[0]][start[1]] = 0 

        while q:
            r, c = q.popleft()

            if (r, c) == target:  
                return visited[r][c]

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < m and maps[nr][nc] != 'X':
                    new_dist = visited[r][c] + 1
                    if visited[nr][nc] == -1 or visited[nr][nc] > new_dist:
                        visited[nr][nc] = new_dist
                        q.append((nr, nc))

        return -1  


    n, m = len(maps), len(maps[0])
    start = lever = exit = None

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                exit = (i, j)


    dist_to_lever = bfs(start, lever)
    if dist_to_lever == -1:  
        return -1


    dist_to_exit = bfs(lever, exit)
    if dist_to_exit == -1:  
        return -1

    return dist_to_lever + dist_to_exit  
