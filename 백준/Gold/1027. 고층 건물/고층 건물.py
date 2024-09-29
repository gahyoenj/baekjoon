N = int(input())
building = list(map(int, input().split()))
ans = 0
for idx in range(N):
    maxA = float('-inf')  # 오른쪽 방향에서의 최대 기울기
    minB = float('inf')  # 왼쪽 방향에서의 최대 기울기
    cnt = 0
    for i in range(idx+1,N):
        if (building[i]-building[idx]) / (i-idx) > maxA:
            maxA = (building[i]-building[idx]) / (i-idx)
            cnt += 1

    for i in range(idx-1,-1,-1):
        if (building[i]-building[idx]) / (i-idx) < minB:
            minB = (building[i]-building[idx]) / (i-idx)
            cnt += 1

    if cnt > ans:
        ans = cnt

print(ans)