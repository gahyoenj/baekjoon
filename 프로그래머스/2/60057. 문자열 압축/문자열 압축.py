def solution(s):
    answer = 2e10
    if len(s) == 1:
        return 1
    
    for unit in range(1,len(s)//2 + 1):
        char = s[:unit]
        cnt = 1
        result = ''
        for idx in range(unit,len(s),unit):
            current = s[idx:idx+unit]
            if char == current:
                cnt += 1
            else:
                if cnt > 1:
                    result += (str(cnt)+char)
                else:
                    result += char
                char = current
                cnt = 1
        if cnt > 1:
                result += (str(cnt)+char)
        else:
            result += char
        
        if len(result) < answer:
            answer = len(result)
    return answer