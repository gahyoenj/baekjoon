from itertools import product

def solution(word):
    answer = 0
    alpha = ['A','E','I','O','U']
    words = []
    for i in range(1,6):
        for w in product(alpha,repeat=i):
            words.append(''.join(w))
    
    words.sort()
    answer = words.index(word) + 1
    return answer