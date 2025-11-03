from itertools import combinations
def solution(relation):
    answer = 0
    row = len(relation)
    col = len(relation[0])
    candidates = []
    for i in range(1,col+1):
        for combi in combinations(range(col),i):
            arr = []
            for item in relation:
                tup = []
                for c in combi:
                    tup.append(item[c])
                arr.append(tuple(tup))
            if len(set(arr)) == row:
                candidates.append(combi)
    result = []
    
    candidates.sort(key=len)
    for cand in candidates:
        minimality = True
        for res in result:
            sub = True
            for x in res:
                if x not in cand:
                    sub = False
                    break
            if sub:
                minimality = False
                break
        if minimality:
            result.append(cand)
            
    answer = len(result) 
    return answer