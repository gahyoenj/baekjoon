lst = []
maxV = 0
pos = 1
maxP = 0
for idx in range(9):
  lst.append(int(input()))
  if maxV < lst[idx]:
    maxV = lst[idx]
    maxP = pos
  pos = pos + 1
print(maxV)
print(maxP)