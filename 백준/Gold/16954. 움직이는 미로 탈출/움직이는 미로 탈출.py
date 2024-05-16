from collections import deque
chess = [list(input()) for _ in range(8)]

visited = [[0]*8 for _ in range(8)]

def bfs():
    q = deque()
    q.append((7,0))

    # visited[7][0] = 1
    while q:

        for _ in range(len(q)):
            vr,vc = q.popleft()
            if chess[vr][vc] == '#':
                continue

            if vr == 0 and vc == 7:
                return True
            for dr,dc in [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,1),(1,-1),(0,0)]:
                newR = vr + dr
                newC = vc + dc
                if newR == 0 and newC == 7:
                    return True
                if 0<=newR < 8 and 0<=newC<8:
                    if chess[newR][newC] =='.':
                        q.append((newR,newC))
                        # visited[newR][newC] = visited[vr][vc] + 1


        chess.insert(0,['.']*8)
        chess.pop()

    return False

result = bfs()

if result:
    print(1)
else:
    print(0)