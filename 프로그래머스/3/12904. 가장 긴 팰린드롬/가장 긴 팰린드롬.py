def solution(s):
    answer = 1
    if len(s) == 1:
        return 1
    
    maxV = 0
    
    for i in range(len(s)):
        left, right = i,i
        while left >=0 and right < len(s) and s[left] == s[right]:
            if right-left+1 > maxV:
                maxV = right-left+1
            
            left -= 1
            right += 1
        
        left,right = i,i+1
        while left >= 0 and right <len(s) and s[left] == s[right]:
            if right-left+1 > maxV:
                maxV = right-left+1
            
            left -= 1
            right += 1
    
    answer = maxV
    return answer