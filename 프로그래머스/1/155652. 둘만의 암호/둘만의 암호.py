def solution(s, skip, index):
    answer = ''
    for alphabet in s:
        cnt = 0
        idx = ord(alphabet)
        
        while cnt < index:
            idx += 1
            
            if idx > 122:
                idx = 97
            
            if chr(idx) in skip:
                continue
            
            cnt += 1
        
        answer += chr(idx)
    return answer