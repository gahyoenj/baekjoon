T = int(input())
for tc in range(T):
  s = input()
  STACK = []
  for c in s:
    if c == '(':
      STACK.append(c)
    elif c == ')':
      if STACK and STACK.pop() == '(':
        result = "YES"
        continue
      else:
        result = "NO"
        break
  if len(STACK) > 0 :
    result = "NO"

  print(result)