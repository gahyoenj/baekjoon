N,M,L,K = map(int,input().split())

zone = []
maxV = 0
maxY = 0
for _ in range(K):
    x,y = map(int,input().split())
    zone.append((x,y))

for i in range(K):
    for j in range(K):
        cnt = 0
        nx = min(zone[i][0],zone[j][0])
        ny = min(zone[i][1],zone[j][1])

        for x,y in zone:
            if nx <= x <= nx+L and ny<=y<=ny+L:
                cnt += 1

        if cnt > maxV:
            maxV = cnt

print(K-maxV)
