def solution(elements):
    answer = 0
    l = len(elements)
    elements = elements * 2
    result = set()
    
    for length in range(1,l+1):
        for start in range(l):
            result.add(sum(elements[start:start+length]))
    answer = len(result)
    return answer