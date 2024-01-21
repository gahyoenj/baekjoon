k, q, l, b, n, p = list(map(int,input().split()))
if k != 1:
  k = 1-k
elif k == 1:
  k = 0
if q != 1:
  q = 1-q
elif q ==1:
  q = 0
if l != 2:
  l = 2-l
elif l == 2:
  l = 0
if b != 2:
  b =2 - b
elif b ==2:
  b = 0
if n != 2:
  n = 2- n
elif n ==2:
  n = 0
if p != 8:
  p = 8 - p
elif p == 8:
  p = 0
print (k, q, l, b, n, p)