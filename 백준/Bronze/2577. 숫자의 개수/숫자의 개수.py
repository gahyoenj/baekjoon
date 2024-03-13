A = int(input())
B = int(input())
C = int(input())

n = A * B * C

n_str = str(n)
lst = []
for s in n_str:
    lst.append(int(s))

for i in range(10):
    print(lst.count(i))