def solution(nums):
    answer = 0
    n = len(nums)
    pick = n // 2
    if len(set(nums)) <= pick:
        answer = len(set(nums))
    else:
        answer = pick
    return answer