from itertools import combinations

def bfs(start, end):
    q = []
    q.append(start)
    visited = [[False] * N for _ in range(N)]
    visited[start[0]][start[1]] = True

    while q:
        vr, vc = q.pop(0)

        if [vr, vc] == end:
            return True

        for dr, dc in ([0, 1], [1, 0], [-1, 0], [0, -1]):
            newR, newC = vr + dr, vc + dc

            if 0 <= newR < N and 0 <= newC < N and not visited[newR][newC]:
                if (vr, vc, newR, newC) not in roads and (newR, newC, vr, vc) not in roads:
                    q.append((newR, newC))
                    visited[newR][newC] = True

    return False

N, K, R = map(int, input().split())

roads = set()
for _ in range(R):
    r1, c1, r2, c2 = map(int, input().split())
    roads.add((r1-1, c1-1, r2-1, c2-1))
    roads.add((r2-1, c2-1, r1-1, c1-1))

cow_list = []
for _ in range(K):
    row, col = map(int, input().split())
    cow_list.append([row-1, col-1])

cnt = 0
for data in combinations(cow_list, 2):
    start, end = data
    if not bfs(start, end):
        cnt += 1

print(cnt)