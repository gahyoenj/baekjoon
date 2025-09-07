def solution(board, skill):
    answer = 0
    N = len(board)
    M = len(board[0])
    arr = [[0] * (M+1) for _ in range(N+1)]
    for t,r1,c1,r2,c2,degree in skill:
        if t == 1:
            degree = -degree
        
        arr[r1][c1] += degree
        arr[r1][c2+1] -= degree
        arr[r2+1][c1] -= degree
        arr[r2+1][c2+1] += degree
        
    for r in range(N+1):
        for c in range(1, M+1):
            arr[r][c] += arr[r][c-1]


    for c in range(M+1):
        for r in range(1, N+1):
            arr[r][c] += arr[r-1][c]

        
    # print(arr)

    
    for r in range(N):
        for c in range(M):
            if board[r][c] + arr[r][c]> 0:
                answer += 1
    return answer