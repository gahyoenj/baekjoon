import sys
N = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))

num = set(card)
length = len(num)
my_dict = {}

for i in num:
    my_dict[i] = 0

for i in card:
    my_dict[i] += 1

# print(my_dict)

for i in check:
    if i in my_dict:
        print(my_dict[i],end=' ')
    else:
        print(0, end=' ')