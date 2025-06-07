from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    finish = []
    across = deque()

    while truck_weights or across:
        answer += 1
        for i in range(len(across)):
            across[i][1] += 1
            
        if across and across[0][1] > bridge_length:
            across.popleft()
        
        if truck_weights and len(across) < bridge_length and sum(x[0] for x in across)+truck_weights[0] <= weight:
            truck = truck_weights.popleft()
            across.append([truck,1])
        
        
            
            
    return answer