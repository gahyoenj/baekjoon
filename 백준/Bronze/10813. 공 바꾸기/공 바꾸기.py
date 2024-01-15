N, M = map(int, input().split())
N_lst = []
a= 1
for idx in range(N):
  N_lst.append(a)
  a = a + 1
for test_case in range(M):
  i, j = map(int,input().split())
  N_lst[i-1], N_lst[j-1] = N_lst[j-1],N_lst[i-1]
for ball in N_lst:
  print(ball, end=' ')