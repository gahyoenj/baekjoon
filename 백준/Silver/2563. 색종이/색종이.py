N = int(input())
arr = [[0] * 100 for _ in range(100)]
for _ in range(N):
    w, h = map(int, input().split())
    for row in range(w,w+10):
        for col in range(h,h+10):
            if not arr[row][col]:
                arr[row][col] = 1
# print(arr)

result = 0
for row in range(100):
    for col in range(100):
        if arr[row][col] == 1:
            result += 1
print(result)