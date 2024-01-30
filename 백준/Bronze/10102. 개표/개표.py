V = int(input())
vote = str(input())
A_cnt = 0
B_cnt = 0
for vote_cnt in vote:
  if vote_cnt == 'A':
    A_cnt += 1
  if vote_cnt == 'B':
    B_cnt += 1

if A_cnt > B_cnt:
  print('A')
elif A_cnt < B_cnt:
  print('B')
else:
  print('Tie')