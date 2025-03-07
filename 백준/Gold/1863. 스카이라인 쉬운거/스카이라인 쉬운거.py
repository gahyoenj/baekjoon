n = int(input())

change = []

cnt = 0

for _ in range(n):
    x,y = map(int,input().split())
    while change and change[-1] > y:
        change.pop()
        cnt += 1
    if change and change[-1] == y:
        continue
    change.append(y)

while change:
    if change[-1] > 0:
        cnt += 1
    change.pop()

# print(change)
print(cnt)