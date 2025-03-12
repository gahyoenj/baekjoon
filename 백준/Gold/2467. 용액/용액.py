n = int(input())
arr = list(map(int,input().split()))
arr.sort()

if arr[0] >= 0:
    print(arr[0], arr[1])
    exit()
elif arr[-1] < 0:
    print(arr[-2], arr[-1])
    exit()

sumV = 0

minV = 2e19
first = 0
last = 0

left = 0
right = n-1

while left < right:
    sumV = arr[left] + arr[right]

    if abs(sumV) < minV:
        minV = abs(sumV)
        first = arr[left]
        last = arr[right]

    if sumV < 0:
        left += 1

    else:
        right -= 1

print(first,last)