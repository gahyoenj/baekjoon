def solution(n, words):
    answer = []

    w = [words[0]]
    cnt = 0
    num = 0

    
    for idx in range(1,len(words)):
        if words[idx] in w:
            cnt = (idx // n) + 1
            num = (idx % n) + 1
            break
            
        elif w[-1][-1] != words[idx][0]:
            cnt = (idx // n) + 1
            num = (idx % n) + 1
            break
        
        w.append(words[idx])
    
    answer = [num,cnt]

    return answer