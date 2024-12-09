from itertools import combinations

def solution(friends, gifts):
    answer = 0
    dic = {}
    for f in friends:
        dic[f] = 0
    # print(dic)
    for A,B in combinations(friends,2):
        atob, btoa, ap, bp = 0, 0, 0, 0
        # print(A,B)
        for i in gifts:
            a,b = i.split(" ")
            if a == A:
                if b == B:
                    atob += 1   
                ap += 1
            elif a==B:
                if b ==A:
                    btoa += 1
                bp += 1
            elif b == A:
                ap -= 1
            elif b == B:
                bp -= 1
        if atob > btoa:
            dic[A] += 1
        elif atob < btoa:
            dic[B] += 1
        else:
            if ap > bp:
                dic[A] += 1
            elif ap < bp:
                dic[B] += 1
    answer = max(dic.values())
    return answer