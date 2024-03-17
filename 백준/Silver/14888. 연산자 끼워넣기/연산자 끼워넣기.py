import sys
from itertools import permutations

def ans():
    global maxV,minV
    for perm in permutations(lst, N-1):
        total = arr[0]
        for r in range(1,N):
            if perm[r-1] == '+':
                total += arr[r]
            elif perm[r-1] == '-':
                total -= arr[r]
            elif perm[r-1] == '*':
                total *= arr[r]
            elif perm[r-1] == '/':
                total = int(total/arr[r])

        if total > maxV:
            maxV = total
        if total < minV:
            minV = total


input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
operator = list(map(int,input().split()))

plus = operator[0]
minus = operator[1]
multi = operator[2]
divi = operator[3]

lst = []
for _ in range(plus):
    lst.append('+')
for _ in range(minus):
    lst.append('-')
for _ in range(multi):
    lst.append('*')
for _ in range(divi):
    lst.append('/')
# print(lst)

minV = 1e9
maxV = -1e9
ans()

print(int(maxV))
print(int(minV))