def solution(s, n):
    answer = ''
    
    for char in s:
        if char == " ":
            answer += " "
            continue
        origin = ord(char)
        num = ord(char) + n
        
        if num > 122:
            num -= 26
        
        elif origin <= 90 and num > 90:
            num -= 26
        
        answer += chr(num)
    
    return answer