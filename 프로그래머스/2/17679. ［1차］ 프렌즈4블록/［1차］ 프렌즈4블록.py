def solution(m, n, board):
    answer = 0
    
    board = [list(i) for i in board]
    
    while True:
        arr = set()
        for row in range(m-1):
            for col in range(n-1):
                if board[row][col] != 0 and board[row][col] == board[row+1][col] == board[row][col+1] == board[row+1][col+1]:
                    arr.add((row,col))
                    arr.add((row,col+1))
                    arr.add((row+1,col))
                    arr.add((row+1,col+1))
        
        if not arr:
            break
        answer += len(arr)

        arr = list(arr)

        while arr:
            r,c = arr.pop()
            board[r][c] = 0
        # print(board)

        for j in range(n):
            st = []
            for i in range(m):
                if board[i][j] !=0 :
                    st.append(board[i][j])

            for i in range(m-1,-1,-1):
                if st:
                    board[i][j] = st.pop()
                else:
                    board[i][j] = 0
    
    print(board)
            
    
    return answer