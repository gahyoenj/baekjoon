N, M = map(int, input().split())
arr = list(map(int, input().split()))
minV = 300000
result = 0
for i in range(N-2):
  for j in range(i+1, N-1):
    for k in range(j+1, N):
      sumV = arr[i] + arr[j] + arr[k]
      if  0 <= M - sumV < minV:
        minV = M - sumV
        result = sumV
print(result)