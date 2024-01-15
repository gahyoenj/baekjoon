lst = []
for idx in range(10):
  lst.append(int(input()))
for idx in range(10):
  lst[idx] = lst[idx] % 42
  idx = idx + 1
lst = set(lst)
print(len(lst))