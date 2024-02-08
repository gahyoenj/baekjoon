T = int(input())
A = 0
B = 0
C = 0
if T >= 3000:
  A = T // 3000
  T -= A * 3000
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