N = int(input())
for test_case in range(N):
  r, e, c =map(int, input().split())
  if r > e-c:
    print('do not advertise')
  elif r == e-c:
    print('does not matter')
  else:
    print('advertise')
