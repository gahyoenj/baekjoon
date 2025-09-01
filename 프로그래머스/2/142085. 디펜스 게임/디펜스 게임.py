import heapq
def solution(n, k, enemy):
    answer = 0
    heap = []
    
    for i in range(len(enemy)):
        en = enemy[i]
        
        n -= en
        heapq.heappush(heap,-en)
        if n < 0:
            if k > 0:
                v = heapq.heappop(heap)
                n -= v
                k -= 1
                answer += 1
            else:
                break
        else:
            answer += 1        
                
            
    
    return answer