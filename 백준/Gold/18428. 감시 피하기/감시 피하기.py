from itertools import combinations

def check(row, col):
    for dr, dc in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
        for n in range(1, N+1):
            newR = row + dr * n
            newC = col + dc * n
            if 0 <= newR < N and 0 <= newC < N:
                if corridor[newR][newC] == 'O':  # 장애물 만나면 break
                    break
                elif corridor[newR][newC] == 'S':  # 학생을 발견하면 True
                    return True
    return False

def monitoring():
    for i, j in teacher:
        if check(i, j):
            return True
    return False

N = int(input())

corridor = [list(input().split(' ')) for _ in range(N)]

teacher = []
empty = []

for i in range(N):
    for j in range(N):
        if corridor[i][j] == 'T':
            teacher.append([i, j])
        elif corridor[i][j] == 'X':
            empty.append([i, j])

hide = False
for comb in combinations(empty, 3):
    for x, y in comb:
        corridor[x][y] = 'O'

    if not monitoring():  # 학생이 감시되지 않으면 성공
        hide = True
        break

    for x, y in comb:
        corridor[x][y] = 'X'

if hide:
    print("YES")
else:
    print("NO")
