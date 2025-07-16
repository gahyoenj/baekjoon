from itertools import combinations

def solution(n, q, ans):
    answer = 0
    
    num = [i for i in range(1,n+1)]
    
    for combi in combinations(num,5):
        can = True
        for idx in range(len(q)):
            code = q[idx]
            cnt = ans[idx]
            j = set(combi)-set(code)
            if 5- len(j) != cnt:
                can = False
                break
        if can:
            answer += 1
    
    return answer