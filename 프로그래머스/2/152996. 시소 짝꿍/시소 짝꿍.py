def solution(weights):
    answer = 0
    
    weights.sort()
    dic = {}
    
    for w in weights:
        if w in dic:
            answer += dic[w]
        
        if w% 2==0 and w//2 in dic:
            answer += dic[w//2]
        
        if (w*2) % 3 == 0 and (w*2) //3 in dic:
            answer += dic[(w*2) // 3]
        
        if (w*3) % 4 == 0 and (w*3) // 4 in dic:
            answer += dic[(w*3) // 4]
        
        dic[w] = dic.get(w, 0) + 1
    
    
    return answer