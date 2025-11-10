from itertools import combinations
def solution(nums):
    answer = 0

    for num in combinations(nums,3):
        number = sum(num)
        isPrime = True
        for i in range(2,int(number**0.5)+1):
            if number % i == 0:
                isPrime = False
                break
        if isPrime:
            answer += 1
    return answer