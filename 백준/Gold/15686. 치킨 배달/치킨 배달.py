# def bfs(row,col):
#     global chicken,minV, store, sumV
#     visited = [[False]*N for _ in range(N)]
#     q = []
#     q.append((row,col))
#     visited[row][col] = True
#
#     while q:
#         vr,vc = q.pop(0)
#
#         for dr,dc in [(-1,0),(0,1),(0,-1),(1,0)]:
#             newR = dr + vr
#             newC = dc + vc
#
#             if 0<=newR<N and 0<=newC<N and not visited[newR][newC]:
#                 if city[newR][newC] !=2:
#                     chicken += 1
#                     q.append((newR,newC))
#                     visited[newR][newC] = True
#                 if city[newR][newC] == 2:
#                     chicken += 1
#                     # visited[newR][newC]
#                     if chicken < minV:
#                         minV = chicken
#                         store += 1
#     sumV += minV
#
# N,M = map(int, input().split())
# city = [list(map(int, input().split())) for _ in range(N)]
# store = 0
# minV = 21e9
# sumV = 0
# for row in range(N):
#     for col in range(N):
#         if city[row][col] == 1:
#             chicken = 0
#             bfs(row,col)
# if store <= M:
#     print(sumV)

def distance(lst):
    global minV
    sumV = 0
    for h in home:
        min_dist = 21e9
        for chi in lst:
            dist = (abs(chi[1]-h[1])+abs(chi[0]-h[0]))
            min_dist = min(min_dist,dist)
        sumV += min_dist
    minV = min(sumV,minV)
    return
def combi(k, n,M):
    if k == M:
        chicken = []
        for i in range(len(store)):
            if visited[i]:
                chicken.append(store[i])
        distance(chicken)
        return

    for i in range(n, len(store)):
        if not visited[i]:
            visited[i] = 1
            combi(k + 1, i + 1, M)
            visited[i] = 0

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

home = []
store = []
for row in range(N):
    for col in range(N):
        if arr[row][col] == 1:
            home.append((row, col))
        elif arr[row][col] == 2:
            store.append((row, col))
# print(store)
visited = [0] * len(store)
minV = 21e9
combi(0, 0,M)
print(minV)

