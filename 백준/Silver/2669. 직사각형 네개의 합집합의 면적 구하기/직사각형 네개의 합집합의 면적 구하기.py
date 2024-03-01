lst = [[0]*100 for _ in range(100)]
for _ in range(4):
    x1,y1,x2,y2 = list(map(int, input().split()))
    for x in range(x1,x2):
        for y in range(y1,y2):
            if not lst[x][y]:
                lst[x][y] = 1


# print(lst)
result = 0
for i in range(100):
    for j in range(100):
        if lst[i][j]==1:
            result +=1

print(result)


