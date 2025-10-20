def solution(s):
    answer = 0
    cnt_x = 0
    cnt = 0
    
    x = s[0]
    
    for idx in range(len(s)):
        if s[idx] == x:
            cnt_x += 1
        else:
            cnt += 1
        
        if cnt == cnt_x:
            answer += 1
            cnt,cnt_x = 0,0
            if idx+1 < len(s):
                x = s[idx+1]
    if cnt or cnt_x:
        answer += 1
    return answer