s = str(input())
word = s.upper()
cnt = {}
maxS = []
maxV = 0
for i in word:
  cnt[i] = cnt.get(i, 0) + 1
  if cnt[i] > maxV:
    maxV = cnt[i]
for j in cnt:
  if cnt[j] == maxV:
    maxS.append(j)  
if len(maxS) >= 2:
  print('?')
else:
  print(''.join(maxS))