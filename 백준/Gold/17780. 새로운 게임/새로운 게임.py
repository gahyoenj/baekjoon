N,K = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(N)]

chess = [[[] for _ in range(N)] for _ in range(N)]
horse = [[] for _ in range(K+1)]
for i in range(K):
    row,col,dir = map(int,input().split())
    chess[row-1][col-1].append(i+1)
    horse[i+1] = (i+1,row-1,col-1,dir)

turn = -1

def finish():
    for row in range(N):
        for col in range(N):
            # print(len(chess[row][col]))
            if len(chess[row][col]) >= 4:
                return True
    return False
directions = [(0,1),(0,-1),(-1,0),(1,0)]

def change_dir(dir):
    if dir == 1:
        new_dir = 2
    elif dir == 2:
        new_dir = 1
    elif dir == 3:
        new_dir = 4
    else:
        new_dir = 3
    return new_dir

def blue_check(row,col,dir):
    new_dir = change_dir(dir)
    newR = row + directions[new_dir-1][0]
    newC = col + directions[new_dir-1][1]

    if newR<0 or newC<0 or newR >=N or newC>= N or board[newR][newC] == 2:
        return True
    return False


def move(row,col,dir):
    newR = row + directions[dir-1][0]
    newC = col + directions[dir-1][1]

    if newR < 0 or newC < 0 or newR >=N or newC >= N or board[newR][newC] == 2:
        if blue_check(row,col,dir):
            return row,col, change_dir(dir)
        else:
            new_dir = change_dir(dir)
            return move(row,col,new_dir)
    elif board[newR][newC] == 1:
        rev_horse = chess[row][col][::-1]
        for h in rev_horse:
            chess[newR][newC].append(h)
            horse_num,r,c,d = horse[h]
            horse[h] = [horse_num,newR,newC,d]
        chess[row][col] = []
    elif board[newR][newC] == 0:
        for h in chess[row][col]:
            chess[newR][newC].append(h)
            horse_num, r, c, d = horse[h]
            horse[h] = [horse_num, newR, newC, d]
        chess[row][col] = []
            # print(rev_horse)

    return newR,newC, dir

for t in range(1,1001):
    for piece in range(1,K+1):
        num,row,col,dir = horse[piece]
        # print(horse[piece])
        # print(row,col)
        # print(chess[row][col])
        if chess[row][col][0] == num:
            newR,newC,new_d = move(row,col,dir)
            horse[num] = [num,newR,newC,new_d]
        else:
            continue

    if finish():
        turn = t
        break

print(turn)