R, C = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

lst = [[1]* C for _ in range(R)]
chess = []
for row in range(R):
    for col in range(C):
        chess.append((row,col,arr[row][col]))

chess.sort(key = lambda x: x[2], reverse=True)   # 가장 큰 수부터 탐색하기 위해

for row,col,num in chess:
    cnt = lst[row][col]
    minV = arr[row][col]  # 가장 큰수를 일단 min이라고 잡아둠
    minR = row
    minC = col
    for dr,dc in [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(1,-1),(-1,1),(1,1)]:
        newR = row + dr
        newC = col + dc
        if 0<=newR<R and 0<=newC<C:
            if minV > arr[newR][newC]:   # 8방향 보면서 그 값이 현재 값보다 작으면 min관련 값들 바꿔줌
                minR = newR
                minC = newC
                minV = arr[newR][newC]
    lst[minR][minC] += cnt
    lst[row][col] -= cnt


# print(lst)
for result in lst:
    print(*result)
