a,b = map(int, input().split())
c,d = map(int, input().split())
e,f = map(int, input().split())
if a == c :
  dot_a = e
elif c == e:
  dot_a = a
else:
  dot_a = c
if b == d:
  dot_b = f
elif b == f:
  dot_b = d
else:
  dot_b = b
print(dot_a, dot_b)