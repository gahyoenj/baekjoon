T = int(input())
for test_case in range(T):
  R, S = list(map(str,input().split()))
  R = int (R)
  S = list(map(str,S))
  for i in range(len(S)):
      S[i] = S[i]*R 
      print(S[i],end="")
  print()