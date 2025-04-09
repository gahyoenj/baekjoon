n, k = map(int,input().split())
arr = list(map(int,input().split()))

num = {}
start = 0
end = 0
maxV = 0
for i in range(n):
    num[arr[i]] = 0
while start <= end:
    if end == n:
        break
    if num[arr[end]] < k:
        num[arr[end]] += 1
        end += 1
    else:
        num[arr[start]] -= 1
        start += 1

    length = end - start
    if length > maxV:
        maxV = length

print(maxV)
