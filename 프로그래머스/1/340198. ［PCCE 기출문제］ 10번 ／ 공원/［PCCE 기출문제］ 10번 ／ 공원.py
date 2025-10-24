def solution(mats, park):
    answer = 0
    n = len(park)
    m = len(park[0])
    mats.sort(reverse=True)
    for size in mats:
        for row in range(n):
            for col in range(m):
                if park[row][col] != '-1':
                    continue
                else:
                    if row + size <= n and col + size <= m:
                        square = True
                        for r in range(row,row+size):
                            for c in range(col,col+size):
                                if park[r][c] != '-1':
                                    square = False
                                    break
                            if not square:
                                break
                        if square:
                            return size
    return -1