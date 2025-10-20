def solution(survey, choices):
    answer = ''
    n = len(survey)
    result = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    for i in range(n):
        if choices[i] == 4:
            continue
        else:
            score = abs(choices[i] - 4)
            if choices[i] > 4:
                result[survey[i][1]] += score
            else:
                result[survey[i][0]] += score
    # print(result)
    for char in ['RT','CF','JM','AN']:
        if result[char[0]] < result[char[1]]:
            answer += char[1]
        else:
            answer += char[0]
        
    return answer