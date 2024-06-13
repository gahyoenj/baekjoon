import sys
input = sys.stdin.readline
def dfs(vr, vc, cnt):
    global maxV
    visited[ord(board[vr][vc]) - ord('A')] = True
    maxV = max(maxV, cnt)


    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        newR, newC = vr + dr, vc + dc
        if 0 <= newR < R and 0 <= newC < C and not visited[ord(board[newR][newC]) - ord('A')]:
            dfs(newR, newC, cnt + 1)

    visited[ord(board[vr][vc]) - ord('A')] = False


R, C = map(int, input().split())
board = [input().rstrip() for _ in range(R)]
visited = [False] * 26

maxV = 1
dfs(0, 0, 1)
print(maxV)
