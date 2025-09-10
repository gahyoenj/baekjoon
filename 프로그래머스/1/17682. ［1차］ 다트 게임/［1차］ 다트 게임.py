def solution(dartResult):
    answer = 0
    
    score = []
    result = ''
    num = ''

    
    for r in dartResult:
        if r.isdigit():  
            if result:
                score.append(num + result)
                result = ''

            if num == '1' and r == '0':
                num += r   
            else:
                num = r

        else:  
            result += r
    
    if result:
        score.append(num+result)
    
    for idx in range(1,len(score)):
        if score[idx][-1] == '*':
            score[idx-1] += '*'
    
    for sc in score:
        num = ''
        for s in sc:
            if s.isdigit():
                num += s
            elif s in 'SDT':
                num = int(num)
                if s == 'D':
                    num = num ** 2
                elif s == 'T':
                    num = num ** 3
            else:
                if s == '*':
                    num = num * 2
                
                else:
                    num = num * (-1)
                    
        print(num)
        answer += num
    return answer