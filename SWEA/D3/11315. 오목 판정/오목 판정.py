T = int(input())
for tc in range(T):
    N = int(input())
    arr = [input() for _ in range(N)]

    dr = [0,1,1,1]
    dc = [1,0,1,-1]
    result = 'NO'
    for row in range(N):
        for col in range(N):
            if arr[row][col] == 'o':
                for i in range(4):
                    cnt = 0
                    for power in range(1,5):
                        newR = row + dr[i] * power
                        newC = col + dc[i] * power
                        if 0 <= newR < N and 0 <= newC < N:
                            if arr[newR][newC] == 'o':
                                cnt += 1
                        else:
                            break

                    if cnt == 4:
                        result = 'YES'
                        break

    print(f'#{tc+1} {result}')