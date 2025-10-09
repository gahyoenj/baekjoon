def solution(s):
    answer = ''
    c = ''
    dic = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4',
           'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    for char in s:
        if char.isdigit():
            answer += char
        else:
            c += char
            
            if c in dic.keys():
                answer += dic[c]
                c = ''
    answer = int(answer)
    
    return answer