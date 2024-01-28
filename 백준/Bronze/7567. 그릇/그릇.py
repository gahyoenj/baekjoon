dish = str(input())
height = 10

for idx in range(1,len(dish)):
  if dish[idx] == dish[idx-1]:
    height += 5
  else:
    height += 10
print(height)