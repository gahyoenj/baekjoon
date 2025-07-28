def solution(sequence, k):
    answer = []
    
    s,e = 0,0
    minL = len(sequence) + 1
    sumV = 0
    
    while e <= len(sequence):
        if sumV == k:
            if e - s  < minL:
                minL = e-s
                answer = [s,e-1]
            
            sumV -= sequence[s]
            s += 1
        
        elif sumV < k:
            if e == len(sequence):
                break
            sumV += sequence[e]
            e += 1
    
        else:
            sumV -= sequence[s]
            s += 1
    
    return answer