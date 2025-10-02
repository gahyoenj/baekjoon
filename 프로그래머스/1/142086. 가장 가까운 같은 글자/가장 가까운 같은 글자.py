def solution(s):
    answer = []    
    dic = {}
    
    for idx in range(len(s)):
        c = s[idx]
        if c not in dic:
            dic[c] = idx
            answer.append(-1)
        else:
            answer.append(idx-dic[c])
            dic[c] = idx
    
    
    return answer