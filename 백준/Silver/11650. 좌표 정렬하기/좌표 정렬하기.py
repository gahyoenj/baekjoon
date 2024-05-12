N = int(input())
lst = []
for _ in range(N):
    xi,yi = map(int,input().split())
    lst.append([xi,yi])

lst.sort(key=lambda x:(x[0],x[1]))

# print(lst)

for x,y in lst:
    print(x,y)