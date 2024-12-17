from collections import defaultdict

def solution(participant, completion):
    answer = ''
    dic = defaultdict(int)
    
    for part in participant:
        dic[part] += 1
    
    for comp in completion:
        dic[comp] -= 1
    
    for key, value in dic.items():
        if value > 0:  # 값이 0보다 큰 경우 미완주자
            answer = key
            break
    
    return answer
