T = int(input())
for test_case in range(T):
  equation = input().split()
  for i in range(1,len(equation)):
    if equation[i] == '@':
      equation[0] =float(equation[0]) * 3
    if equation[i] == '%':
      equation[0] =float(equation[0]) + 5
    if equation[i] == '#':
      equation[0] =float(equation[0]) - 7
  result = float(equation[0])
  print("{:.2f}".format(result))