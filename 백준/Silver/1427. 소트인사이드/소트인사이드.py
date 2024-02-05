N = list(map(int,input()))

for i in range(len(N)-1, 0, -1):
    for j in range(i):
        if N[j] < N[j+1]:
            N[j], N[j+1] = N[j+1], N[j]
for num in N:
    print(num, end='')