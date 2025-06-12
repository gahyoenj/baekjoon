def solution(s):
    answer = []
    tup = []
    
    lst = []
    t = ''
    
    for c in s:
        if c.isdigit() or c == ',':
            t+= c
        
        if c == '}' and t:
            if t[0] == ',':
                t = t[1:]
            
            tup.append(t)
            t = ''
    
    
    for string in tup:
        st = string.split(',')
        lst.append(st)
    
    
    lst = sorted(lst,key=len)
    
    # print(lst)
    
    for t in lst:
        for num in t:
            if int(num) not in answer:
                answer.append(int(num))
    
    return answer