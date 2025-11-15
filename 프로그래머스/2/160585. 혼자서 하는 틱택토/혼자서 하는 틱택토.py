def solution(board):
    def check(board,ch):
        for r in range(3):
            if board[r][0] == board[r][1] == board[r][2] == ch:
                return True
        
        for c in range(3):
            if board[0][c] == board[1][c] == board[2][c] == ch:
                return True
        
        if board[0][0] == board[1][1] == board[2][2] == ch:
            return True
        if board[0][2] == board[1][1] == board[2][0] == ch:
            return True
        
        return False
    answer = -1
    cnt_o = 0
    cnt_x = 0

    for row in range(3):
        for col in range(3):
            if board[row][col] == 'O':
                cnt_o += 1
            elif board[row][col] == 'X':
                cnt_x += 1

    if cnt_x > cnt_o:
        return 0
    elif cnt_o > cnt_x + 1:
        return 0
    else:
        win_o = check(board,'O')
        win_x = check(board,'X')
        
        if win_o and win_x:
            return 0
        
        elif win_o and cnt_o != cnt_x + 1:
            return 0
        elif win_x and cnt_o != cnt_x:
            return 0
        
    return 1