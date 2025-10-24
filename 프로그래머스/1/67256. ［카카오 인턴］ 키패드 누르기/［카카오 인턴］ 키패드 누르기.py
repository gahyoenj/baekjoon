def solution(numbers, hand):
    answer = ''
    keypad = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    
    curL = (3,0)
    curR = (3,2)
    
    for num in numbers:
        if num in [1,4,7]:
            for row in range(len(keypad)):
                for col in range(3):
                    if keypad[row][col] == num:
                        curL = (row,col)
                        answer += 'L'
        elif num in [3,6,9]:
            for row in range(len(keypad)):
                for col in range(3):
                    if keypad[row][col] == num:
                        curR = (row,col)
                        answer += 'R'
        else:
            moveL, moveR = 0,0
            move = (0,0)
            for row in range(len(keypad)):
                for col in range(3):
                    if keypad[row][col] == num:
                        moveL = abs(curL[0] - row) + abs(curL[1] - col)
                        moveR = abs(curR[0] - row) + abs(curR[1] - col)
                        move = (row,col)
            if moveL < moveR:
                curL = move
                answer += 'L'
            elif moveL > moveR:
                curR = move
                answer += 'R'
            else:
                if hand == 'left':
                    curL = move
                    answer += 'L'
                else:
                    curR = move
                    answer += 'R'
            
            
    
    return answer