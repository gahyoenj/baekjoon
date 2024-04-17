def check(lst):
    visited = [False] * N
    for i in range(N-1):
        if abs(lst[i] - lst[i+1]) > 1 : return False
        if lst[i] == lst[i+1] : continue
        if lst[i] - lst[i+1] == 1:    # 그 다음이 1 작은 경우
            if visited[i+1] : return False
            visited[i+1] = True
            for idx in range(1,L):
                if i+1+idx >= N:
                    return False
                elif lst[i] - lst[i+1+idx] == 1 and not visited[i+1+idx]:
                    visited[i+1+idx] = True
                    continue
                else:
                    return False
            continue
        if lst[i+1] - lst[i] == 1:   # 전이 1 작은 경우
            if visited[i]: return False
            visited[i] = True
            for idx in range(1,L):
                if i-idx < 0 :
                    return False
                elif lst[i+1] - lst[i-idx] == 1 and not visited[i-idx]:
                    visited[i-idx] = True
                    continue
                else:
                    return False
            continue
    return True


N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
for row in range(N):
    if check(arr[row]):
        cnt += 1

arr_col = list(zip(*arr))

for row in range(N):
    if check(arr_col[row]):
        cnt += 1

print(cnt)