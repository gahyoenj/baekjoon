def solution(clothes):
    answer = 0
    classification = {}
    for name, category in clothes:
        if category not in classification:
            classification[category] = []
        
        classification[category].append(name)
    
    multi = 1
    
    for key in classification.keys():
        multi *= (len(classification[key])+1)
        
    answer += (multi - 1)
    return answer