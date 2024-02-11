N = int(input())
result = []
for i in range(1000000):
  digits = [i]
  while i > 0:
      digit = i % 10
      digits.append(digit)
      i //= 10
  if sum(digits) == N:
    result.append(digits[0])
if result:    
  print(min(result))
else:
  print(0)