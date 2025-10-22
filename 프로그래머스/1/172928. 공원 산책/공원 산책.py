def solution(park, routes):
    answer = []
    w = len(park[0])
    h = len(park)
    r,c = 0,0
    for row in range(h):
        for col in range(w):
            if park[row][col] == 'S':
                r = row
                c = col
    direction = {'N':(-1,0),'S':(1,0),'W':(0,-1),'E':(0,1)}
    for route in routes:
        d,p = route.split(" ")
        flag = True
        for i in range(1,int(p)+1):
            newR = r + direction[d][0] * i
            newC = c + direction[d][1] * i
            if not(0<= newR< h and 0<=newC<w) or park[newR][newC] == 'X':
                flag = False
                break
        
        if flag:
            r += direction[d][0] * int(p)
            c += direction[d][1] * int(p)
    answer = [r,c]
        
    return answer