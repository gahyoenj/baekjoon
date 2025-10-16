def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    element = {'code':0,'date':1,'maximum':2,'remain':3}
    data.sort(key=lambda x:x[element[ext]])
    
    s,e = 0, len(data)
    
    while s < e:
        mid = (s+e) // 2
        if data[mid][element[ext]] < val_ext:
            s = mid + 1
        else:
            e = mid
    
    answer = data[:s]
    
    answer.sort(key=lambda x:x[element[sort_by]])
    
    return answer