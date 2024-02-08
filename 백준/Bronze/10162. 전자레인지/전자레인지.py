T = int(input())
A = 0
B = 0
C = 0
if T >= 300:
  A = T // 300
  T -= A * 300
if T >= 60:
  B = T // 60
  T -= B * 60
if T >= 10:
  C = T // 10
  T -= C * 10
  
if T == 0:
  print(A, B, C)
else:
  print(-1)