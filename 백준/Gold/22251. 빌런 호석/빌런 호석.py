n,k,p,x = map(int,input().split())

num = [[1,1,1,1,1,1,0],[0,1,1,0,0,0,0],[1,1,0,1,1,0,1],
       [1,1,1,1,0,0,1],[0,1,1,0,0,1,1],[1,0,1,1,0,1,1],
       [1,0,1,1,1,1,1],[1,1,1,0,0,0,0],[1,1,1,1,1,1,1],
       [1,1,1,1,0,1,1]]

diff = [[] for _ in range(10)]


for i in range(10):
    for j in range(10):
        cnt = 0
        for K in range(7):
            if num[i][K] != num[j][K]:
               cnt += 1
        diff[i].append(cnt)

# print(diff)

current = str(x)
if len(current) < k:
    current = '0' * (k - len(current)) + current


ans = 0
for i in range(1,n+1):
    if i == x:
        continue
    cnt = 0

    number = str(i)

    if len(number) < k:
        number = '0' * (k - len(number)) + number

    # print(number)
    for idx in range(k):
        cnt += diff[int(number[idx])][int(current[idx])]

    if cnt <= p:
        # print(cnt,number)
        ans += 1
print(ans)