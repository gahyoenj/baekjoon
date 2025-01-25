A,B = map(int,input().split())

def bfs(start):
    q = []
    q.append((start,1))

    while q:
        now,cnt = q.pop(0)
        if now > B:
            continue
        if now == B:
            return cnt

        q.append((int(str(now)+"1"), cnt + 1))
        q.append((now*2, cnt + 1))

    return -1


print(bfs(A))