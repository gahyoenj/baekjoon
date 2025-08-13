def solution(name, yearning, photo):
    answer = []
    score = {}
    
    for idx in range(len(name)):
        score[name[idx]] = yearning[idx]
    
    for arr in photo:
        s = 0
        for person in arr:
            if person in score:
                s += score[person]
        
        answer.append(s)
    
    return answer