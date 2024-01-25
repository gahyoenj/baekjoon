T = int(input())
for test_case in range(T):
  score = 0
  cnt = 0
  score_input = str(input())
  for i in range(len(score_input)):
    if score_input[i] =='O':
      cnt += 1
      score += cnt
    if score_input[i] =='X':
      cnt = 0
  print(score)