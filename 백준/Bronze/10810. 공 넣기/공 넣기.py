N, M = map(int, input().split())
N_lst = [0]*N
for test_case in range (M):
  i, j, k =map(int, input().split())
  for j in range(i-1,j):
    N_lst[j]=k
for ball in N_lst:
  print(ball, end=' ')