def dfs(row, col,ans, cnt):
    global maxV

    for dr, dc in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
        newR = row + dr
        newC = col + dc
        if 0 <= newR < N and 0 <= newC < N and not visited[newR][newC]:
            if arr[newR][newC] < arr[row][col]:
                visited[newR][newC] = True
                dfs(newR,newC,ans+1,cnt)
                visited[newR][newC] = False
            elif arr[newR][newC] - arr[row][col] < K and cnt == 1:
                temp = arr[newR][newC]
                arr[newR][newC] = arr[row][col] - 1   # 최대한 덜 깎기
                visited[newR][newC] = True
                dfs(newR, newC, ans+1 ,0)
                arr[newR][newC] = temp
                visited[newR][newC] = False

    if ans > maxV:
        maxV = ans


T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_height = max(map(max, arr))
    maxV = 0
    for row in range(N):
        for col in range(N):
            if arr[row][col] == max_height:
                ans = 1  # 각 테스트 케이스마다 초기화
                visited = [[False] * N for _ in range(N)]
                visited[row][col] = True
                dfs(row, col, ans,1)  # cnt => 깎을 수 있는 횟수

    print(f'#{tc + 1} {maxV}')