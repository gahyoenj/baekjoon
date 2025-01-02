from itertools import permutations

def check(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    lst = []
    for i in range(1, len(numbers) + 1):

        numlst = set(int(''.join(p)) for p in permutations(numbers, i))
        lst.extend(numlst)
    print(set(lst)) 
    for num in set(lst):
        if num == 0 or num == 1:pass
        else:
            if check(num):
                print(num)
                answer += 1
    return answer
