def find_next(dice,num):
    for i in range(6):
        if dice[i] == num:
            idx = i
    if idx == 0:
        down = dice[5]
        maxV = max(dice[1:5])
    if idx == 1:
        down = dice[3]
        maxV = max(dice[0],dice[2],dice[4],dice[5])
    if idx == 2:
        down = dice[4]
        maxV = max(dice[0],dice[1],dice[3],dice[5])
    if idx == 3:
        down = dice[1]
        maxV = max(dice[0], dice[2], dice[4], dice[5])
    if idx == 4:
        down = dice[2]
        maxV = max(dice[0], dice[1], dice[3], dice[5])
    if idx == 5:
        down = dice[0]
        maxV = max(dice[1:5])
    return down,maxV
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0
for idx in range(6):
    next, maxV = find_next(arr[0],arr[0][idx])
    for j in range(1,N):
        nextV, max_V = find_next(arr[j],next)
        next = nextV
        maxV += max_V
    if maxV > result:
        result = maxV
print(result)