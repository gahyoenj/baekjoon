def spread(dust):
    for fine,row, col in dust:
        cnt = 0
        for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
            newR = row + dr
            newC = col + dc
            if 0<=newR<R and 0<=newC<C and room[newR][newC] != -1:
                cnt += 1
                room[newR][newC] += fine//5
        room[row][col] -= fine//5 * cnt



R,C,T = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(R)]

for _ in range(T):
    dust = []
    clean = []
    for row in range(R):
        for col in range(C):
            if room[row][col] != -1 and room[row][col] != 0:
                dust.append((room[row][col],row,col))
            if room[row][col] == -1:
                clean.append((row,col))



    spread(dust)

    # 공기청정기 작동하기
    upi = clean[0][0]
    upj = clean[0][1]

    downi = clean[1][0]
    downj = clean[1][1]
    

    # 위쪽
    for r in range(upi - 1, 0, -1):  # 아래로이동
        room[r][0] = room[r - 1][0]
    for c in range(C - 1):  # 왼쪽이동
        room[0][c] = room[0][c + 1]
    for r in range(upi):  # 위로이동
        room[r][C - 1] = room[r + 1][C - 1]
    for c in range(C - 1, 1, -1):  # 오른쪽
        room[upi][c] = room[upi][c - 1]
    room[upi][1] = 0

    # 아래쪽
    for r in range(downi + 1, R - 1):  # 위로 이동
        room[r][0] = room[r + 1][0]
    for c in range(C - 1):  # 왼쪽이동
        room[R - 1][c] = room[R - 1][c + 1]
    for r in range(R - 1, downi, -1):  # 아래쪽이동
        room[r][C - 1] = room[r - 1][C - 1]
    for c in range(C - 1, 1, -1):  # 오른쪽
        room[downi][c] = room[downi][c - 1]
    room[downi][1] = 0
# print(room)
ans = 0
for row in range(R):
    for col in range(C):
        if room[row][col] > 0:
            ans += room[row][col]

print(ans)