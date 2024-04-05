def bfs():
    global ans
    while q:
        for _ in range(len(water_q)):  # 물먼저 퍼지게
            wr,wc = water_q.pop(0)


            for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                new_wr = wr + dr
                new_wc = wc + dc
                if 0<=new_wr < R and  0<=new_wc<C:
                    if arr[new_wr][new_wc] == '.' or arr[new_wr][new_wc] =='S':
                        arr[new_wr][new_wc] = '*'
                        water_q.append((new_wr,new_wc))
        for _ in range(len(q)):  # 고슴도치 이동
            vr,vc = q.pop(0)

            for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                nr = vr + dr
                nc = vc + dc
                if 0<=nr < R and  0<=nc<C:
                    if arr[nr][nc] == '.':
                        arr[nr][nc] = 'S'
                        q.append((nr,nc))
                    elif arr[nr][nc] == 'D':
                        print(ans)
                        return

        ans +=1
    print('KAKTUS')
    return

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
q = []
water_q = []
ans = 1
for row in range(R):
    for col in range(C):
        if arr[row][col] == 'S':
            q.append((row,col))
        elif arr[row][col] == '*':
            water_q.append((row,col))
bfs()