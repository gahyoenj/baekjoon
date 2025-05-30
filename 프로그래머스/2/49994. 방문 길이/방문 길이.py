def solution(dirs):
    answer = 0
    visited = []
    move = {'U':(0,1),'D':(0,-1),'R':(1,0),'L':(-1,0)}
    row, col = 0,0
    
    for d in dirs:
        dr,dc = move[d]
        newR = row + dr
        newC = col + dc
        if -5<=newR<=5 and -5<=newC<=5:
            check = [(row,col),(newR,newC)]
            check.sort()
            if check not in visited:
                visited.append(check)
            
            row = newR
            col = newC
    
    answer = len(visited)
    
    
    return answer