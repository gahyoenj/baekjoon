a= int(input())
b= int(input())
c= int(input())
d= int(input())
e= int(input())
score_list = [a, b, c, d, e]
for i in range(len(score_list)):
  if score_list[i] < 40:
    score_list[i] = 40
avg = sum(score_list)/len(score_list)
print(int(avg))