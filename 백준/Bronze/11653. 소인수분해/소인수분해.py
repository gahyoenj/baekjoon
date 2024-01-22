N = int(input())
d = 2
numbers = []
while N >= d:
  if N % d == 0:
    N = N//d
    numbers.append(d)
  else:
    d += 1
for num in numbers:
  print(num)