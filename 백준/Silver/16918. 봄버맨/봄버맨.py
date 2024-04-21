def bomb(lst):
    while lst:
        vr,vc = lst.pop(0)
        arr[vr][vc] = '.'
        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            newR = vr + dr
            newC = vc + dc
            if 0<=newR<R and 0<=newC<C and arr[newR][newC] == 'O':
                arr[newR][newC] = '.'

R, C, N = map(int, input().split())

arr = [list(input()) for _ in range(R)]

if N % 2 == 0:
    for _ in range(R):
        print('O' * C)
else:
    N = N//2
    for _ in range(N):
        bomb_lst = []
        for row in range(R):
            for col in range(C):
                if arr[row][col] == 'O':
                    bomb_lst.append((row,col))
        arr = [['O' for _ in range(C)] for _ in range(R)]
        bomb(bomb_lst)

    for i in range(R):
        for j in range(C):
            print(arr[i][j],end='')
        print()