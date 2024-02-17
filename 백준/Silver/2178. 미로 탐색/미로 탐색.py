def bfs(stR,stC):
  q = []
  visited = [[0] * M for _ in range(N)]
  q.append((stR,stC))
  visited[stR][stC] = 1

  while q:
    vr,vc = q.pop(0)

    for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
      newR = vr + dr
      newC = vc + dc
      if 0 <= newR < N and 0 <= newC < M and not visited[newR][newC]:
        if arr[newR][newC] == 1:
          q.append((newR,newC))
          visited[newR][newC] = visited[vr][vc] + 1
          if newR == enR and newC == enC:
            print(visited[newR][newC])
            
N, M = map(int,input().split())
arr = [list(map(int, input())) for _ in range(N)]

enR = N-1
enC = M-1
bfs(0,0)