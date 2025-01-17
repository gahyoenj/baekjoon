import copy

N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]

directions = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]


def see(x, y, dirs, office):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for d in dirs:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                break
            if office[nx][ny] == 6:
                break
            if office[nx][ny] == 0:
                office[nx][ny] = -1


def dfs(cctv, office):
    global min_blind_spots

    stack = [(cctv, office)]

    while stack:
        current_cctv, current_office = stack.pop()

        if not current_cctv:
            blind_spots = sum(row.count(0) for row in current_office)
            min_blind_spots = min(min_blind_spots, blind_spots)
            continue

        num, row, col = current_cctv.pop()

        for dirs in directions[num]:
            new_office = copy.deepcopy(current_office)
            see(row, col, dirs, new_office)
            stack.append((current_cctv[:], new_office))

    return


cctv = []
for row in range(N):
    for col in range(M):
        if 1 <= office[row][col] <= 5:
            cctv.append((office[row][col], row, col))

min_blind_spots = float('inf')
dfs(cctv, office)

print(min_blind_spots)
