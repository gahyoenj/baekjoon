N = int(input())
vote_list =[]
for _ in range(N):
  vote = int(input())
  vote_list.append(vote)
cnt = vote_list.count(1)
if cnt > len(vote_list) // 2:
  print("Junhee is cute!")
else:
  print("Junhee is not cute!")