# 2475
arr = list(map(int, input().split()))

for i in range(len(arr)):
    arr[i] = arr[i] **2

sumV = sum(arr)

print(sumV%10)
    