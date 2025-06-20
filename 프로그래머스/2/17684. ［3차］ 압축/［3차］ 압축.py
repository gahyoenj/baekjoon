def solution(msg):
    answer = []
    dic = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    
    idx = 1
    maxV = 1
    
    while msg:
        if msg[0:idx] in dic:
            answer.append(dic.index(msg[:idx])+1)
            dic.append(msg[:idx+1])
            
            msg = msg[idx:]
            maxV =  max(idx+1, maxV)
            idx = maxV
            
        else : 
            idx -= 1
    
    return answer