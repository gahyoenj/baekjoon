N = int(input())
score = list(map(int, input().split()))
M = 0
for i in range(N):
  if score[i] >= M:
    M = score[i]
for i in range(N):
  score[i] = score[i]/M*100
avg = sum(score) / N
print(avg)