lst = []
num = []
a=1
for idx in range(30):
  num.append(a)
  a = a + 1
for idx in range(28):
  lst.append(int(input()))
n_lst= set(num) - set(lst)
minV = min(n_lst)
maxV = max(n_lst)
print(minV)
print(maxV)