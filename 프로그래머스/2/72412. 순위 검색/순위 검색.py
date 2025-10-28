from itertools import combinations
def solution(info, query):
    answer = []
    arr = []
    
    info_dict = {}
    for i in info:
        information = i.split()
        score = int(information[-1])
        condition = information[:-1]
        for n in range(5):
            for combi in combinations(range(4),n):
                temp = condition.copy()
                for idx in combi:
                    temp[idx] = '-'
                key = ''.join(temp)
                if key not in info_dict:
                    info_dict[key] = []
                info_dict[key].append(score)
    for key in info_dict:
        info_dict[key].sort()
    
    for q in query:
        question = q.split()
        l = question[0]
        p = question[2]
        e = question[4]
        f = question[6]
        s = int(question[7])
        
        key = ''.join([l,p,e,f])
        
        if key in info_dict:
            score = info_dict[key]
            left,right = 0,len(score)
            while left < right:
                mid = (left+right) // 2
                if score[mid] < s:
                    left = mid + 1
                else:
                    right = mid
            answer.append(len(score)-left)
        else:
            answer.append(0)
        

    return answer