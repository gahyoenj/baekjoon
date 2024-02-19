N , K = map(int, input().split())
arr = list(map(int, input().split()))
sumV = 0
end = 0
start = 0
maxV = -100 * N
while end < N:
  sumV += arr[end]
  if end - start + 1 < K:
    end += 1
  elif end - start + 1 == K:
    maxV = max(maxV, sumV)
    sumV -= arr[start]
    start += 1
    end += 1
print(maxV)