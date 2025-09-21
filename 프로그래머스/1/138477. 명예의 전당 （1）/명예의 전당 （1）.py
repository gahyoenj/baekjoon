import heapq
def solution(k, score):
    answer = []
    heap = []
    for s in score:
        if len(heap) < k:
            heapq.heappush(heap,s)
            answer.append(heap[0])
        
        else:
            if heap[0] < s:
                minV = heapq.heappop(heap)
                heapq.heappush(heap,s)
                answer.append(heap[0])
            else:
                answer.append(heap[0])
    
            
    return answer