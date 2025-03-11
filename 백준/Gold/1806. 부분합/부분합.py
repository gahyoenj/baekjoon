n, s = map(int,input().split())
arr = list(map(int,input().split()))

sumV = 0
end = 0
minV = 2e19
check = False

for start in range(n):
    while sumV < s and end < n:
        sumV += arr[end]
        end += 1

    # print(start,end,sumV)
    if sumV >= s:
        length = end - start
        check = True
        if length < minV:
            minV = length

    sumV -= arr[start]

if check:
    print(minV)
else:
    print(0)