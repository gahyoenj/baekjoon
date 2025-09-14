from itertools import combinations
def solution(numbers):
    answer = []
    for nums in combinations(numbers,2):
        if not sum(nums) in answer:
            answer.append(sum(nums))
    answer.sort()
        
    return answer