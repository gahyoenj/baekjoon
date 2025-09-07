t = int(input())
for T in range(1,t+1):
  n = int(input())
  f = [0] * (n+1)
  f[0] = 1
  f[1] = 1
  f[2] = 3

  for i in range(3,n+1):
    f[i] = f[i-1] + f[i-2] * 2 + f[i-3] 
  
  result = f[-1]

  print(f'#{T} {result}')