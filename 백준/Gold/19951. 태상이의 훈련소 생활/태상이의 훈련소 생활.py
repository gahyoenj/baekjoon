N, M = map(int, input().split())

Hi = list(map(int, input().split()))
arr = [0] * (N+1)

for _ in range(M):
    a,b,k = map(int, input().split())
    arr[a-1] += k
    arr[b] -= k

sub_sum = 0
for i in range(N):
    sub_sum += arr[i]
    print(Hi[i]+sub_sum, end=' ')