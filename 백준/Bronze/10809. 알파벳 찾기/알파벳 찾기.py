S=list(map(str,input()))
for i in range(97,123):
  for j in range(len(S)):
    if chr(i) == S[j]:
      print(j,end=" ")
      break
  else:
    print(-1,end=" ")