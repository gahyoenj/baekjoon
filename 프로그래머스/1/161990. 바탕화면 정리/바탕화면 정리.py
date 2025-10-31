def solution(wallpaper):
    answer = []
    n = len(wallpaper)
    m = len(wallpaper[0])
    minR = max(n,m)
    minC = minR
    maxR, maxC = 0,0
    for row in range(n):
        for col in range(m):
            if wallpaper[row][col] == '#':
                minR = min(row,minR)
                minC = min(col,minC)
                maxR = max(row,maxR)
                maxC = max(col,maxC)
    answer = [minR,minC,maxR+1,maxC+1]
    return answer