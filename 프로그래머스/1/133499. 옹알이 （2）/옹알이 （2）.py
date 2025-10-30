def solution(babbling):
    answer = 0
    speak = ['aya','ye','woo','ma']
    for word in babbling:
        w = ''
        idx = 0
        pronounce = True
        while idx < len(word):
            can = False
            
            for s in speak:
                if word[idx:idx+len(s)] == s and s!= w:
                    w = s
                    idx += len(s)
                    can = True
                    break
            if not can:
                pronounce = False
                break
        if pronounce:
            answer += 1
    return answer