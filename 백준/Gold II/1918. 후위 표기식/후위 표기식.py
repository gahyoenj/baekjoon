icp = {'+':1, '-':1, '*':2, '/':2, '(':3}
isp = {'+':1, '-':1, '*':2, '/':2, '(':0}
s = input()
STACK = []
result = ''
for c in s:
  if c.isupper():
    result += c
  elif c == ')':
    while STACK[-1] != '(':
      result += STACK.pop()
    STACK.pop()
  else:
    if STACK and icp[c] > isp[STACK[-1]]:
      STACK.append(c)
    else: 
      while STACK and icp[c] <= isp[STACK[-1]]:
        result += STACK.pop()
      STACK.append(c)
while STACK:
  result += STACK.pop()
print(result)