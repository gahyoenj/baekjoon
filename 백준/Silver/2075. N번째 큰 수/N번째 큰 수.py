import heapq

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]


heap = []
for i in range(n):
    for j in range(n):
        heapq.heappush(heap,lst[i][j])

        if len(heap) > n:
            heapq.heappop(heap)

print(heap[0])
