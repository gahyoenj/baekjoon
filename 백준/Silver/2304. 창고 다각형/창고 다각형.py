N = int(input())
lst = []
maxV = 0
for _ in range(N):
    L, H = map(int, input().split())
    lst.append([L,H])
lst.sort()   # 밑면 기준으로 정렬

i = 0
for l_lst in lst:
    if l_lst[1] > maxV:
        maxV = l_lst[1]
        idx = i
    i += 1
# print(idx)

h = lst[0][1]   # 첫번째 기둥 높이

for i in range(idx):    # 최대 높이 전까지
    if h < lst[i+1][1]:
        maxV += h * (lst[i+1][0] - lst[i][0])
        h = lst[i+1][1]
    else:
        maxV += h * (lst[i+1][0] - lst[i][0])

h = lst[-1][1]
for i in range(N-1,idx,-1):
    if h < lst[i-1][1]:
        maxV += h * abs(lst[i - 1][0] - lst[i][0])
        h = lst[i-1][1]
    else:
        maxV += h * abs(lst[i - 1][0] - lst[i][0])

print(maxV)
