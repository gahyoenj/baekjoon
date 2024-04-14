N = int(input())

lst = []
result = {}
for i in range(N):
    s = list(input())
    lst.append(s)

for i in range(N):
    for j in range(len(lst[i])):
        if lst[i][j] in result:
            result[lst[i][j]] += 10 ** (len(lst[i])-j-1)  # 자리에 맞게 추가
        else:
            result[lst[i][j]] = 10 **(len(lst[i])-j-1)
ans = []
for num in result.values():
    ans.append(num)
ans.sort(reverse=True)

sumV = 0
s = 9
for i in ans:
    sumV += i * s
    s -= 1

print(sumV)