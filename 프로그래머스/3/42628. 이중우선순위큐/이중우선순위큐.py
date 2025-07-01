import heapq

def solution(operations):
    answer = []
    
    for op in operations:
        command, data = op.split(" ")
        if command == 'I':
            heapq.heappush(answer,int(data))
        
        elif command == "D" and answer :
            if data == "-1":
                heapq.heappop(answer)
            else:
                answer.sort()
                answer.pop()
    maxV, minV = 0,0
    if answer:
        maxV = max(answer)
        minV = min(answer)
    
    answer = [maxV, minV]
    return answer