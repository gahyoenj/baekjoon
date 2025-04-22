def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    
    while answer < len(citations):
        if citations[answer] >= answer + 1:
            answer += 1
        else:
            break
    
    return answer