def solution(board):
    answer = 0
    rowL = len(board)
    colL = len(board[0])
    
    dp = [[0] * colL for _ in range(rowL)]
    
    for row in range(rowL):
        for col in range(colL):
            if board[row][col]:
                if row == 0 or col == 0:
                    dp[row][col] = 1
                else:
                    dp[row][col] = min(dp[row-1][col],dp[row][col-1],dp[row-1][col-1])+1
            
                answer = max(dp[row][col],answer)
    return answer * answer