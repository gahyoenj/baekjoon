import heapq
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
jewerly =[]
for _ in range(N):
    M,V = map(int, input().split())
    jewerly.append((M,V))

jewerly.sort(key=lambda x:x[0])
bag = []
heap = []
ans = 0
for _ in range(K):
    Ci = int(input())
    bag.append(Ci)
bag.sort()

for num in bag:
    while jewerly and jewerly[0][0]<=num:
        heapq.heappush(heap,-jewerly[0][1])
        heapq.heappop(jewerly)   # 적은 무게부터 비교하고 있었으므로 jewerly에 최소힙을 이용해 pop 하면 최소 무게 제거됨.
    if heap:
        ans -= heapq.heappop(heap)
print(ans)
