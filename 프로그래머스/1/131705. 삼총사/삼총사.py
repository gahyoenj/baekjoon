from itertools import combinations
def solution(number):
    answer = 0
    
    for lst in combinations(number,3):
        if sum(lst) == 0:
            answer += 1
    
    
    return answer