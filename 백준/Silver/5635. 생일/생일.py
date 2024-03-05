n = int(input())
lst = []
for _ in range(n):
    name,d,m,y = input().split()
    lst.append([2010-int(y),name,int(m),int(d)])
    # d = int(d)
    # m = int(m)
    # y = int(y)
    lst.sort()

for idx in range(1,len(lst)):
    if lst[idx-1][0] == lst[idx][0]:
        if lst[idx-1][2] < lst[idx][2]:
            lst[idx-1], lst[idx] = lst[idx], lst[idx-1]
        if lst[idx-1][2] == lst[idx][2]:
            if lst[idx-1][3] < lst[idx][3]:
                lst[idx-1], lst[idx] = lst[idx], lst[idx-1]
print(lst[0][1])
print(lst[-1][1])
