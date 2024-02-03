n = int(input())
Q1 = 0
Q2 = 0
Q3 = 0
Q4 = 0
axis = 0
for _ in range(n):
  x, y = map(int, input().split())
  if x > 0 and y > 0:
    Q1 += 1
  elif x < 0 and y > 0:
    Q2 += 1
  elif x < 0 and y < 0:
    Q3 += 1
  elif x > 0 and y < 0:
    Q4 += 1
  elif x == 0 or y == 0:
    axis += 1
print('Q1:', Q1)
print('Q2:', Q2)
print('Q3:', Q3)
print('Q4:', Q4)
print('AXIS:', axis)