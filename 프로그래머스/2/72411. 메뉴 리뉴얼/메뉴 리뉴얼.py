from itertools import combinations

def solution(orders, course):
    answer = []
    dic = {}

    for order in orders:
        lst = [n for n in order]
        lst.sort()
        for num in course:
            for combi in combinations(lst,num):
                menu = ''.join(combi)
                
                if menu in dic.keys():
                    dic[menu] += 1
                
                else:
                    dic[menu] = 1
    
    one = []
    
    for food in dic:
        if dic[food] == 1:
            one.append(food)
    
    for d in one:
        del dic[d]
    
    maxV = {}
    
    for num in course:
        maxV[num] = 0
    
    for c in dic:
        length = len(c)
        
        if maxV[length] < dic[c]:
            maxV[length] = dic[c]
    
    # print(maxV)
    
    for c in dic:
        length = len(c)
        
        if dic[c] == maxV[length]:
            answer.append(c)
        
    
    answer.sort()
    
    return answer