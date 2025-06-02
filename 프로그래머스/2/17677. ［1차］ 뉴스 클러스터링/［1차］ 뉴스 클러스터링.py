from collections import Counter

def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    A = []
    B = []
    
    for idx in range(len(str1)-1):
        s = str1[idx:idx+2]
        
        if s.isalpha():
            A.append(s)
            
    for idx in range(len(str2)-1):
        s = str2[idx:idx+2]
        
        if s.isalpha():
            B.append(s)
    
    if not A and not B:
        answer = 1
    
    else:
        union = []
        union_set = set(A + B)
        
        for elem in union_set:
            count_a = A.count(elem)
            count_b = B.count(elem)
            cnt = max(count_a,count_b)
            union.extend([elem]*cnt)
        
        inter = []
        for elem in A:
            if elem in B:
                inter.append(elem)
                B.remove(elem)
        
        print(inter)
        print(union)
        answer = len(inter) / len(union)
    
    answer *= 65536
    answer = int(answer)
    return answer