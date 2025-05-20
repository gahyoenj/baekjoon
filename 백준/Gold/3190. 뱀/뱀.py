N = int(input())
K = int(input())

apple = []
for _ in range(K):
    r,c = map(int,input().split())
    apple.append((r,c))

L = int(input())

move = []
for _ in range(L):
    x,c = input().split()
    x = int(x)
    move.append((x,c))

X,Y = 1,1

body = [(X,Y)]
directions = [(0,1),(1,0),(0,-1),(-1,0)]
dir = 0
time = 0
while True:
    time += 1
    dx,dy = directions[dir]
    x,y = body[-1]
    nx = x + dx
    ny = y + dy


    if nx < 1 or ny < 1 or nx > N or ny > N:
        break

    if (nx,ny) in body:
        break

    body.append((nx, ny))

    if (nx,ny) in apple:
        apple.remove((nx,ny))

    else:
        body.pop(0)

    if move and time == move[0][0]:
        if move[0][1] == 'D':
            dir = (dir+1) % 4

        elif move[0][1] == 'L':
            dir = (dir-1) % 4

        move.pop(0)


print(time)