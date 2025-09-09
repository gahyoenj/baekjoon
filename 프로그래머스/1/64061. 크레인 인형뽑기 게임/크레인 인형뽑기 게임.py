def solution(board, moves):
    answer = 0
    basket = []
    n = len(board)
    arr = []
    
    for c in range(n):
        col = []
        for r in range(n):
            if board[r][c] != 0:
                col.append(board[r][c])
        arr.append(col)
    
    # print(arr)
    
    for move in moves:
        move -= 1
        
        doll = 0
        if arr[move]:
            doll = arr[move].pop(0) 

        if basket and basket[-1] == doll:
            answer += 2
            basket.pop()
        elif doll != 0:
            basket.append(doll)

    return answer